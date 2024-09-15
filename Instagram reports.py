import requests
import string
import random
from colorama import Fore, Style
from requests.sessions import Session

# Copyright Information
# ====================================================
# This script is developed by se.cj.
# All rights reserved. Unauthorized use or distribution
# of this code is prohibited. For any inquiries, please
# contact se.cj directly.
# ====================================================

def random_str(length):
    """
    Generate a random string of specified length.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def get_user_agent():
    """
    Retrieve a random user-agent string from a predefined list.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    user_agents = [
        # Add a larger list of User-Agents here
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

def report_profile_attack(username, num_reports=1, proxies=None):
    """
    Report a profile multiple times to a given URL.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    if proxies:
        proxy = random.choice(proxies)
        ses = Session()
        ses.proxies = {"https": f"http://{proxy}"}
    else:
        ses = Session()

    for _ in range(num_reports):
        try:
            user_agent = get_user_agent()
            headers = {
                "User-Agent": user_agent,
            }
            report_form = {
                "username": username,  # Update with actual form data required
                "reason": "This profile violates our community guidelines."  # Example reason
            }
            res = ses.post("https://help.instagram.com/ajax/help/contact/submit/page", data=report_form, headers=headers, timeout=10)
            res.raise_for_status()
            print_success("Successfully reported! - se.cj")
        except Exception as e:
            print_error("Connection error has occurred! (FormRequestsError) - se.cj", e)
            return

def parse_proxy_file(file_path):
    """
    Parse a file to retrieve proxy information.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    proxies = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    type_, ip_, port_ = line.split(':')
                    proxy = {"https": f"http://{ip_}:{port_}"}
                    proxies.append(proxy)
    except Exception as e:
        print_error("Error reading proxy file - se.cj", e)
    return proxies

def print_success(message):
    """
    Print a success message to the terminal.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    print(Fore.GREEN + "[+] " + Style.RESET_ALL + message + " - se.cj")

def print_error(message, e=None):
    """
    Print an error message to the terminal.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    print(Fore.RED + "[-] " + Style.RESET_ALL + message + " - se.cj")
    if e:
        print(Fore.RED + "[-] " + Style.RESET_ALL + str(e) + " - se.cj")

def main():
    """
    Main function to execute the script.

    Copyright Notice:
    This function is part of the script developed by se.cj.
    Unauthorized modification or distribution of this function
    is prohibited.
    """
    print("This script is developed by se.cj. All rights reserved.")
    
    username = input("Enter the username of the account to run the tool on: ").strip()
    password = input("Enter the password of the account to run the tool on: ").strip()
    target_username = input("Enter the target username to report: ").strip()

    num_reports = int(input("Enter the number of reports to send: ").strip())

    proxies = parse_proxy_file(input("Enter the path to your proxy file: ").strip())

    report_profile_attack(target_username, num_reports=num_reports, proxies=proxies)

if __name__ == "__main__":
    main()
