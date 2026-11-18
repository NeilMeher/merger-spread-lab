# Source register and coverage

Sources accessed 2026-11-18. The limited case table contains six factual published USD-per-share closes and three derived daily index returns. Third-party reports and raw feeds remain with their publishers. Bulk redistribution rights were not established. Stooq's three pilot endpoints returned browser-verification HTML, and the tested FRED CSV returned a recent window instead of the requested dates. The brief's dated-observation fallback supplies the three pairs.

| Case | Usable dates (ET) | Milestone source | Price evidence | Benchmark evidence |
|---|---|---|---|---|
| ATVI | July 10 and 11, 2023 | [FTC docket order](https://www.ftc.gov/system/files/ftc_gov/pdf/608644.2023.09.25_d09412_-_order_returning_matter_to_adjudication.pdf), decision dated July 10, public July 11 intraday | [Dated $82.70 and $90.99 closes](https://gameworldobserver.com/2023/07/12/activision-blizzard-shares-two-year-high-up-10-percent) and [July 11 market report](https://www.latimes.com/entertainment-arts/business/story/2023-07-11/microsoft-wins-u-s-court-nod-to-buy-activision-in-loss-for-ftc) | [July 12 CAPIS market note](https://capis.com/capis-morning-note-07-12-23-market-awaits-cpi-expectations-are-for-a-low-number/) |
| IRBT | November 24 and 27, 2023 | [European Commission press release](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_23_5990/IP_23_5990_EN.pdf) | [Dated $42.30 and $34.35 closes](https://miru.com/analysis/shutterstock-s-q2-loss-and-guidance-suspension-deepen-uncertainty) | [Danamon November 28 recap](https://www.danamon.co.id/Personal/Investasi/Market-Insight/-/media/ALL-CONTENT-PERSONAL-BANKING/DAILY-MARKET-RECAP/2023/November/Daily-Market-Insight-28-November-2023.pdf) |
| SAVE | January 12 and 16, 2024 | [Justice Department case record](https://www.justice.gov/atr/case/us-and-plaintiff-states-v-jetblue-airways-corporation-and-spirit-airlines-inc), [Spirit 8-K](https://www.sec.gov/Archives/edgar/data/1498710/000149871024000045/save-20240116.htm) | [Dated $14.97 and $7.92 closes](https://members.porterandcompanyresearch.com/wp-content/uploads/2024/02/PCDI_02_19_2024.pdf) and [contemporary $7.92 closing report](https://qz.com/spirit-airlines-stock-jet-blue-merger-blocked-1851170021) | [AP Jan. 12](https://apnews.com/article/c2ce7c3436de985375954fb5a904fb53) and [Jan. 16](https://apnews.com/article/4c58578dbdec033d90e169126d4ecb84) |

The CSV dates are regular-session closing dates, with the exception of the Nov. 24, 2023 early close at 13:00 ET. January 15, 2024 was a US market holiday. Milestone timing precision is limited to the public-date session. Where only a period is supported, an exact minute is left unspecified. The rows use contemporaneous unadjusted closes, with no splits or paid special cash within the measured windows found in the reviewed terms. Event dates and closing terms use primary agency and SEC records. Prices are isolated published observations rather than licensed exchange histories.

## Point-in-time terms ledger

| Case | Date | Terms or regulatory event | Price coverage |
|---|---|---|---|
| ATVI | 2022-01-18 | $95 cash agreement | Outside pilot prices |
| ATVI | 2023-07-10/11 | U.S. order dated July 10 and denial reported intraday July 11 ET | Prior and affected closes |
| ATVI | 2023-07-18 | Later letter agreement permits 2023 dividend; outside valuation date | Outside pilot prices |
| ATVI | 2023-10-13 | SEC closing filing confirms $95 cash | Close paid; no event-window series |
| IRBT | 2023-07-24 | Amended from $61 to $51.75 | Outside pilot prices |
| IRBT | 2023-11-27 | EU objections announced by US close | Prior and affected closes |
| IRBT | 2024-01-28/29 | Effective termination January 28, publicly announced January 29 before open | No completed close-to-close audit used |
| SAVE | 2022-10-26 | $2.50 approval prepayment | Outside pilot prices |
| SAVE | 2023-01 to 2023-12 | $0.10 monthly prepayments to holders of record | Outside pilot prices |
| SAVE | 2024-01-16 | Injunction by US close | Prior and affected closes |
| SAVE | 2024-03-01/04 | Termination effective March 1, announced March 4 | No completed close-to-close audit used |

[Activision closing 8-K](https://www.sec.gov/Archives/edgar/data/718877/000110465923108985/tm2328253d1_8k.htm) · [iRobot amendment and terms](https://www.sec.gov/Archives/edgar/data/1159167/000119312523192865/d502452ddefa14a.htm) · [Spirit prepayments](https://www.sec.gov/Archives/edgar/data/1498710/000149871024000117/save-20231231.htm) · [Spirit termination](https://www.sec.gov/Archives/edgar/data/1498710/000149871024000124/a240304pressreleasefinal.htm)

Fields ending in close and offer are USD per share. market_return is a decimal price-index return. Break-price entries are assumptions in USD per share. Grid rows record calendar-day close horizons, PVs of each scenario, implied weights as decimals and a separate feasibility flag.
