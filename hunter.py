#!/usr/bin/env python3
# Yemeni Hunter V5 - Ibb Edition
# By Mahmoud Al-Daei - Ibb, Yemen - The Green City
# SOC Level Phishing & OSINT Tool

import re, socket
import requests
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.GREEN + """
__   __                         _   _   _             _            
\\ \\ / /__ _ __ ___   ___ _ __ (_)_| | | |_   _ _ __ | |_ ___ _ __ 
 \\ V / _ \\ '_ ` _ \\ / _ \\ '_ \\| | | | | | | | '_ \\| __/ _ \\ '__|
  | |  __/ | | | | |_| | | |_| | | | | ||  __/ |   
  |_|\\___|_| |_| |_|\\___|_| |_|_|\\__,_|  \\__,_|_| |_|\\__\\___|_|   
    V5 - Ibb Edition | By Mahmoud Al-Daei | Ibb - The Green City 💚
    """ + Style.RESET_ALL)

def check_phishing(url):
    score = 0
    reasons = []
    
    # 1. faceb00k trick
    if re.search(r'faceb[0o]{2}k|g00gle|amaz0n', url, re.I):
        score += 3
        reasons.append("[!] Typo-squatting: 0 instead of o")
    # 2. suspicious keywords
    if re.search(r'login.*secur|secur.*login|verify.*account', url, re.I):
        score += 2
        reasons.append("[!] Suspicious keywords: login-secure-verify")
    # 3. many dashes
    if url.count('-') >= 3:
        score += 2
        reasons.append(f"[!] Many dashes: {url.count('-')}")
    # 4. @ symbol
    if '@' in url:
        score += 2
        reasons.append("[!] @ symbol redirect trick")
    # 5. IP direct
    if re.match(r'https?://\d+\.\d+\.\d+\.\d+', url):
        score += 3
        reasons.append("[!] Direct IP link (no domain)")
    # 6. No https
    if not url.startswith('https://'):
        score += 1
        reasons.append("[!] No HTTPS")
        
    return score, reasons

def main():
    banner()
    while True:
        url = input(Fore.CYAN + "\nHunter@Ibb-V5> " + Style.RESET_ALL).strip()
        if url.lower() in ['exit','quit','q']: break
        if not url: continue
        if not url.startswith('http'): url = 'http://' + url
        
        print(f"\n[*] Scanning: {url}")
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            ip = socket.gethostbyname(domain) if domain else "N/A"
            print(f"[*] Domain: {domain}")
            print(f"[*] IP: {ip}")
            print(f"[*] VirusTotal: https://www.virustotal.com/gui/domain/{domain}")
        except Exception as e:
            print(f"[!] Error resolving: {e}")
            domain = url
            
        score, reasons = check_phishing(url)
        print(f"\n{'='*50}")
        if score >= 7:
            print(Fore.RED + f"[!!!] CRITICAL Phishing {score}/10 - DO NOT CLICK!" + Style.RESET_ALL)
        elif score >= 4:
            print(Fore.YELLOW + f"[!] SUSPICIOUS {score}/10 - Be Careful" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"[+] SAFE {score}/10" + Style.RESET_ALL)
            
        for r in reasons:
            print(Fore.YELLOW + "  " + r)
        print(f"{'='*50}")
        
        # Log
        with open("hunter_reports.txt","a") as f:
            f.write(f"{url} | Score: {score}/10 | Reasons: {'; '.join(reasons)}\n")

if __name__ == "__main__":
    main()
