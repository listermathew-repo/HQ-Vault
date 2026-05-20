---
title: "Trading journal formulas setup"
date: 2026-03-17
created: 2026-03-17T07:31:23.377648Z
updated: 2026-03-17T07:34:12.702039Z
source: claude
category: trading
tags: ["journal", "formulas", "setup", "trading", "excel", "performance-tracking"]
people: []
projects:
  - "Trading Journal"
related:
  - "2026-03-17 Setting_up_Pine_Script_in_Claude_Code.md"
  - "2026-03-18 VWAP_Pine_Script_trading_strategy.md"
message_count: 2
uuid: 771330f4-335e-4bf2-9882-76dd044ccfff
---

## Links

### Trading Setup
- [[Setting up Pine Script in Claude Code]]
- [[VWAP Pine Script trading strategy]]

### Tools
- Excel/LibreOffice Spreadsheet
- Dynamic formulas for P&L tracking


**You:** create a trading jornnal
Formulas Below:  Trades Placed Profit =if(E8=0,"",(D8-C8)*E8)  Trades Placed W/L (*Note: youtube does not allow the greater than or less than sign in the description, so replace the word greater than in the formula below with the greater than sign.) =if(E8=0,"",IF(F8 greater than 0,"W","L"))  Days Traded Date: =unique(A8:A)  Days Traded Profit: =if(I8=0,"",SUMIF(A$8:A,I8,F$8:F))  Days of the Month values: =SUMIF($I$8:$I,date($N$7,$L8,O$7),$J$8:$J)  Win Amount Total: =sumif(G8:G500,"W",F8:F500)  Loss Amount Total: =sumif(G8:G500,"L",F8:F500)  Dashboard Wins: =COUNTIF(Recording!G8:G500,"W")  Dashboard Losses: =COUNTIF(Recording!G8:G500,"L")

https://www.youtube.com/watch?v=fv1h4p2lfvQ

**Claude:** Now I'll build the trading journal based on your formulas. Let me create a polished Excel file with a **Recording** sheet and **Dashboard** sheet.Let me fix the formula references to make them LibreOffice-compatible:Your trading journal is ready! Here's what's included:

**Recording Sheet**
- Columns A–H: Date, Day (auto), Ticker, Entry $, Exit $, Shares *(blue = your inputs)*, then auto-calculated **P&L $** and **W/L**
- Conditional formatting: green for wins, red for losses
- **Days Traded** section (cols J–K): unique dates + daily P&L totals
- **Monthly Calendar** (col M onward): P&L by day for all 12 months — enter the year in cell O5

**Dashboard Sheet**
- Total Wins/Losses, Win Rate, Net P&L, Profit Factor, Avg Win/Loss, Best/Worst Day, Largest Win/Loss

**One note for the Days Traded "Unique Dates" (cell J8):** add this formula manually in Excel after opening, as it requires Excel's dynamic array engine:
```
=UNIQUE(A8:A507)
```
All other formulas (2,391 total) are pre-built and error-free ✅