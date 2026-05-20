---
title: "Accessing local file path"
date: 2026-03-26
created: 2026-03-26T04:32:36.304700Z
updated: 2026-04-02T06:56:56.299400Z
source: claude
category: finance
tags: ["payslips", "capgemini", "local-access", "onedrive", "spreadsheet"]
people: ["Mathew Lister"]
projects: ["Capgemini Termination"]
related: []
message_count: 34
uuid: 91bd3b10-5719-40f4-97ea-b258bb982844
---


## Links

- [[2026-03-26 Adelaide_contractor_salary_equivalence]] — Adelaide salary equivalence calculations
- [[2026-03-27 Things_To_Review_Do_2026]] — Main action plan tracker

---

**You:** can you access this link? "C:\Users\mathe\OneDrive\CapGemini\Pay Slip_Lister Mathew_20260304"

**Claude:** I can't access files on your local computer — the path `C:\Users\mathe\OneDrive\...` is on your own machine and isn't reachable from here.

However, you've already uploaded two payslips for the same pay period (01/03/26 – 31/03/26), and I can see both of them. The first appears to be a preliminary or partial version (with $0.00 across most line items), while the second is the full/final payslip showing the detailed breakdown including normal pay, annual leave adjustments, ETP redundancy payments, lump sum amounts, and a total net pay of **$40,430.86**.

If there's a different payslip or document you'd like me to look at, just upload it here and I'll be happy to help. Is there something specific you'd like to do with these payslips?

**You:** can you access folders on onedrive?

**Claude:** No, I don't have direct access to OneDrive. I can only work with files you upload directly into this chat.

That said, let me check if there's a connector available that might help.Unfortunately, there's no OneDrive connector available at the moment. The only Microsoft integration listed is for Microsoft Learn documentation, which isn't what you need.

Your best options are to either upload the files directly into this chat (drag and drop, or use the attachment button), or if the files are also in Google Drive, I do have access to search your Google Drive. Would either of those work for you?

**You:** ill add them 10 at a time

can you update the attached spreadsheet?

**Claude:** Let me read the skill file and examine your existing spreadsheet first.Now let me look at the remaining PDFs that aren't already visible in my context, to check for any that aren't already in the spreadsheet.Good — only the two March 2026 payslips are new. All others are already in the spreadsheet. Let me now update it with those two records and adjust the FY2026 summaries.Everything looks correct. Let me copy it to the output folder.Here's the updated spreadsheet. All the PDFs you uploaded except the two **March 2026 payslips** were already in the spreadsheet, so I've added those two new records. Here's what changed:

**All Pay Slips** — added 2 new rows (now 63 records): the super-only slip (`13032026.pdf`) and the full termination payslip (`13032026_1.pdf`).

**FY Summary** — updated FY2026 across all sections: YTD figures now reflect March 2026 (Taxable Gross $93,484.68, Tax $25,194, Net $109,508.16), super employer increased to $15,589.41, ESOP to $1,918.89 (3 months), and AL balance updated to -1.61 hrs.

**Super Detail** — added March 2026 SGC entry ($1,781.76) and updated all FY2026 totals.

**Leave Detail** — added March 2026 entry and updated FY2026 year-end AL balance to -1.61 hrs.

**ESOP Detail** — added March 2026 deduction ($639.63) and updated FY2026 total to $1,918.89.

**Notes** — added termination details: ETP Redundancy ($3,828.37), Lump Sum D ($39,308.00 total), and final net pay ($40,430.86).

You mentioned you'd add files 10 at a time — if you have more payslips to upload, I'm ready.

**You:** how much have I paid in ESOP? and how much PAL is onpaid?

**Claude:** These 10 payslips are all already in the spreadsheet, so no updates needed there. To answer your questions:

**ESOP Total Paid: $6,715.08**

That breaks down as $2,595.00 in FY2024 (3 months × $865), $2,201.19 in FY2025 (3 months × $733.73), and $1,918.89 in FY2026 (3 months × $639.63).

**PAL (Purchased Annual Leave) — Unpaid Balance: $13,317.29**

Here's the reconciliation:

Total deductions taken from your pay: $4,483.68 (FY2023) + $14,286.71 (FY2024) + $9,999.18 (FY2025) + $3,318.12 (FY2026) = **$32,087.69**

Total payouts received back: $8,967.60 (Jan 2024) + $9,802.80 (Dec 2024) = **$18,770.40**

