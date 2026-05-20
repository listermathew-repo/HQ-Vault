#!/usr/bin/env python3
"""
Convert Claude and Gemini conversations to Obsidian markdown vault.
Phase 1: Structural conversion with basic tagging and frontmatter.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
import re
import glob

# Configuration
VAULT_ROOT = Path(__file__).parent.parent
BRAIN_DIR = Path(__file__).parent
OUTPUT_CLAUDE_DIR = BRAIN_DIR / "Conversations" / "Claude"
OUTPUT_GEMINI_DIR = BRAIN_DIR / "Conversations" / "Gemini"
INDEX_DIR = BRAIN_DIR / "Index"

# Category keywords
CATEGORY_KEYWORDS = {
    "trading": ["vwap", "pine", "strategy", "macd", "rsi", "eurusd", "audusd", "fibonacci", "tradingview", "capital.com", "journal", "setup", "chart"],
    "legal": ["capgemini", "redundancy", "settlement", "complaint", "witness", "lawyer", "hr", "employment", "case"],
    "finance": ["salary", "loan", "interest", "transfer", "aud", "gbp", "asx", "portfolio", "investment", "money", "pay"],
    "technology": ["claude", "mcp", "obsidian", "python", "script", "code", "api", "github", "powershell", "editor", "compiler"],
    "research": ["duke", "astro", "peptide", "history", "government", "news", "investigation"],
    "personal": ["resume", "language", "preferences", "cover letter", "things to review", "notes"],
    "admin": ["organizing", "knowledge", "guide", "setup"]
}

def sanitize_filename(title: str, max_len: int = 80) -> str:
    """Sanitize title to be a safe filename."""
    # Remove special characters, keep alphanumeric, dash, space
    safe = re.sub(r'[^\w\s\-]', '', title)
    # Replace multiple spaces with single space
    safe = re.sub(r'\s+', ' ', safe).strip()
    # Limit length
    if len(safe) > max_len:
        safe = safe[:max_len].rsplit(' ', 1)[0]
    return safe.replace(' ', '_')

def detect_category(title: str, content: str = "") -> str:
    """Detect category from title and optional content keywords."""
    text = (title + " " + content).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    return "personal"  # default

def extract_initial_tags(title: str, category: str) -> List[str]:
    """Extract initial tags from title and category."""
    tags = [category]
    # Add simple keyword tags from title
    words = re.findall(r'\b[\w\-]+\b', title.lower())
    for word in words:
        if len(word) > 3 and word not in ["that", "this", "with", "from", "into", "over"]:
            tags.append(word)
    return list(set(tags))[:10]  # Limit to 10 tags

def convert_claude_conversations():
    """Convert Claude conversations.json to individual markdown files."""
    print("Loading Claude conversations...")
    conv_file = BRAIN_DIR / "Claude Data" / "conversations.json"

    with open(conv_file, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    print(f"Loaded {len(conversations)} conversations")

    # Create output directory
    OUTPUT_CLAUDE_DIR.mkdir(parents=True, exist_ok=True)

    converted = 0
    skipped = 0

    for conv in conversations:
        # Skip empty conversations
        if not conv.get('chat_messages'):
            skipped += 1
            continue

        uuid = conv.get('uuid', 'unknown')
        title = conv.get('name', 'Untitled').strip()
        if not title:
            title = f"Conversation {uuid[:8]}"

        created_at = conv.get('created_at', '')
        updated_at = conv.get('updated_at', '')

        # Parse dates
        try:
            created_dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            date_str = created_dt.strftime('%Y-%m-%d')
        except:
            date_str = datetime.now().strftime('%Y-%m-%d')

        # Detect category
        content_preview = ' '.join([m.get('text', '')[:200] for m in conv['chat_messages'][:3]])
        category = detect_category(title, content_preview)

        # Extract tags
        tags = extract_initial_tags(title, category)

        # Build content
        messages = []
        message_count = len(conv['chat_messages'])

        for msg in conv['chat_messages']:
            sender = msg.get('sender', 'unknown')
            # Filter content blocks: skip tool_use, tool_result, thinking, token_budget
            text_parts = []
            for content_block in msg.get('content', []):
                content_type = content_block.get('type', '')
                if content_type == 'text':
                    text_parts.append(content_block.get('text', ''))

            full_text = ''.join(text_parts).strip()
            if not full_text:
                full_text = msg.get('text', '')

            if full_text:
                if sender == 'human':
                    messages.append(f"**You:** {full_text}")
                else:
                    messages.append(f"**Claude:** {full_text}")

        # Build frontmatter
        frontmatter = f"""---
