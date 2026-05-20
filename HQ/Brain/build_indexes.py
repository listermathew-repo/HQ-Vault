#!/usr/bin/env python3
"""
Phase 3: Build index files from enriched conversation metadata.
Run after all tagging agents complete.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

CONVERSATIONS_DIR = Path(__file__).parent / "Conversations"
INDEX_DIR = Path(__file__).parent / "Index"

def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}

    fm_text = match.group(1)
    fm = {}

    for line in fm_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Parse JSON arrays
            if value.startswith('[') and value.endswith(']'):
                try:
                    fm[key] = json.loads(value)
                except:
                    fm[key] = [v.strip() for v in value[1:-1].split(',')]
            else:
                fm[key] = value

    return fm

def build_people_index():
    """Build People.md from all conversations."""
    people_map = defaultdict(list)

    for conv_file in CONVERSATIONS_DIR.rglob("*.md"):
        try:
            content = conv_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)

            people = fm.get('people', [])
            if isinstance(people, str):
                people = [p.strip() for p in people.strip('[]').split(',')]

            title = fm.get('title', conv_file.stem)
            rel_path = conv_file.relative_to(CONVERSATIONS_DIR)

            for person in people:
                if person and person.lower() != 'nan':
                    people_map[person].append(str(rel_path))
        except Exception as e:
            print(f"  Error reading {conv_file.name}: {e}")

    # Build markdown
    lines = [
        "# People",
        "",
        "Index of people mentioned across conversations.",
        "",
    ]

    for person in sorted(people_map.keys()):
        convs = people_map[person]
        conv_links = ", ".join([f"[[{Path(c).stem}]]" for c in convs[:3]])
        if len(convs) > 3:
            conv_links += f", and {len(convs)-3} more"
        lines.append(f"- **{person}** — {conv_links}")

    output = "\n".join(lines)
    (INDEX_DIR / "People.md").write_text(output, encoding='utf-8')
    print(f"[OK] Built People.md with {len(people_map)} people")

def build_topics_index():
    """Build Topics.md from all conversations."""
    topics_map = defaultdict(lambda: defaultdict(int))

    for conv_file in CONVERSATIONS_DIR.rglob("*.md"):
        try:
            content = conv_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)

            category = fm.get('category', 'other')
            tags = fm.get('tags', [])

            if isinstance(tags, str):
                tags = json.loads(tags) if tags.startswith('[') else [t.strip() for t in tags.split(',')]

            for tag in tags:
                if tag and tag.lower() != 'nan':
                    topics_map[category][tag] += 1
        except Exception as e:
            print(f"  Error reading {conv_file.name}: {e}")

    # Build markdown
    lines = [
        "# Topics",
        "",
        "Index of topics organized by category.",
        "",
    ]

    for category in sorted(topics_map.keys()):
        lines.append(f"## {category.title()}")
        lines.append("")

        for topic in sorted(topics_map[category].keys(),
                           key=lambda x: topics_map[category][x],
                           reverse=True):
            count = topics_map[category][topic]
            lines.append(f"- `{topic}` ({count})")

        lines.append("")

    output = "\n".join(lines)
    (INDEX_DIR / "Topics.md").write_text(output, encoding='utf-8')
    print(f"[OK] Built Topics.md with {sum(len(v) for v in topics_map.values())} unique topics")

def build_timeline_index():
    """Build Timeline.md with chronological conversation list."""
    convs = []

    for conv_file in CONVERSATIONS_DIR.rglob("*.md"):
        try:
            content = conv_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)

            date_str = fm.get('date', '2026-01-01')
            title = fm.get('title', conv_file.stem)
            source = fm.get('source', 'unknown')
            category = fm.get('category', 'other')

            convs.append({
                'date': date_str,
                'title': title,
                'file': conv_file.relative_to(CONVERSATIONS_DIR),
                'source': source,
                'category': category,
            })
        except Exception as e:
            print(f"  Error reading {conv_file.name}: {e}")

    # Sort by date
    convs.sort(key=lambda x: x['date'], reverse=True)

    # Build markdown
    lines = [
        "# Timeline",
        "",
        "Chronological index of all conversations (newest first).",
        "",
    ]

    current_month = None
    for conv in convs:
        # Parse date for grouping
        try:
            dt = datetime.strptime(conv['date'], '%Y-%m-%d')
            month_str = dt.strftime('%B %Y')
        except:
            month_str = 'Unknown Date'

        # Add month header
        if month_str != current_month:
            if current_month:
                lines.append("")
            lines.append(f"## {month_str}")
            lines.append("")
            current_month = month_str

        # Add conversation link
        source_badge = f"**{conv['source'].upper()}**" if conv['source'] != 'unknown' else ""
        cat_badge = f"`{conv['category']}`"
        lines.append(f"- [{conv['date']}] {source_badge} {cat_badge} [[{conv['file'].stem}]] — {conv['title']}")

    output = "\n".join(lines)
    (INDEX_DIR / "Timeline.md").write_text(output, encoding='utf-8')
    print(f"[OK] Built Timeline.md with {len(convs)} conversations")

def main():
    print("=== Building Index Files ===\n")

    try:
        build_people_index()
        build_topics_index()
        build_timeline_index()

        print(f"\n[OK] All indexes built successfully")
        print(f"Output: {INDEX_DIR}")
    except Exception as e:
        print(f"[ERROR] {e}")
        raise

if __name__ == '__main__':
    main()