So **$13,317.29** has been deducted but not yet paid back to you. Given the March 2026 payslip appears to be your final/termination payslip, this outstanding PAL balance should be owed to you — it's worth checking with payroll whether it's included in the Lump Sum D payment ($39,308.00) or if it's being processed separately.

**You:** what is listing in the final payslip for the items?

**Claude:** Here's the full breakdown from the final payslip (13032026_1.pdf):

**Before Tax Earnings:**
- Normal pay: 39.39 hrs × $82.95 = $3,267.58
- Other Leave No Pay: 60.40 hrs × $0.00 = $0.00
- Annual Leave: -60.40 hrs × $82.95 = -$5,010.46 (reversal, dated 06/03/2026)
- **Sub Total: -$1,742.88**

**Before Tax Deductions:**
- PAL: $0.00
- Super SS: $0.00
- **Sub Total: $0.00**

**Taxable Gross Earnings: -$1,742.88**

**Specials:**
- ETP Redun With Super: $3,828.37

**Tax Deductions:**
- TAX: $902.00
- ETP Tax: -$1,225.00 (refund)
- **Total Tax Deducted: -$323.00** (net refund)

**After Tax Earnings:**
- Lump Sum D: $26,545.47
- Lump Sum D with Super: $12,762.53
- **Sub Total: $39,308.00**

**After Tax Deductions:**
- ESOP Deduction: -$639.63

**Total Net Pay: $40,430.86**

So regarding your PAL question — the $13,317.29 in unpaid PAL deductions doesn't appear as a separate line item here. It's likely rolled into the **Lump Sum D ($39,308.00)** which typically covers unused leave entitlements and other termination payouts under Australian tax law. You might want to confirm with payroll exactly what that Lump Sum D comprises, as it could include your outstanding PAL balance, any remaining leave loading, and redundancy-related amounts.

**You:** i should have been paid for 5 weeks plus 8 weeks

does this marry up?

**Claude:** Let me work through that. Your weekly rate based on the $172,542.34 salary is **$3,318.12/week** ($172,542.34 ÷ 52).

**Expected payout: 13 weeks × $3,318.12 = $43,135.56**

**Actual termination payments on the final payslip:**

| Component | Amount |
|---|---|
| ETP Redun With Super | $3,828.37 |
| Lump Sum D with Super | $12,762.53 |
| Lump Sum D | $26,545.47 |
| **Total** | **$43,136.37** |

The difference is **$0.81** — that's just rounding. So yes, the 5 + 8 = 13 weeks **does marry up** against the termination lump sums.

The breakdown likely splits as roughly 8 weeks redundancy ($26,545.47 as Lump Sum D — the tax-free genuine redundancy component) and 5 weeks notice ($16,590.90 split across the ETP and Lump Sum D with Super as taxable components).

That said, this means the **$13,317.29 in unpaid PAL deductions isn't visibly included** in these line items — it's separate from the 13 weeks. It might be worth raising with payroll whether that's been refunded or is still owing to you.

**You:** i should have been paid for 5 weeks plus 8 weeks
does this marry up? did i get paid this?

what else makes up the final pay slip?

**Claude:** Let me break down every component of the final payslip and map it against what you're owed.

**Your weekly rate: $172,542.34 ÷ 52 = $3,318.12/week**

**13 weeks (5 notice + 8 redundancy) = $43,135.56**

The three termination lump sums add up to almost exactly that:

| Item | Amount |
|---|---|
| ETP Redun With Super | $3,828.37 |
| Lump Sum D with Super | $12,762.53 |
| Lump Sum D | $26,545.47 |
| **Total** | **$43,136.37** |

So yes, your **13 weeks was paid** (off by $0.81 rounding).

**The rest of the payslip:**

| Item | Amount | What it is |
|---|---|---|
| Normal pay (39.39 hrs) | +$3,267.58 | ~5 days worked in March before termination |
| Annual Leave reversal (-60.40 hrs) | -$5,010.46 | Clawback of leave previously taken (you were overdrawn) |
| Other Leave No Pay (60.40 hrs) | $0.00 | Replaces those AL hours with unpaid leave |
| Tax (net) | +$323.00 | $1,225 ETP tax refund minus $902 normal tax |
| ESOP deduction | -$639.63 | Final month's share plan deduction |
| **Net Pay** | **$40,430.86** | |

**What's NOT on this payslip: your $13,317.29 in unpaid PAL**

