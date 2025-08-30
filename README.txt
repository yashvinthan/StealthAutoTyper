# ⌨️ StealthAutoTyper — Human-like Typing Bot (No Repeats)

StealthAutoTyper is a Windows automation script that simulates **extremely human-like typing behavior** using the low-level **SendInput API**.  

Unlike simple auto-typers, this project introduces:
- Random typing delays
- Occasional typos with backspace corrections
- CPU-aware pacing
- “Thinking” pauses between sentences
- A **no-repeats guard** to prevent accidental multiple runs  

This makes the typing appear natural and indistinguishable from a real user.

⚠️ **Disclaimer:** For demos, testing, and educational use only. Do not use in password fields, login forms, or against software policies.
⚠️ Use responsibly. Don’t target password fields, logins, or any software that forbids automation.

---

## ✨ Features
- **Human cadence**: random delays, pauses, natural rhythm
- **Mistakes like a human**: typos + backspaces
- **CPU throttling**: slows when your system is under load
- **Thinking pauses**: simulates a human stopping to think
- **No repeats**: prevents duplicate typing sessions
- **Zero dependencies**: pure Python + ctypes

---

## 🚀 Usage

### Run from source
1. Make sure Python (3.10+ recommended) is installed.  
2. Clone this repo and run:
   ```bash
   python StealthAutoTyper.py
