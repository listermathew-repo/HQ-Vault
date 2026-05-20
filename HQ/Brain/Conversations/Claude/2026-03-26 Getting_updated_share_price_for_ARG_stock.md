---
title: "Getting updated share price for ARG stock"
date: 2026-03-26
created: 2026-03-26T01:14:00.888640Z
updated: 2026-03-26T01:15:51.329147Z
source: claude
category: finance
tags: ["stock-price", "arg", "asx", "excel-stocks-datatype", "googlefinance"]
people: ["Mathew Lister"]
projects: ["Portfolio Management"]
related: []
message_count: 6
uuid: 12d9dce5-c116-4a0b-b1bc-f789261741b7
---

## Links

- [[2026-03-26 Excel_formula_for_market_value_calculation]] — Market value calculation formulas
- [[2026-03-26 Making_a_spreadsheet_look_beautiful]] — Portfolio formatting and analysis

---

**You:** in cell d8 i have ARG
Argo Investments LtdARG
I want the updated share price in g8

**Claude:** Let me check if you've uploaded a spreadsheet file.The most recent share price I can find for **Argo Investments (ASX: ARG)** is **$8.75 AUD** as of 20/03/2026. That's from last Friday — today's closing price may differ slightly, so you might want to double-check on the ASX website or your broker for today's exact figure.

Go ahead and enter **8.75** in cell G8 as a starting point. Just note that I can't provide live real-time prices, so this could be a few days behind.

**You:** in cell d8 i have ARG
Argo Investments LtdARG
I want the updated share price in f8 and the number of shares in e8 and in g8 i want the total shares x share price

give me the formula

**Claude:** It depends on whether you're using **Google Sheets** or **Excel**, since they handle live stock prices differently.

**Google Sheets** (easiest for live prices):

Since ARG is on the ASX, for **F8** (share price):

```
=GOOGLEFINANCE("ASX:"&D8, "price")
```

For **G8** (total value):

```
=E8*F8
```

E8 (number of shares) you'd enter manually.

**Excel 365** doesn't have a simple formula equivalent. You'd need to either use the *Stocks data type* (select the ticker cell → Data tab → Stocks) or pull prices via Power Query. There's no one-liner formula like Google Sheets offers.

If you're in Excel and want a self-updating formula-based approach, switching that sheet to Google Sheets is the path of least resistance. Want me to help set up either option further?

**You:** excel

**Claude:** In Excel 365, there's no `GOOGLEFINANCE` equivalent formula. Instead you use the **Stocks data type**:

**Step 1 — Convert D8 to a Stock:**
Select D8 → go to **Data** tab → click **Stocks**. Excel should recognize "ARG" and convert it (it may show as "Argo Investments Ltd" with a small stocks icon).

If it doesn't auto-detect as ASX, click the cell, then the small icon that appears, and select the correct match (ASX listing).

**Step 2 — Formulas:**

**F8** (share price):
```
=D8.Price
```

**E8** — enter your number of shares manually.

**G8** (total value):
```
=E8*F8
```

One thing to note: the Stocks data type price isn't real-time — it updates periodically (typically 15–20 min delay) and only refreshes when the workbook is open. You can force a refresh via **Data → Refresh All**.