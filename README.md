# # 🔍 OpenAI Quick Search Hotkey

A lightweight Python tool that lets you instantly query OpenAI using a hotkey. Simply highlight some text, hit `Ctrl+1`, type your question, and the result is displayed in your terminal.

---

## 🛠 Features

- ⌨️ Trigger via `Ctrl+1` from anywhere
- 📋 Automatically grabs highlighted (copied) text
- 🧠 Returns a smart, helpful answer based on context
- 🪄 Lightweight, no tray icons or GUI clutter

---

## 🚀 How It Works

1. You highlight any text (e.g. from browser, PDF, document).
2. Press `Ctrl+1`.
3. A popup asks: _"How can I help?"_
4. It combines your question with the highlighted text.
5. Sends it to OpenAI via API.
6. The answer is printed neatly in your terminal.

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/cheryllwp/openai-hotkey-shortcut.git
cd openai-hotkey-shortcut
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Set up environment