You've had $32,087.69 deducted from your pay for purchased annual leave, but only received $18,770.40 back in PAL payouts. That's $13,317.29 still owing. It doesn't appear as a line item anywhere on this final payslip.

I'd recommend raising this with payroll — those PAL deductions are your money that was withheld from salary, and it should be refunded on termination if the purchased leave wasn't taken.

**You:** please can you deouble check

for all the years I have bought PAL
How many days have I bought and how many have I used; and how many are out standing?

**Claude:** Let me trace through the PAL carefully, cycle by cycle, using the actual deductions and payouts from your payslips.Here's the full PAL reconciliation across three purchase cycles:

**Cycle 1 — Calendar Year 2023 (3 weeks purchased)**
- Deductions: 12 months × $747.28/month = $8,967.36
- Payout received Jan 2024: $8,967.60 (120 hrs = 15 days)
- **Settled** ✓

**Cycle 2 — Jan–Jun 2024 (3 weeks purchased)**
- Deductions: $754.08 + 5 × $1,809.80 = $9,803.08
- Payout received Dec 2024: $9,802.80 (120 hrs = 15 days)
- **Settled** ✓

**Cycle 3 — Jan–Jun 2025 + Jan–Feb 2026 (4 weeks purchased)**
- Jan–Jun 2025: 6 × $1,666.53 = $9,999.18 (= 3 weeks at $3,333/week)
- Jan–Feb 2026: 2 × $1,659.06 = $3,318.12 (= 1 week at $3,318/week)
- Payout: **$0.00**
- **OUTSTANDING: $13,317.30**

**Grand total:**

| | Weeks | Days | $ |
|---|---|---|---|
| Total bought | 10 | 50 | $32,087.74 |
| Paid out (cycles 1 & 2) | 6 | 30 | $18,770.40 |
| **Outstanding (cycle 3)** | **4** | **20** | **$13,317.30** |

None of the purchased leave was "used" as actual leave days — all completed cycles were cashed out as payouts rather than taken.

**The $13,317.30 for 4 weeks (20 days) does not appear anywhere on your final payslip.** It's not in the Lump Sum D, the ETP, or any other line item. This is money that was deducted from your salary and should be refunded on termination. I'd raise this with payroll as a priority.

**You:** can you see this?
Employee Stock Ownership Plan

**Claude:** I can't see any new document or image attached — it looks like you may have forgotten to upload it. Could you try attaching the ESOP document again? I'd be happy to review it alongside the $6,715.08 in ESOP deductions from your payslips.

**You:** create full json

**Claude:** Here's the full JSON with all 63 payslip records. It includes your employee details, full salary history, FY summaries, termination breakdown, the PAL reconciliation (including the $13,317.30 outstanding), ESOP totals ($6,715.08), super history, leave balances, and every individual payslip record.

**You:** review again

Everything is here, can you access folder?

"G:\My Drive\CapGemini\Capgemini Payslips"

**Claude:** I can't access local file paths like `G:\My Drive\...`, but I do have access to search your Google Drive. Let me look for that folder.Found the folder! It was just created a minute ago. Let me look inside it for the payslip files.I can see two subfolders in there. Let me look inside each one.I found the folder and can see it contains two subfolders:

- **Pay Slip_Lister Mathew_130326** (modified today)
- **Pay Slip_Lister Mathew_20260304** (modified 22 days ago — March 4)

Unfortunately, my Google Drive access can only read **Google Docs** — it can't open PDFs or other binary files stored in Drive. So I can see the folder structure but can't read the actual payslip PDFs inside them.

The **20260304** folder is interesting though — that's a payslip date we don't have in the spreadsheet. Was there a payslip issued on 4 March 2026? That could potentially contain the PAL payout or other information we're looking for.

The easiest way to get me those files is still to upload them directly into this chat. If you could upload whatever's in the **Pay Slip_Lister Mathew_20260304** folder, I can check if it's a new record we're missing.

**You:** create full json

**Claude:** Here's the full JSON (91 KB). It covers everything:

- **63 payslip records** with all line-item data
- **56 monthly super records** — grand total $194,544.39
- **56 monthly leave records** — 87 days AL taken across all years
- **9 ESOP monthly records** — grand total $6,715.08
- **3 PAL purchase cycles** — $13,317.34 outstanding (4 weeks / 20 days unpaid)
- **Full termination breakdown** — both March 2026 payslips line by line
- **13-week redundancy reconciliation** — confirmed paid ($43,136.37 vs $43,135.56 expected)
- **Salary history** — 7 rate changes from $150k to $172,542
- **FY summaries** — FY2022 through FY2026
- **Amounts potentially owing** — the PAL shortfall flagged

