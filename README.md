# 💱 Mini Currency Converter: SkillStruct Workshop

Build a small Python app that uses **live exchange rates** from the internet. **No Python experience needed:** the code is mostly written, and you fill in the blanks.

Data comes from the [Frankfurter API](https://frankfurter.dev). It's free, needs no sign-up or API key, and its rates are published by the European Central Bank.

---

Only if you already have Python set up, or want to try it at home.

### 1. Install Python (3.10 or newer)

Check if you already have it. Open a terminal (Mac: **Terminal**, Windows: **Command Prompt** or **PowerShell**) and type:

```bash
python3 --version     # Mac / Linux
python --version      # Windows
```

If you see `Python 3.10` or higher, you're set. Otherwise, download it from [python.org/downloads](https://www.python.org/downloads/).

> **Windows:** during installation, tick **"Add Python to PATH"**.

### 2. Install VS Code (recommended)

1. Download from [code.visualstudio.com](https://code.visualstudio.com).
2. Open VS Code, go to the **Extensions** panel (the squares icon on the left), search for **Python**, and install the one by **Microsoft**.

### 3. Open the project

1. Unzip the workshop files. Go to **Code  → Download Zip**
2. In VS Code: **File → Open Folder** and choose the `student-pack` folder.
3. Open a terminal inside VS Code: **Terminal → New Terminal**.

### 4. Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your computer.

**Mac / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```

You should now see `(.venv)` at the start of the terminal line.

Then tell VS Code to use it: press `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`), choose **Python: Select Interpreter**, and pick the one that mentions `.venv`.

### 5. Install the required package

```bash
pip install -r requirements.txt
```

This installs `requests`, the library that talks to the API. Everything else the app uses is built into Python.

### 6. Run it

```bash
python starter.py
```

Or open `starter.py` and click the **▶** button at the top right of VS Code.

You should see:

```
💱 Mini Currency Converter
```

Nothing else happens yet. That's your job! 🙂

---

## How to work

The code is already mostly written. Your job is to **fill in the blanks**. A blank looks like this: `___` (three underscores).

New to Python? Run **`warmup.py`** first. It shows everything you need today in a few lines, including how functions work.

1. Open `starter.py`. At the top you'll see `LEVEL = 1`.
2. Find the blanks `___` in **Level 1**. We'll do this level together.
3. Replace each `___` with the right thing. The comment above it tells you what to put.
4. Run the file. When you see `🎉 Level 1 works!`, change `LEVEL = 1` to `LEVEL = 2` at the top, and carry on.

| Level | What you'll build | |
|---|---|---|
| 1 | Fetch live data from the API | Together |
| 2 | Convert money between two currencies | **Goal for everyone** |
| 3 | Show a table of several currencies | Bonus |
| 4 | Find the best and worst day to exchange this week | Bonus |
| ⭐ | Stretch goals: user input, error handling, a chart | Extra bonus |

**Finishing Level 2 is a success.** Levels 3 and 4 are there if you finish early.

Need a reminder of how Python works? Open **`CHEATSHEET.md`**. **Stuck? Put your hand up.** Getting stuck is a normal part of programming.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `There's still a blank ( ___ ) to fill in` | Search the file for `___` (Cmd/Ctrl+F) in the level you're on, and replace it. |
| My new level doesn't run | Check you changed `LEVEL` at the top of `starter.py`, and saved the file. |
| `ModuleNotFoundError: No module named 'requests'` | Run `pip install -r requirements.txt`, and check that `(.venv)` shows in your terminal and VS Code is using the `.venv` interpreter (step 4). |
| `python: command not found` | Try `python3` instead (Mac/Linux), or reinstall Python and tick "Add Python to PATH" (Windows). |
| Windows says running scripts is disabled when activating | In PowerShell, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, then try again. Or use Command Prompt instead. |
| The internet isn't working, or the API isn't responding | Open `starter.py` and change `USE_OFFLINE = False` to `USE_OFFLINE = True`. The app will use saved sample rates from `backup_rates.json`. |
| A currency like NGN doesn't work | This API only covers the ~30 currencies published by the European Central Bank. See the full list at https://api.frankfurter.dev/v1/currencies |

---

## Try the API in your browser

Paste this into your browser to see exactly what your code will receive:

```
https://api.frankfurter.dev/v1/latest?base=GBP&symbols=EUR,USD
```
