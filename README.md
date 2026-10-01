# Yemeni Hunter V5 - Ibb Edition 💚
By Mahmoud Al-Daei | Ibb - The Green City, Yemen
SOC Level 1 Phishing & OSINT Detector

## Proof of Work (Real Test from Termux)
- PHISHING: http://faceb00k-login-security.com
  => SUSPICIOUS 6/10
  => Detected: Typo-squatting (0 instead of o) + login-secure-verify + No HTTPS

- SAFE: https://www.google.com
  => SAFE 0/10
  => IP: 216.239.38.120
  => VirusTotal: https://www.virustotal.com/gui/domain/www.google.com

## Features
- Typo-squatting detection
- Suspicious keywords
- Dashes / @ / IP / HTTPS checks
- Domain to IP resolver
- Auto VirusTotal link
- Logging to hunter_reports.txt

## Usage
python hunter.py

## Author
Mahmoud Al-Daei - Ibb - 2026
The Green City Hunter