**You:** this is the response I got from Capgemini

Please review and advise? Do I need to go back to them?

Hi Matthew,
 
Thank you for your email.
 
In regards to your Purchase Leave used and refunds, for the agreement in 2025, you had agreed to Purchase 15 days of Leave. During the 2025 Calendar year, you took 10 days of Purchase Leave off. The screenshots from Replicon confirm you took Purchase Leave off from the 6th – 8th May, along with August 6th – 14th August 2025.
 

 

 
Your total Purchase Leave 2025 agreement cost was for $9,999.18 for the 15 days. You elected to repay this in 6 monthly deductions of $1,666.53 . Your 2025 Purchase Leave agreement was fully repaid by you in the June 2025 payrun. However in the 2025 calendar year, you only took 10 days off for Purchase leave with the other 5 days as unused.
 
Your remaining unused 5 day of Purchase Leave (40hours) was paid out to you as a refund of $3,333.06 before tax in your January 2026 payrun. It is shown on your below January payslip as PAL Payment $3,333.06.

 
In regard to your 2026 Purchase Leave taken and deducted, you initially agreed to purchase 15 days of Purchase Leave. This was for a total cost of $9954.30 and you elected to have 6 monthly deductions processed for $1659.06 per month.
 
In the month of January 2026, you used 5 days of Purchase Leave from the 5th January to the 9th January 2026 off work. You applied for these days as Purchase Leave and they were approved by Vi Tran.


Your Purchase Leave taken off work was recorded in your February 2026 payrun, as the Purchase Leave was approved after the January 2026 payrun was completed.

 
 
As you finished working with Capgemini back in March 2026, you had only taken 5 days off for Purchase Leave and you had not fully been repaid. Your 2026 Purchase Leave agreement was adjusted for you to only use 5 days, for a cost of $3318.15.
 
You had 2 Purchase Leave deductions for $1659.06 to repay for your adjustment agreement of $3318.15. The 2 deductions were taken in the January and February 2026 payruns. As a result, you have repaid for your 5 days taken in full and were not due to receive any additional refund upon your departure from Capgemini.
 
 
In regard to your ESOP balance we have on record and agree that you had $6715.08 deducted over 3 years (2023, 2024, 2025 ESOP scheme).
 
In order to exit the ESOP program and receive a possible refund you will need to complete the exit process. You should have received an email about this already. If not you will later receive it today.
 
If you have any further questions regarding ESOP please email the ESOP team at __esopteam@capgemini.com__.
 
 
We believe we have provided you with all of the information you requested. However if you disagree with anything please advise us what your concern is.
 
 
Kind regards,
Payroll Team

**Claude:** This is really important information. Let me carefully check Capgemini's claims against the payslip evidence you've just shared.

**Image 3 is key — the January 2026 payslip has more detail than what was in the spreadsheet.** It shows a **PU PAL Payment of $3,333.06** that I didn't have captured. This changes the PAL picture significantly.

Let me verify their numbers:

**2025 PAL Agreement (Cycle 3):**
- 15 days purchased at $9,999.18 (6 × $1,666.53) ✓ — matches payslips
- Per-day cost: $9,999.18 ÷ 15 = $666.61/day
- 10 days taken as actual leave (May 6-8 = 3 days, Aug 6-14 = 7 days) ✓ — confirmed by Images 1 & 2
- 5 unused days expired Dec 31, 2025 ✓ — Image 1 shows "Initial Balance Expiry" reducing balance from 5 to 0
- Refund for 5 unused days: 5 × $666.61 = $3,333.06 ✓ — visible on Jan 2026 payslip (Image 3)
- **SETTLED** ✓

**2026 PAL Agreement (Cycle 4):**
- Originally 15 days at $9,954.30 ($1,659.05 × 6 per month)
- 5 days taken Jan 5-9, 2026 ✓ — confirmed by Images 4 & 5
- Recorded in Feb 2026 payslip as Normal/PAL hour swaps ✓ — Image 6
- Agreement adjusted to 5 days: 5 × $663.62 = $3,318.10 ≈ $3,318.12
- 2 deductions of $1,659.06 taken (Jan + Feb 2026) = $3,318.12
- Deductions match adjusted 5-day cost ✓
- **SETTLED** ✓

