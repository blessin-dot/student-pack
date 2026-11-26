"""
🐍 Python warm-up: SkillStruct workshop
========================================

Everything you need for today, in one file. Run it to see each example
print its result, then try the two small exercises at the bottom.
"""

# 1. print() shows something on the screen
print("Hello, SkillStruct!")


# 2. A variable is a labelled box that stores a value
name = "Ada"
amount = 100
print(name, amount)


# 3. An f-string puts variables inside text (note the f before the quotes)
print(f"{name} wants to convert {amount} pounds")


# 4. A dictionary stores pairs of key → value
rates = {"EUR": 1.15, "USD": 1.25}
print(rates["EUR"])          # look up the value for the key "EUR" → 1.15


# 5. A dictionary can hold another dictionary.
#    This is exactly the shape of what the API sends back today!
data = {"base": "GBP", "rates": {"EUR": 1.15, "USD": 1.25}}
print(data["rates"]["USD"])  # first "rates", then "USD" → 1.25


# 6. A FUNCTION is a reusable recipe.
#
#    def convert(amount, rate):      ← "def" starts the recipe; it needs 2 ingredients
#        result = amount * rate      ← the steps (indented with 4 spaces)
#        return result               ← the finished dish it hands back
#
def convert(amount, rate):
    result = amount * rate
    return result

# Writing the recipe doesn't run it. You run it by CALLING it with real values:
print(convert(100, 1.2))     # → 120.0
print(convert(50, 1.25))     # same recipe, different ingredients → 62.5


# 7. A function can use another function
def describe(amount, rate, currency):
    converted = convert(amount, rate)
    return f"{amount} GBP = {converted:.2f} {currency}"

print(describe(100, 1.15, "EUR"))   # → 100 GBP = 115.00 EUR


# 8. if: do something only when a condition is true
if convert(100, 1.15) > 110:
    print("Good rate!")


# 9. for: repeat something for every item
for currency, rate in rates.items():
    print(f"1 GBP = {rate} {currency}")


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# A. Write a function called double that takes a number and returns it times 2.
#    Test it by adding:   print(double(21))      → should show 42
#
# B. Write a function called greet that takes a name and returns "Hello, <name>!"
#    Test it by adding:   print(greet("Ada"))    → should show Hello, Ada!
