# 🐍 Python cheat sheet: everything you need today

## Show something on screen
```python
print("Hello!")
print(name, amount)
```

## Variables: a labelled box for a value
```python
name = "Ada"          # text (a "string") goes in quotes
amount = 100          # a whole number
rate = 1.15           # a decimal number
```

## f-strings: put variables inside text
```python
print(f"{name} has {amount} pounds")      # Ada has 100 pounds
print(f"{rate:.2f}")                      # 1.15   (:.2f = 2 decimal places)
```

## Dictionaries: pairs of key → value
```python
rates = {"EUR": 1.15, "USD": 1.25}
rates["EUR"]                              # 1.15

data = {"base": "GBP", "rates": {"EUR": 1.15}}
data["rates"]["EUR"]                      # 1.15  (a dictionary inside a dictionary)
```

## Functions: a reusable recipe
```python
def convert(amount, rate):     # def = define; amount and rate are the ingredients
    result = amount * rate     # the steps are indented (4 spaces)
    return result              # return hands back the result

convert(100, 1.2)              # calling it with real values → 120.0
```

## if: only when something is true
```python
if amount > 50:
    print("That's a lot!")
```

## for: repeat for every item
```python
for code, rate in rates.items():
    print(code, rate)
```

## Useful built-ins
```python
max(history, key=history.get)   # the key with the HIGHEST value
min(history, key=history.get)   # the key with the LOWEST value
float("250")                    # turn text into a number → 250.0
"gbp".upper()                   # → "GBP"
```

## Common errors
| You see | It usually means |
|---|---|
| `There's still a blank ( ___ ) to fill in` | Find the `___` in the current level and replace it |
| `NameError: name 'x' is not defined` | A typo in a variable name, or you used it before creating it |
| `KeyError: 'EUR'` | That key isn't in the dictionary: check the spelling and the quotes |
| `IndentationError` | The spaces at the start of a line don't line up: use 4 spaces |
| `SyntaxError` | A missing bracket `)`, quote `"` or colon `:` |
