import requests
from pyfiglet import Figlet
from termcolor import colored

# -----------------------------
# 🔰 Banner Function
# -----------------------------
def show_banner():
    f = Figlet(font='slant')
    banner = f.renderText('Kunal Rajput')
    print(colored(banner, 'green'))

# -----------------------------
# 🛡 Security Headers to Check
# -----------------------------
REQUIRED_HEADERS = {
    "Content-Security-Policy": "default-src",
    "Strict-Transport-Security": "max-age",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": ["DENY", "SAMEORIGIN"],
    "X-XSS-Protection": "1",
    "Referrer-Policy": "",
    "Permissions-Policy": "",
    "Cross-Origin-Embedder-Policy": "require-corp",
    "Cross-Origin-Opener-Policy": "same-origin",
    "Cross-Origin-Resource-Policy": "",
}

# -----------------------------
# 🔍 Header Checking Function
# -----------------------------
def check_headers(url):
    result = {}
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\n🔍 Checking Security Headers for: {url}\n")

        for header, expected in REQUIRED_HEADERS.items():
            status = "❌ Missing"
            value = headers.get(header, None)

            if value:
                if expected:
                    if isinstance(expected, list):
                        if any(opt in value for opt in expected):
                            status = "✅ OK"
                        else:
                            status = "⚠️ Weak"
                    elif expected in value:
                        status = "✅ OK"
                    else:
                        status = "⚠️ Weak"
                else:
                    status = "✅ OK"
            result[header] = {
                "status": status,
                "value": value or "Not Found"
            }
            print(f"{status} → {header}: {value or 'Not Found'}")

    except Exception as e:
        print(f"\n❗ Error: {e}")
    return result

# -----------------------------
# ▶️ Main Program
# -----------------------------
if __name__ == "__main__":
    show_banner()
    target_url = input("🌐 Enter website URL (with https://): ").strip()
    check_headers(target_url)
