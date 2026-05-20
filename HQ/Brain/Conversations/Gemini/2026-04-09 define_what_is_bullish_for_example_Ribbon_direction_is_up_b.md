---
title: "Gemini Conversation conversation_1775730739"
date: 2026-04-09
created: 2026-04-09T00:00:00Z
source: gemini
category: personal
tags: ["trading", "technical-analysis", "bias-criteria", "bullish", "bearish", "neutral", "market-alignment", "risk-rules", "ema", "rsi"]
people: []
projects: ["Market Alignment Framework", "Trading System Development"]
related: ["2026-04-09 what_is_scenario_1", "2026-04-13 what_are_the_5_scenarions", "2026-04-16 what_is_the_pre_entry_checklist"]
message_count: 6
uuid: conversation_1775730739
---


**You:** define what is bullish for example Ribbon direction is up (bullish colour)", "Price is above the 20 EMA on the 4H", "RSI is below 60 (room to run)"

**Gemini:** Based on the provided documents, "bullish" conditions are defined by price action and technical indicators that signal upward momentum or buy-side control. Following your examples, here are the definitions of bullish states according to the various trading systems in your files:**Market Control & Structure**

  - **Scenario 1 (Buy-Side Control):** Defined as when acceptance is established and held above a key decision zone. This indicates active buy-side participation where sell-side attempts to regain control have failed.
  - **Bullish Campaign:** Represented by a "1→2→3" structure where an impulse occurs as price breaks above the "Point 2" high.
  - **Higher Highs & Higher Lows:** A market consistently making higher highs and higher lows constitutes a market moving higher.
  - **3 Bar Swing:** A bullish bias is suggested if the third bar in a sequence makes a higher high than the previous two.

**Indicator-Based Bullish Signals**

  - **EMA Ribbon/Band Direction:**
      - In the **Pivot-Based EMA** system, a "Golden Cross" (10 EMA \> 21 EMA) signifies a long/bullish trend.
      - The **EMA Continuation** model identifies bullish trend health when the 10 EMA is above the 20 EMA and both are sloping upward with clear separation.
  - **Price Position Relative to Averages:**
      - **VWAP:** Price trading above the VWAP is a primary indicator of bullish/buy-side control.
      - **EMA:** Long entries are permitted only when price is within or above the 10–20 EMA band, with a preference for tests of the 20 EMA.
  - **RSI (Momentum):** In the **VWAP Bounce Pro** system, a long entry requires the RSI to be below 70, indicating it is not yet overbought and has "room to run".

**Candlestick & Execution Triggers**

  - **Triple A Bar:** A bullish confirmation candle where the close is greater than the open, it makes a higher high than the previous candle, and the close is above the pivot.
  - **Session Open Hook:** A bullish setup occurs when price wicks below the **Daily Open**, then a 15 min candle closes back above it with a strong body.
  - **Impulse/Displacement:** Strong, urgent upward expansion characterized by large green candle bodies with minimal overlap and visible gaps.

**You:** define the "bias\_criteria": { "bullish": \[ "Ribbon direction is up (bullish colour)", "Price is above the 20 EMA on the 4H", "RSI is below 60 (room to run)" \], "bearish": \[ "Ribbon direction is down (bearish colour)", "Price is below the 20 EMA on the 4H", "RSI is above 40 (room to drop)" \], "neutral": \[ "Ribbon is flat or mixed", "Price is chopping around the 20 EMA", "RSI is between 45 and 55"

**Gemini:** Based on the provided documents and the structure of your examples, here is the definition for the **bias\_criteria** within the framework:**bias\_criteria**

  - **Bullish (Buy-Side Control)**
      - **Ribbon Direction**: Up (bullish color). In the Pivot-Based EMA system, this is defined by a "Golden Cross" where the 10 EMA is greater than the 21 EMA.
      - **EMA Cascade**: Price is above the 20 EMA on the 4H. The framework's cascade logic requires trading in the direction of the 4H trend (UP).
      - **RSI (Momentum)**: RSI is below 60 (room to run). This aligns with the VWAP Bounce Pro rule requiring RSI to be below 70 to ensure the market is not overbought before a long entry.
  - **Bearish (Sell-Side Control)**
      - **Ribbon Direction**: Down (bearish color). This occurs when the 10 EMA is less than the 21 EMA (Dead Cross).
      - **EMA Cascade**: Price is below the 20 EMA on the 4H. If the 4H trend is DOWN, only short opportunities are considered.
      - **RSI (Momentum)**: RSI is above 40 (room to drop). This aligns with the requirement for RSI to be above 30 to ensure the market is not oversold before a short entry.
  - **Neutral (Negotiation / Scenario 3)**
      - **Ribbon Status**: Flat or mixed. Characterized by "braided" or flat EMAs, indicating a lack of directional trend health.
      - **Price Behavior**: Price is "chopping" or overlapping around the 20 EMA rather than expanding away from it.
      - **RSI (Momentum)**: RSI is between 45 and 55. This represents a mid-range state where no clear momentum edge exists.

**You:** and define the risk rules for example "risk\_rules": \[ "Only take trades where R:R is at least 1:2", "No trading in the first 15 minutes of the NY session open", "Maximum 2 open positions at once", "If I have 2 losing trades in a row, stop for the day"

**Gemini:** Based on the provided documents and the structure of your examples, here is the definition for **risk\_rules** within the framework:  
  
**risk\_rules**

  - **Risk-to-Reward (R:R) Ratio**
      - **Minimum 1:2 R:R**: This aligns with the "Extreme Reversal Trades" and the **Market Flip Checklist**, which requires reward to be asymmetric with at least a 2R potential.
      - **Predetermined Targets**: Professional consistency requires taking profits when the system dictates (e.g., VWAP or ±1 SD bands) rather than based on emotion.
  - **Session Open Timing**
      - **No trading in the first 15 min of NY Open**: The framework emphasizes waiting for the **15 min candle close** back through the Daily Open (5 PM NY time) before acting. This ensures session open behavior is confirmed rather than reacted to.
  - **Position Management**
      - **Maximum 2 open positions**: This aligns with the **Mean Reversion System** operating limits, which allow a maximum of two trades per session.
      - **No "Making a Day"**: Risk per trade is fixed (typically 0.25%–1%) and never increased to recover losses.
  - **Daily Stop Rules**
      - **Stop for the day after 2 losing trades**: This matches the **Trading Operating Guide**, which mandates that once a maximum daily loss (0.5%–1.0%) or maximum losing trades limit is hit, trading stops immediately with no strategy switching or discretionary overrides.
      - **Daily Profit Cap**: Trading also stops after hitting a 0.5%–1.0% profit cap to prevent overconfidence and degradation of execution quality.

## Links
- Related conversation: "what_is_scenario_1" (2026-04-09)
- Related conversation: "what_are_the_5_scenarions" (2026-04-13)