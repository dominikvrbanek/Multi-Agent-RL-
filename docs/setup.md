# Setup Guide

Requirements: **Git** and **Conda (Miniconda)**, or Python 3.10/3.11 if you prefer venv.
Nothing here needs a GPU.

## Option A: Conda (default)

**Windows:** open *Anaconda Prompt* (Start menu). **macOS/Linux:** any terminal.

```bash
git clone <REPO-URL>
cd uais-marl-soccer
conda env create -f environment.yml
conda activate marl
python scripts/smoke_test.py
```

The first environment solve can take a minute or two. The `torch` download is large, so use decent wifi.

## Option B: venv (no conda)

**Windows (PowerShell):**
```powershell
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # only if activation is blocked
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Then, on any OS:
```bash
python -m pip install --upgrade pip
pip install mpe2 pettingzoo gymnasium "stable-baselines3[extra]" supersuit torch wandb pytest
pip install -e .
python scripts/smoke_test.py
```

## Verify

```bash
python scripts/smoke_test.py            # headless check
python scripts/smoke_test.py --render   # opens a window; you should see agents moving
python scripts/random_baseline.py       # prints the random-action reward baseline
pytest                                  # runs the tests
```

## Notes

- The Phase 1 environment is **`simple_tag_v3`** (predator-prey) from the **`mpe2`** package. Import from `mpe2`, not `pettingzoo.mpe`, which is deprecated.
- In VS Code, select the interpreter (Ctrl+Shift+P, "Python: Select Interpreter", `marl`).
- If `conda` isn't recognized in PowerShell, run `conda init powershell` once in Anaconda Prompt and restart the terminal.
- Still stuck on Windows? WSL2 gives you a Linux environment and sidesteps most issues.
- Use one approach (conda **or** venv), not both.
