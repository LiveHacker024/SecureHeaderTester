# 🔐 Security Header Testing Tool – Part of SecureHeaderTester 🛡️

A lightweight and modular security header scanner designed for penetration testers, security researchers, and developers. This tool checks for the presence, correctness, and strength of critical HTTP security headers that protect against common web attacks like **XSS**, **Clickjacking**, **CORS abuse**, and more.

---

## 🚀 Features

- ✅ Scans for 15+ essential security headers
- ❌ Detects missing or weakly configured headers
- 🧩 Easy to integrate into your own CLI or FastAPI-based tools
- 📦 Clean, structured output (Text / JSON / Ready for PDF)
- 🐍 Python 3 compatible – no external dependencies except `requests`

---

---

If requirements.txt is not available, manually install:

pip3 install requests

🖥️ Usage (CLI)

python3 header_checker.py

Enter a target URL when prompted:

🌐 Enter website URL (with https://): https://example.com

✔️ Output Example:

✅ Content-Security-Policy found ➜ default-src 'self'
❌ Permissions-Policy NOT found
⚠️  X-Frame-Options found but value may be weak ➜ ALLOW-FROM

🧩 Integration (Python Module)

from header_checker import check_headers

results = check_headers("https://example.com")
for header, data in results.items():
    print(f"{header}: {data['status']} ➜ {data['value']}")

📋 Headers Tested

    Content-Security-Policy

    Strict-Transport-Security

    X-Content-Type-Options

    X-Frame-Options

    X-XSS-Protection

    Referrer-Policy

    Permissions-Policy

    Cross-Origin-Embedder-Policy

    Cross-Origin-Opener-Policy

    Cross-Origin-Resource-Policy

    Set-Cookie (flags check)

    Access-Control-Allow-Origin

    Cache-Control

...and more.
📄 License

MIT License
👨‍💻 Author

Developed by [Your Name or Handle]
🔗 [LinkedIn or Twitter if you'd like]
🌐 https://yourportfolio.dev


---

### ✅ What You Should Do Next:
- Place the above markdown in your `README.md`
- Make sure `header_checker.py` exists in your repo
- Optional: Add a sample `requirements.txt` with just:

requests

## 🔧 Installation

```bash
git clone https://github.com/yourusername/SecureHeaderTester.git
cd SecureHeaderTester
pip3 install -r requirements.txt

