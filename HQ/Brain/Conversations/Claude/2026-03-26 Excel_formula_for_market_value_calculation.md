---
title: "Excel formula for market value calculation"
date: 2026-03-26
created: 2026-03-26T03:31:37.056850Z
updated: 2026-03-26T03:31:58.128727Z
source: claude
category: finance
tags: ["excel", "formula", "portfolio", "asx", "arg", "stock-data-type"]
people: ["Mathew Lister"]
projects: ["Portfolio Management"]
related: []
message_count: 2
uuid: ea5e4588-b44a-4223-836c-2ca8353cbf0b
---


## Links

- [[2026-03-26 Getting_updated_share_price_for_ARG_stock]] — Stock price formulas and data types
- [[2026-03-26 Making_a_spreadsheet_look_beautiful]] — Portfolio spreadsheet formatting

---

**You:** need the excel formula for excel
InvestmentASX TickerUnits HeldPrice ($)Market Value ($)AllocationArgo Investments LtdARG20,600#REF!#REF!#REF!

**Claude:** The `#REF!` errors are cascading — once the **Price** formula breaks, **Market Value** and **Allocation** break too since they depend on it.

Here are the formulas you likely need (assuming row 2 is your first data row):

**Price ($)** — This depends on how you're sourcing prices. The `#REF!` usually means a cell reference is pointing somewhere that no longer exists (e.g., a deleted sheet or column). If you were pulling from another sheet, you'll need to re-link it. If you're entering prices manually, just type the value directly.

If you're on Microsoft 365, you can use the **Stocks data type**: type the ticker in a cell, select it, go to **Data → Stocks**, then pull the price with:

`=B2.[Price]`

**Market Value ($)** — assuming Price is in column D and Units Held is in column C:

`=C2*D2`

**Allocation (%)** — assuming Market Value is in column E:

`=E2/SUM(E:E)`

Format that cell as a percentage. This gives each holding's weight relative to the total portfolio.

So for your ARG row with 20,600 units, once the price is populated (say $11.50), Market Value would calculate as $236,900, and Allocation would show its share of your total portfolio.

Would you like me to look at the actual spreadsheet file if you have one to upload? That way I can pinpoint exactly which reference is broken.