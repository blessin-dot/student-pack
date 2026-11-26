"""
💱 Mini Currency Converter: SkillStruct workshop
=================================================

Today you'll finish a Python app that uses LIVE exchange rates from the
internet. Most of the code is written for you: your job is to fill in the
blanks marked  ___

HOW TO WORK
  1. Start with LEVEL = 1 (just below this box).
  2. Find the blanks  ___  in that level and fill them in.
  3. Run the file. Did it work? Change LEVEL to 2 and carry on.

  Levels 1 and 2 are the goal. Levels 3 and 4 are bonus levels.
  Stuck? Put your hand up. Getting stuck is a normal part of programming!

New to Python? Run warmup.py first, and keep CHEATSHEET.md open.

Internet not working? Change USE_OFFLINE to True below. The app will use
saved sample rates instead.
"""

LEVEL = 1            # 👈 Change this to 2, 3 or 4 when you finish each level

USE_OFFLINE = False  # 👈 Change to True if the internet isn't working


import json
from datetime import date, timedelta
from pathlib import Path

import requests

BASE_URL = "https://api.frankfurter.dev/v1"
BACKUP_FILE = Path(__file__).parent / "backup_rates.json"


# ===========================================================================
# LEVEL 1: Get live data from the internet   (we'll do this one together)
# ===========================================================================

def get_data(endpoint, params):
    """Ask the API for data and give it back as a Python dictionary."""
    if USE_OFFLINE:
        return load_backup(endpoint, params)

    # The full web address, e.g. https://api.frankfurter.dev/v1/latest
    url = BASE_URL + "/" + endpoint

    # Send the request to the API.
    # BLANK: which variable holds the web address we just built?
    response = requests.get(___, params=params, timeout=10)

    # Turn the API's reply into a Python dictionary.
    # BLANK: the name of the format the API replies in (4 letters, lowercase).
    return response.___()


# ===========================================================================
# LEVEL 2: Convert money
# ===========================================================================

def get_rate(base, target):
    """How much 1 unit of `base` is worth in `target`.
    Example: get_rate("GBP", "EUR") gives something like 1.15"""
    data = get_data("latest", {"base": base, "symbols": target})

    # `data` looks like this:
    #   {"amount": 1.0, "base": "GBP", "date": "2026-11-20", "rates": {"EUR": 1.15}}
    #
    # BLANKS: pick the rate out of the dictionary inside the dictionary.
    # Hint: first the key "rates", then the target currency.
    rate = data[___][___]
    return rate


def convert(amount, base, target):
    """Convert `amount` from `base` to `target`.
    Example: convert(100, "GBP", "EUR") gives something like 115.0"""
    rate = get_rate(base, target)

    # BLANK: how do you turn an amount and a rate into the converted amount?
    return ___


# ===========================================================================
# LEVEL 3 (bonus): Show a table of currencies
# ===========================================================================

def show_table(amount, base, targets):
    """Print what `amount` of `base` is worth in each currency in `targets`."""
    data = get_data("latest", {"base": base, "symbols": ",".join(targets)})
    print(f"\n{amount} {base} is worth:")

    # A for loop repeats the indented lines once for each item.
    # Here each item is a pair: a currency code and its rate, e.g. "EUR", 1.15
    for code, rate in data["rates"].items():
        # BLANK: how much is `amount` worth in this currency?
        value = ___
        print(f"  {code}: {value:.2f}")


# ===========================================================================
# LEVEL 4 (bonus): Find the best day to exchange
# ===========================================================================

def get_history(base, target, days=7):
    """Return {date: rate} for the last `days` days.
    (This one is done for you.)"""
    start = (date.today() - timedelta(days=days)).isoformat()
    data = get_data(f"{start}..", {"base": base, "symbols": target})
    return {day: rates[target] for day, rates in data["rates"].items()}


def best_day(base, target):
    """Print each day's rate, then the best and worst day to exchange."""
    history = get_history(base, target)    # e.g. {"2026-11-18": 1.15, ...}

    for day, rate in history.items():
        print(f"  {day}: {rate}")

    # The best day has the HIGHEST rate, because you get more money.
    # max(..., key=history.get) finds the date with the highest rate.
    best = max(history, key=history.get)

    # BLANK: which function finds the LOWEST? (the opposite of max)
    worst = ___(history, key=history.get)

    print(f"\n  Best day:  {best} ({history[best]})")
    print(f"  Worst day: {worst} ({history[worst]})")

    # Notice anything missing from the dates? Why might that be? 🤔


# ===========================================================================
# STRETCH GOALS (finished everything? try one!)
# ===========================================================================
#  ⭐ Let the user choose: ask which currencies to use with input(),
#     instead of always GBP to EUR. (input() gives you text: use .upper())
#  ⭐ Handle mistakes: what happens if someone types "XYZ"? Make the app
#     print a friendly message instead of crashing (look up try/except).
#  ⭐ Text chart: in best_day, print a bar of "█" for each day, longer when
#     the rate is higher.


# ---------------------------------------------------------------------------
# You don't need to change anything below this line.
# It runs each level up to the LEVEL you set at the top.
# ---------------------------------------------------------------------------

def load_backup(endpoint, params):
    """Saved sample data, in the same shape as the real API (done for you)."""
    with open(BACKUP_FILE, encoding="utf-8") as file:
        backup = json.load(file)
    if endpoint == "currencies":
        return backup["currencies"]

    base = params.get("base", "EUR").upper()
    symbols = params.get("symbols")

    def rebase(eur_rates):
        rates = {"EUR": 1.0, **eur_rates}
        if base not in rates:
            raise ValueError(f"{base} isn't in the backup data.")
        wanted = symbols.upper().split(",") if symbols else [c for c in rates if c != base]
        result = {}
        for code in wanted:
            if code not in rates:
                raise ValueError(f"{code} isn't in the backup data.")
            result[code] = round(rates[code] / rates[base], 5)
        return result

    if endpoint == "latest":
        return {"amount": 1.0, "base": base, "date": backup["latest"]["date"],
                "rates": rebase(backup["latest"]["rates"])}
    history = {day: rebase(rates) for day, rates in backup["history"].items()}
    days = sorted(history)
    return {"amount": 1.0, "base": base, "start_date": days[0], "end_date": days[-1], "rates": history}


def main():
    print("💱 Mini Currency Converter")

    if LEVEL >= 1:
        print("\n--- Level 1: live data from the API ---")
        data = get_data("latest", {"base": "GBP", "symbols": "EUR"})
        print(data)

    if LEVEL >= 2:
        print("\n--- Level 2: convert money ---")
        amount = float(input("How many GBP do you want to convert? "))
        result = convert(amount, "GBP", "EUR")
        print(f"{amount:.2f} GBP = {result:.2f} EUR")

    if LEVEL >= 3:
        print("\n--- Level 3 (bonus): a table of currencies ---")
        show_table(100, "GBP", ["EUR", "USD", "JPY", "CHF", "CAD"])

    if LEVEL >= 4:
        print("\n--- Level 4 (bonus): best day to exchange ---")
        best_day("GBP", "EUR")

    print("\n🎉 Level", LEVEL, "works! Change LEVEL at the top to try the next one.")


if __name__ == "__main__":
    try:
        main()
    except (NameError, AttributeError) as error:
        if "___" in str(error):
            print("\n✋ There's still a blank ( ___ ) to fill in for this level.")
            print("   Look for ___ in the code, replace it, and run again.")
        else:
            raise
    except requests.RequestException:
        print("\n📡 Couldn't reach the internet. Set USE_OFFLINE = True at the top and run again.")