**My earlier analysis was wrong.** I was treating PAL deductions as pure "savings" that should all be refunded. In reality, PAL pays for actual leave days taken — you only get refunds for days you didn't use. The $3,333.06 payout in January 2026 was on the payslip but wasn't captured in the spreadsheet data I was working from.

**Revised PAL summary:**

| Cycle | Days Bought | Days Taken | Days Refunded | Deducted | Refunded | Status |
|---|---|---|---|---|---|---|
| 2023 | 15 | 0 | 15 | $8,967.36 | $8,967.60 | Settled |
| 2024 | 15 | 0 | 15 | $9,803.08 | $9,802.80 | Settled |
| 2025 | 15 | 10 | 5 | $9,999.18 | $3,333.06 | Settled |
| 2026 | 5 (adjusted) | 5 | 0 | $3,318.12 | $0 | Settled |

**Capgemini's explanation checks out. You don't need to go back to them on PAL.**

**For the ESOP ($6,715.08):** They've confirmed the amount and said you need to complete the exit process to receive a possible refund. If you haven't received the ESOP exit email yet, I'd follow up with **esopteam@capgemini.com** — that's where the money is.

Want me to update the JSON and spreadsheet with the corrected PAL data?

**You:** yes please

**Claude:** Both files updated. Here's what changed:

**PAL — corrected across all 4 cycles:**

| Cycle | Bought | Taken | Refunded | Deducted | Refunded $ | Status |
|---|---|---|---|---|---|---|
| 2023 | 15 days | 0 | 15 | $8,967 | $8,968 | Settled |
| 2024 | 15 days | 0 | 15 | $9,803 | $9,803 | Settled |
| 2025 | 15 days | 10 | 5 | $9,999 | $3,333 | Settled |
| 2026 | 5 days (adj) | 5 | 0 | $3,318 | $0 | Settled |
| **Total** | **50 days** | **15** | **35** | **$32,088** | **$22,103** | **All settled** |

**Key corrections:** Jan 2026 payslip now includes the $3,333.06 PAL payout (refund for 5 unused 2025 days). Added full detail from the Jan and Feb 2026 payslips including the Normal/PAL hour swaps. Notes updated to reflect Capgemini's confirmation.

**Only outstanding item now: ESOP $6,715.08** — you need to complete the exit process via esopteam@capgemini.com to get that back.

**You:** so what is outstadning?

Subject: FORMAL NOTICE: Claim for Outstanding Wages and Unauthorised Deductions 
– Employee ID: 002459
To: Capgemini Australia Payroll / Human Resources
Date: March 26, 2026
Reference: Redundancy Termination Date March 13, 2026
To Whom It May Concern,
Following my redundancy on March 13, 2026, I have conducted a forensic audit of my 
63 payslip records and year-to-date summaries. While the 13-week redundancy payout 
is reconciled, there are significant outstanding wages and after-tax deductions that 
remain unpaid and unreconciled.
1. THE PRIMARY CLAIM: Purchased Annual Leave (PAL) - $13,317.30
A total of 20 days (152 hours) of PAL was deducted from my gross salary across 2025 
and 2026 but was never credited to my leave balance or refunded upon termination.
Audit of Deductions (Cycle 3):
• FY2025 (Jan–Jun 2025): 6 monthly deductions of $1,666.53 = $9,999.18 (3 weeks 
equivalent).
• FY2026 (Jan–Feb 2026): 2 monthly deductions of $1,659.06 = $3,318.12 (1 week 
equivalent).
• Total Salary Sacrificed: $13,317.30
Evidence of Non-Usage:
My leave records confirm that 0 days of PAL were utilized. All leave taken in 2025/26 was 
coded as Standard Annual Leave, leading to a balance deficit. Consequently, 
Capgemini "clawed back" $5,010.46 from my final termination pay (Ref: 
Mathew_Lister_13032026_1.pdf) to settle that deficit.
By failing to apply the PAL I had already purchased, Capgemini has effectively charged 
me twice for the same leave: once through monthly salary deductions and a second 
time through the termination "Annual Leave Reversal."
2. SECONDARY CLAIM: ESOP Contributions - $6,715.08
My records show $6,715.08 in after-tax deductions for the Employee Share Ownership 
Plan (ESOP). This includes a final deduction of $639.63 taken from my termination pay 
on March 13, 2026.
I note that this final deduction was made without my specific written authorisation for 
this final pay period, which may constitute an unauthorised deduction under Section 
324 of the Fair Work Act 2009.
I require a formal statement confirming either:
• The immediate refund of these post-tax contributions; or
• Proof of share allocation and the mechanism for transfer/sale following my 
redundancy.
3. SUMMARY OF OUTSTANDING AMOUNTS
Item Amount Status
Purchased Annual Leave (PAL) $13,317.30 Outstanding Wages
ESOP Contributions $6,715.08 Unreconciled After-Tax Funds
TOTAL REMITTANCE REQUIRED $20,032.38
4. RESOLUTION & LEGAL NOTICE
These funds represent wages already earned and sacrificed by me. Failure to remit 
these amounts constitutes a breach of the Fair Work Act 2009.
I require these funds to be processed within 7 days. Please provide a corrected Pay 
Advice and confirmation of associated Superannuation Guarantee (SGC) adjustments 
for the PAL component.
I have retained all 63 payslip records and am prepared to provide this data to Fair Work 
Australia and, if necessary, escalate this as a liquidated debt claim in the Small Claims 
Court.
Sincerely,
Mathew Lister Employee ID: 002459

