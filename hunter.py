import re

def banner():
    print("\033[92m")
    print(" Mahmoud Al-Daei [msd773] | Ibb - The Green City")
    print("")
    print(" --- YEMENI HUNTER IBB V7 ULTIMATE | CYBERSECURITY ---")
    print("")
    print(" Features: Virus + Fake Links + Foreign WA + Telegram Scams")
    print("\033[0m")

def check_url(url):
    score = 0
    reasons = []

    # 1. IP Address
    if re.search(r'\d+\.\d+\.\d+\.\d+', url):
        score += 3
        reasons.append("[!] IP Address Found - DANGER")

    # 2. @ trick
    if "@" in url:
        score += 3
        reasons.append("[!] @ Symbol Trick - PHISHING")

    # 3. Fake Domain
    if url.count(".") > 4 or "faceb00k" in url or "paypa1" in url:
        score += 2
        reasons.append("[!] Fake Domain - SUSPICIOUS")

    # 4. Short Link
    shorteners = ["bit.ly","tinyurl","t.me","wa.me","cutt.ly"]
    if any(s in url for s in shorteners):
        score += 1
        reasons.append("[!] Short Link - HIDDEN URL")

    # 5. Telegram / WA Scam
    if "telegram" in url.lower() and ("gift" in url or "prize" in url):
        score += 2
        reasons.append("[!] Telegram Gift Scam")

    if len(url) > 75:
        score += 1
        reasons.append("[!] Very Long URL")

    return score, reasons

banner()
while True:
    try:
        url = input("\n\033[92mHunter@Ibb-V7> \033[0m")
    except:
        break

    if url.lower() == "exit":
        break

    score, reasons = check_url(url)

    if score >= 3:
        print("\n \033[91m[RESULT: PHISHING CONFIRMED! DO NOT OPEN]\033[0m")
    elif score >= 1:
        print("\n \033[93m[RESULT: SUSPICIOUS - BE CAREFUL]\033[0m")
    else:
        print("\n \033[92m[RESULT: LOOKS SAFE]\033[0m")

    for r in reasons:
        print(f" - {r}")