title: "{title}"
date: {date_str}
created: {created_at}
updated: {updated_at}
source: claude
category: {category}
tags: {json.dumps(tags)}
people: []
projects: []
related: []
message_count: {message_count}
uuid: {uuid}
---
"""

        # Build body
        body = '\n\n'.join(messages) if messages else "(No messages)"

        # Write file
        safe_title = sanitize_filename(title)
        filename = f"{date_str} {safe_title}.md"
        filepath = OUTPUT_CLAUDE_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write('\n\n')
            f.write(body)

        converted += 1
        if converted % 20 == 0:
            print(f"  Converted {converted} Claude conversations...")

    print(f"[OK] Converted {converted} Claude conversations, skipped {skipped} empty")
    return converted

def convert_gemini_conversations():
    """Convert Gemini .txt conversation files to markdown."""
    print("Loading Gemini conversations...")

    gemini_dir = BRAIN_DIR / "Gemini Data" / "Takeout" / "Gemini in Workspace" / "Conversation History"

    if not gemini_dir.exists():
        print("  (Gemini Data directory not found, skipping)")
        return 0

    txt_files = list(gemini_dir.glob("conversation_*.txt"))
    print(f"Found {len(txt_files)} Gemini conversation files")

    OUTPUT_GEMINI_DIR.mkdir(parents=True, exist_ok=True)

    converted = 0
    for txt_file in txt_files:
        try:
            with open(txt_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            conv_turns = data.get('conversation_turns', [])
            if not conv_turns:
                continue

            # Extract date from last turn
            date_str = datetime.now().strftime('%Y-%m-%d')
            title = f"Gemini Conversation {txt_file.stem}"

            # Try to get date from first turn
            for turn in conv_turns:
                if 'user_turn' in turn:
                    turn_modified = turn['user_turn'].get('turn_last_modified', '')
                    if turn_modified:
                        try:
                            dt = datetime.fromisoformat(turn_modified.replace('Z', '+00:00'))
                            date_str = dt.strftime('%Y-%m-%d')
                            break
                        except:
                            pass

            # Infer category from content
            content_preview = ' '.join([
                turn.get('user_turn', {}).get('prompt', '')[:100]
                for turn in conv_turns[:3]
            ])
            category = detect_category(title, content_preview)
            tags = extract_initial_tags(content_preview, category)

            # Build messages
            messages = []
            for turn in conv_turns:
                if 'user_turn' in turn:
                    prompt = turn['user_turn'].get('prompt', '').strip()
                    if prompt:
                        messages.append(f"**You:** {prompt}")

                if 'system_turn' in turn:
                    text_blocks = turn['system_turn'].get('text', [])
                    for block in text_blocks:
                        if isinstance(block, dict):
                            text = block.get('data', '').strip()
                        else:
                            text = str(block).strip()
                        if text:
                            messages.append(f"**Gemini:** {text}")

            # Build frontmatter
            frontmatter = f"""---
title: "{title}"
date: {date_str}
created: {date_str}T00:00:00Z
source: gemini
category: {category}
tags: {json.dumps(tags)}
people: []
projects: []
related: []
message_count: {len(messages)}
uuid: {txt_file.stem}
---
"""

            # Build body
            body = '\n\n'.join(messages) if messages else "(No messages)"

            # Write file
            safe_title = sanitize_filename(content_preview[:60])
            filename = f"{date_str} {safe_title}.md"
            filepath = OUTPUT_GEMINI_DIR / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(frontmatter)
                f.write('\n\n')
                f.write(body)

            converted += 1

        except Exception as e:
            print(f"  Error processing {txt_file.name}: {e}")
            continue

    print(f"[OK] Converted {converted} Gemini conversations")
    return converted

def create_index_stubs():
    """Create placeholder index files."""
    print("Creating index files...")

    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    files = {
        'People.md': """# People

Index of people mentioned across conversations.

(To be populated by tagging agents)
""",
        'Topics.md': """# Topics

Index of topics organized by category.

(To be populated by tagging agents)
""",
        'Timeline.md': """# Timeline

Chronological index of all conversations.

(To be populated by indexing script)
"""
    }

    for filename, content in files.items():
        filepath = INDEX_DIR / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"[OK] Created {len(files)} index files")

def main():
    print("=== Brain Conversation Converter ===\n")

    claude_count = convert_claude_conversations()
    print()
    gemini_count = convert_gemini_conversations()
    print()
    create_index_stubs()

    print(f"\n=== Summary ===")
    print(f"Total converted: {claude_count + gemini_count} conversations")
    print(f"  Claude: {claude_count}")
    print(f"  Gemini: {gemini_count}")
    print(f"\nOutput directories:")
    print(f"  {OUTPUT_CLAUDE_DIR}")
    print(f"  {OUTPUT_GEMINI_DIR}")
    print(f"  {INDEX_DIR}")

if __name__ == '__main__':
    main()
