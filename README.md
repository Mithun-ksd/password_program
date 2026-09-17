# 🔐 Password Tool — Generator & Strength Tester
 
A simple desktop GUI application built with **Python** and **Tkinter** that lets you:
 
1. **Generate** strong, random passwords with customizable options (length, uppercase, lowercase, numbers, symbols).
2. **Check the strength** of any password you type in.
No internet connection or external servers involved — everything runs locally on your machine.
 
---
 
## 📸 Preview
 
![Password Tool Preview]
 
<img width="501" height="787" alt="pas1" src="https://github.com/user-attachments/assets/da861031-920e-46d6-a8ff-04279063c58d" />
<img width="497" height="782" alt="pas2" src="https://github.com/user-attachments/assets/34507e76-1695-4048-b608-1b7866fbdf46" />


## ✨ Features
 
### Password Generator
- Choose the password **length**.
- Toggle character sets on/off:
  - Lowercase letters (`a-z`)
  - Uppercase letters (`A-Z`)
  - Numbers (`0-9`)
  - Symbols (`!@#$%^&*...`)
- **Generate** a random password from the selected character sets.
- **Copy** the generated password to your clipboard with one click.
- **Clear** the result field.
### Password Strength Tester
- Type or paste any password into the field.
- Click **Check** to see if it's rated **Weak**, **Medium**, or **Strong**.
- Strength is scored based on:
  - Length (8+ characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of numbers
  - Presence of symbols
- **Clear** the field and reset the result.
---
 
## 🛠 Requirements
 
- **Python 3.7+**
### Modules used
 
| Module | Type | Purpose |
|---|---|---|
| `tkinter` | Built-in (standard library) | GUI window, labels, buttons, checkboxes |
| `random` | Built-in (standard library) | Randomly selecting characters for passwords |
| `string` | Built-in (standard library) | Predefined character sets (letters, digits, punctuation) |
| `pyperclip` | External (must be installed) | Copying the generated password to the clipboard |
 
> `tkinter`, `random`, and `string` come bundled with standard Python installations — no separate install needed. The **only** package you need to install manually is `pyperclip`.
 
**Note on Tkinter (Linux users):** most Windows/macOS Python installs include Tkinter by default. On some Linux distributions, you may need to install it separately:
```bash
# Debian/Ubuntu
sudo apt-get install python3-tk
 
# Fedora
sudo dnf install python3-tkinter
```
 
---
 
## 📦 Installation
 
### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/password_program.git
cd password_program
```
 
### 2. Install the required package
```bash
pip install pyperclip
```
 
## ▶️ How to Run
 
```bash
python password_generator.py
```
 
This will open a desktop window titled **"Password Tool"** with two sections: the Generator on top and the Strength Tester below it.
 
---
 
## ⚙️ How It Works
 
### `generate()`
Reads the desired length from the input box, then builds a pool of characters based on which checkboxes (lowercase, uppercase, numbers, symbols) are ticked. It uses `random.choices()` to pick characters from that pool and joins them into a password string, which is then displayed in the result label. If no checkboxes are selected, it warns you to select an option instead of generating an empty password.
 
### `check_strength()`
Reads the password typed into the strength-tester field and awards one point for each of the following conditions it meets: length ≥ 8, contains a lowercase letter, contains an uppercase letter, contains a digit, contains a symbol. Based on the total score, it labels the password **Weak** (red), **Medium** (orange), or **Strong** (green).
 
### `copy_to_clipboard()`
Grabs the currently displayed password from the result label and copies it to your system clipboard using `pyperclip`, so you can paste it directly wherever you need it.
 
### `clear_generator()` / `clear_password()`
Reset the respective result label and input field back to empty.
 
---
 
## 📁 Project Structure
 
```
├── password_generator.py   # Main application script
├── README.md                # Project documentation (this file)
└── .gitignore                # Files/folders excluded from Git tracking
```
 
---
 
## ⚠️ Known Limitations
 
- Password generation uses `random.choices()` (Python's standard PRNG), which is **not cryptographically secure**. For generating passwords intended for real, sensitive account security, consider using the [`secrets`](https://docs.python.org/3/library/secrets.html) module instead, which is designed for cryptographic use.
- The GUI is built with Tkinter, so it opens as a native desktop window and won't run in a web browser.
---
 
## 🤝 Contributing
 
Feel free to fork this repository, open issues, or submit pull requests if you'd like to add features (e.g., password history, exportable strength reports, dark mode, or switching to the `secrets` module for generation).
 
---
 
