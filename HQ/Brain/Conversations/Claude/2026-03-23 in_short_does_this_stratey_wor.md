---
title: "Smash Day Strategy Analysis"
date: 2026-03-23
created: 2026-03-23T12:20:01.553268Z
updated: 2026-03-23T12:22:13.653343Z
source: claude
category: trading
tags: ["trading", "strategy", "smash-day", "larry-williams", "eurusd", "backtest"]
people: []
projects: ["Trading Strategy Development"]
related:
  - "2026-03-20 Fibonacci_Strategy"
  - "2026-03-20 Key_indicators_for_profitable_EURUSD_and_AUDUSD_trading"
  - "2026-03-23 Williams_Percent_R_indicator_lesson"
  - "2026-03-25 Calculating_equivalent_trades_on_funded_account"
message_count: 4
uuid: f8f1d98d-5ea3-4d18-bb26-45744b97c333
---

## Links
- [[2026-03-20 Fibonacci_Strategy]] — Technical analysis foundations
- [[2026-03-20 Key_indicators_for_profitable_EURUSD_and_AUDUSD_trading]] — Indicator framework for EUR/USD
- [[2026-03-23 Williams_Percent_R_indicator_lesson]] — Larry Williams %R educational content
- [[2026-03-25 Calculating_equivalent_trades_on_funded_account]] — Position scaling and account management


**You:** in short
does this stratey work and if so what is the best scenario to trade? https://drive.google.com/driv
https://roguequant.substack.com/p/i-backtested-larry-williams-trading

**Claude:** Let me grab the Substack article and check your Drive link.Regarding your Google Drive link — it's incomplete (cuts off at "/driv"), so I couldn't access it. If you can reshare the full link I'll take a look.

Here's the short version on the Substack article about Larry Williams' **Smash Day** strategy:

**Does it work?** Sort of — but not universally. The author backtested it across 15 markets from 2014–2024, and the results were very mixed. The raw pattern with a short lookback period was mostly unprofitable. With an 8-period lookback (requiring the close to break the lowest low of the last 8 days), results improved significantly across almost all assets — which makes intuitive sense: the more extended the trend, the more meaningful the reversal signal.

**Best scenarios to trade it:**

- **S&P 500 longs** — the standout result. It showed an 80% win rate with a 6.94 profit factor on the long side. Other indices (Dow, Nikkei, Russell) were also strong for longs but weak for shorts.
- **Euro (both directions)** — the best currency overall, and it remained robust even when exit rules were changed, which is a good sign of real edge.
- **Silver with 8-period lookback** — no negative years over the test period, though the author cautions this was the best-fit parameter.

**What didn't work:** Wheat was disappointing despite Larry recommending it. Gold only worked on the long side. Adding stop-loss exits made results worse for most assets.

**Key takeaway:** There's a real idea here — failed breakouts do reverse — but it's not a plug-and-play system. It needs the right asset, the right direction (longs for indices, shorts for some currencies), a longer lookback, and proper risk management. The author himself flags potential overfitting concerns and suggests walk-forward testing before trading it live.

As always, this isn't financial advice — just a breakdown of what the article found. Worth doing your own testing before committing capital.

**You:** should i use it on eurusd?

**Claude:** Based on what the article found, EUR/USD is actually one of the strongest candidates — but with some nuances worth knowing.

**What the backtest showed for Euro:**

The Euro was the best currency by far among all those tested. Unlike most other assets where the strategy only worked in one direction, the Euro showed good results in both long and short positions, though it was even better on the short side. It also passed an important robustness check: when exit rules were changed (like adding stops), the Euro continued to perform well, while most other assets got worse. That's a meaningful signal — strategies that survive different exit methods tend to have more genuine edge.

**What to keep in mind before trading it:**

- The backtest covered 2014–2024. That's decent but not enormous, and market regimes change.
- The 8-period lookback was used as default across assets — it wasn't independently optimized for Euro, which is actually a *good* thing (less overfitting risk).
- The author recommends walk-forward analysis to confirm validity before going live.
- You'd still need to define your position sizing and risk management, which the backtest doesn't fully address.

So the data is encouraging for EUR/USD relative to the other markets tested. But I'd echo the article's advice: do your own out-of-sample testing before putting real money behind it, and treat it as one component of a broader system rather than a standalone strategy.

I'm not a financial advisor, so take this as an analysis of the article's findings rather than a trading recommendation.