what is outstanding?

**Claude:** **Please do not send this letter.** The PAL claim of $13,317.30 is no longer valid based on what we just verified together. Sending it would undermine your credibility on the ESOP claim, which *is* legitimate.

Here's the current position:

**PAL — $0 outstanding (SETTLED)**

We confirmed this an hour ago when you shared Capgemini's response and the Replicon screenshots. The breakdown was:

- 2025: You *did* take 10 days of PAL (May 6-8, Aug 6-14) — the Replicon screenshots prove it. The remaining 5 unused days were refunded $3,333.06 in your Jan 2026 payslip.
- 2026: Agreement adjusted to 5 days taken Jan 5-9. Two deductions of $1,659.06 cover the cost exactly.

The letter claims "0 days of PAL were utilized" — that's incorrect. The system records show 15 days were taken across 2025 and 2026, all approved.

**ESOP — $6,715.08 (PENDING, but not in the way the letter claims)**

This money *is* yours, but Capgemini told you there's an exit process to complete. It's not necessarily an "unauthorised deduction" — you would have signed up for the scheme. The right approach is to contact esopteam@capgemini.com, complete the exit process, and then escalate if they don't pay out.

**The only action item right now is completing the ESOP exit process.** Would you like me to help draft a more appropriate email to the ESOP team requesting that?

**You:** how much in aus did i put in to ESOP per year?

**Claude:** Here's the ESOP breakdown by calendar year (all after-tax deductions):

| Year | Months | Monthly | Annual Total |
|---|---|---|---|
| 2024 | Jan – Mar (3 months) | $865.00 | $2,595.00 |
| 2025 | Jan – Mar (3 months) | $733.73 | $2,201.19 |
| 2026 | Jan – Mar (3 months) | $639.63 | $1,918.89 |
| **Total** | **9 months** | | **$6,715.08** |

These are all after-tax, so $6,715.08 is the actual cash out of your pocket. The monthly amount decreased each year, which is a bit unusual — worth asking the ESOP team why the contribution rate dropped when your salary was going up.

**You:** add in an extra column to put in the EUR amount

**Claude:** Based on historical AUD/EUR rates for each contribution period:

| Year | Months | Monthly (AUD) | Total (AUD) | Approx AUD/EUR Rate | Total (EUR) |
|---|---|---|---|---|---|
| 2024 | Jan – Mar | $865.00 | $2,595.00 | ~0.61 | ~€1,583 |
| 2025 | Jan – Mar | $733.73 | $2,201.19 | ~0.585 | ~€1,288 |
| 2026 | Jan – Mar | $639.63 | $1,918.89 | ~0.60 | ~€1,151 |
| **Total** | **9 months** | | **$6,715.08** | | **~€4,022** |

The EUR rates are approximate mid-quarter averages — the actual rate Capgemini used for the share purchase may differ. The ESOP team should be able to tell you the exact EUR amounts and how many shares were allocated each year, since Capgemini shares trade on Euronext Paris in EUR.

That's worth asking when you do the exit process — specifically how many shares you hold and at what price they were purchased, as they may be worth more or less than the €4,022 you put in depending on the Capgemini share price movement.