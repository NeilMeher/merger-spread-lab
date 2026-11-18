import argparse
import csv
from datetime import date, time
from pathlib import Path

from figure import Plot

ROOT = Path(__file__).resolve().parent


def effective_close(event_day, event_time, sessions):
    for day, close in sorted(sessions.items()):
        if day > event_day or (day == event_day and event_time < close):
            return day
    raise ValueError("Supply the next trading session")


def remaining_cash(headline, approval, monthly_count):
    return headline - approval - min(1.15, .10 * monthly_count)


def payoff(amount, days, first_payment=None, rate=.05):
    def pv(cash, elapsed):
        return cash / (1 + rate) ** (elapsed / 365)
    payments = (sum(pv(.10, day) for day in range(first_payment, days+1, 30))
                if first_payment is not None else 0)
    return pv(amount, days) + payments


def implied(price, completion, broken):
    if completion <= broken:
        return None, False
    weight = (price-broken)/(completion-broken)
    return weight, 0 <= weight <= 1


def scenario_rows(deal):
    remaining = remaining_cash(float(deal["headline_offer"]), float(deal["prepaid_approval"]),
                               int(deal["prepaid_months"]))
    for phase in ("prior", "event"):
        session = date.fromisoformat(deal["prev_session" if phase == "prior" else "effective_session"])
        first = (date(2024, 1, 31) - session).days if deal["symbol"] == "SAVE" else None
        for days in (30, 90, 180):
            completion = payoff(remaining, days, first)
            for level in ("low", "mid", "high"):
                recovery = float(deal[f"break_{level}"])
                broken = payoff(recovery, 30, first)
                weight, feasible = implied(float(deal[f"{phase}_close"]), completion, broken)
                yield dict(symbol=deal["symbol"], session=session.isoformat(), phase=phase, days_to_close=days,
                           break_price=recovery, pv_completion=round(completion, 6), pv_break=round(broken, 6),
                           raw_weight=round(weight, 8) if weight is not None else None, feasible=feasible)


def render(deal, rows, output, synthetic):
    symbol = deal["symbol"]
    title = f"{symbol} · {deal['milestone']}"
    detail = "Synthetic fixture" if synthetic else f"{deal['case']} · {deal['event_date']}"
    prior, event = [float(deal[f"{phase}_close"]) for phase in ("prior","event")]
    offer = remaining_cash(float(deal["headline_offer"]), float(deal["prepaid_approval"]),
                           int(deal["prepaid_months"]))
    timeline = Plot(title, detail, (0, 3), (0, max(prior, event, offer)*1.12),
                    "Closing observations around public milestone", "USD per share",
                    x_ticks=[(.45, deal["prev_session"]), (2.55, deal["effective_session"])])
    x, _ = timeline.point(2.15, 0)
    timeline.parts.append(f'<path d="M{x} 90V355" stroke="#77644d" stroke-dasharray="4 4"/>')
    timeline.series([(.45, prior), (2.55, event)], "#166c77", "Reported closes")
    timeline.series([(0,offer), (3,offer)], "#973e30", "Remaining cash at close", dots=False)
    timeline.save(output/f"{symbol}-timeline.svg")

    boundaries = [float(deal[f"break_{key}"]) for key in ("low", "high")]
    sensitivity = Plot(f"{symbol} · completion-weight sensitivity", detail + " · affected session",
                       tuple(boundaries), (0,100), "Break price (USD per share)", "Feasible weight (%)")
    for days, color in ((30,"#166c77"), (90,"#973e30"), (180,"#6a4e83")):
        values = [(r["break_price"], r["raw_weight"]*100) for r in rows
                  if r["phase"] == "event" and r["days_to_close"] == days and r["feasible"]]
        sensitivity.series(values, color, f"{days} days to close")
    sensitivity.save(output/f"{symbol}-sensitivity.svg")


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--input", type=Path, default=ROOT/"events.csv")
    arg.add_argument("--output", type=Path, default=ROOT/"report")
    arg.add_argument("--fixture", action="store_true")
    args = arg.parse_args()
    path = ROOT/"fixture.csv" if args.fixture else args.input
    with path.open(newline="", encoding="utf-8") as file:
        deals = list(csv.DictReader(file))
    args.output.mkdir(parents=True, exist_ok=True)
    grid = []
    for deal in deals:
        rows = list(scenario_rows(deal))
        grid.extend(rows)
        render(deal, rows, args.output, args.fixture)
        raw = float(deal["event_close"]) / float(deal["prior_close"]) - 1
        benchmark = float(deal["market_return"])
        print(f"{deal['symbol']}: raw {raw:+.2%}, market-adjusted {raw - benchmark:+.2%}")
        for phase in ("prior", "event"):
            weights = [r["raw_weight"] for r in rows if r["phase"] == phase and r["feasible"]]
            band = f"{min(weights):.1%} to {max(weights):.1%}" if weights else "no feasible cells"
            print(f"  {phase}: {band} ({len(weights)}/9 feasible)")
    with (args.output/"weights.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=grid[0])
        writer.writeheader()
        writer.writerows(grid)


if __name__ == "__main__":
    main()
