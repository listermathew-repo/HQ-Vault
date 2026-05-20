---
title: "Code project review"
date: 2026-04-23
created: 2026-04-23T03:10:06.731625Z
updated: 2026-04-23T03:14:57.089894Z
source: claude
category: trading
tags: ["project", "review", "code", "trading"]
people: []
projects: []
related: []
message_count: 6
uuid: 775f96a8-c3d7-4a1d-a432-68a6962b2a07
---


**You:** can you review a project in claude code

**Claude:** Yes! Claude Code has solid project review capabilities. Here's how it works:

**For general project/codebase review (in the terminal):**
Claude Code can explore and analyze your entire codebase autonomously. You can simply open it in your project directory and ask things like:
- *"Review this codebase and summarize the architecture"*
- *"Find potential bugs or security issues"*
- *"What areas of this project need improvement?"*

Claude reads files autonomously, identifies relevant code, and preserves compatibility by examining existing patterns — verbose, context-heavy prompts are usually no longer necessary.

**For PR/pull request review (`/code-review` command):**
On a PR branch, you can run `/code-review` locally (outputs to terminal) or `/code-review --comment` to post the review as a PR comment. Claude launches 4 review agents in parallel, scores each issue for confidence, and outputs issues with 80+ confidence — covering things like missing error handling, memory leaks, and naming convention violations.

**For automated GitHub PR reviews (Code Review feature):**
Code Review is in research preview, available for Team and Enterprise subscriptions. It analyzes your GitHub pull requests and posts findings as inline comments, with a fleet of specialized agents examining code changes in the context of your full codebase — looking for logic errors, security vulnerabilities, broken edge cases, and subtle regressions.

**Tips for better reviews:**
- Add a `CLAUDE.md` file to your repo root with project context and conventions
- Add a `REVIEW.md` for review-specific instructions — use it to change what gets flagged, at what severity, and how findings are reported. Keep it focused; a long `REVIEW.md` dilutes the rules that matter most.

What kind of project review are you looking to do — a local codebase audit, PR review, or something else?

**You:** can you review custom coding session and this  in claude code

and provide

can you review tradingview and disable all alerts; perform the markup of the levels
if you cannot set up the alarms for today, advise me and I will do them
what else? What is the setup and entry for EURO. the % trade size and the TP and SL

**Claude:** Let me search for the available tools to interact with TradingView.Good, I have a browser tab. Let me navigate to TradingView now.I'm not able to access TradingView through the browser in this environment — the network is restricted for direct site access. Here's a clear breakdown of what I can and can't help with:

---

**What I can't do from here:**
- **Disable alerts** on TradingView — I cannot access the site directly. You'll need to do this yourself in TradingView (Alerts panel → select all → delete/disable), or via your `tradingview-mcp` in Claude Code by asking it to manage alerts.
- **Draw/markup levels** on your live chart — this requires direct chart access. In Claude Code with tradingview-mcp, you could try prompting: *"Draw key support/resistance levels on EURUSD"* if the MCP has drawing tool access.
- **Set today's alarms** — same restriction. **You'll need to set these yourself today.** I'd recommend doing it manually given the time sensitivity.

---

**What I'd advise for EURUSD (general framework — not financial advice):**

For your own analysis, here's the standard structure to work through:

- **Setup:** Is price at a key HTF (higher timeframe) level — daily/4H support or resistance? Is there confluence (e.g., a round number, previous high/low, 50/200 EMA)?
- **Entry trigger:** Look for a lower TF (15m/1H) confirmation — e.g., a rejection candle, break of structure, or engulfing pattern at the level.
- **Trade size:** A common rule is **1–2% account risk per trade** maximum. Size your position so your stop loss = 1–2% of account.
- **TP:** Aim for at minimum a **1:2 risk-to-reward**. Mark the next significant level as your target.
- **SL:** Place just beyond the level/swing — not too tight. Typically 10–20 pips beyond the structure on EURUSD depending on timeframe.

---

**To get a proper EURUSD-specific setup from Claude Code with tradingview-mcp**, try prompting it in your Claude Code terminal:

```
"Analyze EURUSD on the 4H chart. Identify key support and resistance levels, current price action setup, and suggest an entry, stop loss, and take profit."
```

Would you like me to help you draft a detailed prompt for your Claude Code + TradingView MCP session?

**You:** yes

**Claude:** Here's a detailed prompt you can paste directly into your Claude Code terminal with the tradingview-mcp connected:

---

```
You are connected to TradingView via MCP. Please complete the following tasks in order:

---

## TASK 1 — CLEAR ALL ALERTS
- Open the Alerts panel
- Select all existing alerts
- Disable or delete every alert
- Confirm when done

---

## TASK 2 — EURUSD CHART MARKUP
Switch to EURUSD on the 4H chart and mark up the following levels:

1. **Current Day High & Low** — draw horizontal lines, label them "Today High" / "Today Low"
2. **Previous Day High & Low** — draw horizontal lines, label them "PDH" / "PDL"
3. **Weekly Open** — horizontal line labelled "Weekly Open"
4. **Key Support Zones** — identify the 2–3 nearest significant support levels below current price
5. **Key Resistance Zones** — identify the 2–3 nearest significant resistance levels above current price
6. **200 EMA on 4H** — if not already on chart, add it
7. **Any visible Fair Value Gaps (FVGs)** on the 4H or 1H — box them

Report back all levels with their exact prices.

---

## TASK 3 — EURUSD TRADE SETUP ANALYSIS
Using the current chart after markup, analyse and report:

**Bias:**
- What is the current HTF (Daily / 4H) directional bias? Bullish or Bearish?
- Is price at a premium or discount relative to the weekly range?

**Setup:**
- What is the current price action setup? (e.g. rejection at resistance, break and retest, consolidation breakout)
- Is there confluence? (Level + EMA + FVG + session timing)

**Entry:**
- What is the suggested entry price or zone?
- Entry type: limit order or market order on confirmation?
- What 1H or 15m trigger confirms the entry? (e.g. engulfing candle, BOS, rejection wick)

**Stop Loss:**
- Where should the SL be placed? (just beyond structure / swing)
- SL in pips from entry?

**Take Profit:**
- TP1 (conservative) — first significant level
- TP2 (full target) — next major level
- TP in pips for each

**Risk Management:**
- Suggested risk per trade: 1–2% of account
- Risk:Reward ratio for this setup
- If R:R is below 1:2, advise to skip the setup

**Session:**
- Is this setup best taken in London open, NY open, or wait for next session?

---

## TASK 4 — SET TODAY'S ALERTS
Based on the levels identified, set price alerts for:
- PDH and PDL
- Today's key resistance (for short trigger)
- Today's key support (for long trigger)
- Any FVG midpoint that price may revisit

If you are unable to create alerts via MCP, list the exact price levels so I can set them manually.

---

Report everything clearly with prices, pips, and reasoning.
```

---

**How to use it:**
1. Open your Claude Code terminal
2. Make sure `tradingview-mcp` is active (you can see it in your tab bar)
3. Paste the entire prompt above and hit Enter
4. Claude Code will work through each task sequentially

If the MCP can't set alerts, it will give you the exact levels at the end of Task 4 so you can set them manually in under a minute. Want me to also draft a shorter daily routine version of this prompt you can reuse each morning?