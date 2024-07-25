import time
import os
import subprocess
import requests

def install_if_missing(package, install_cmd):
    """Install a package if it is not already installed."""
    try:
        subprocess.check_output(f'dpkg -s {package}', shell=True)
    except subprocess.CalledProcessError:
        print(f'\033[1;33;40m[INFO] Installing {package}...\033[0m')
        os.system('sudo apt update && sudo apt install -y ' + package)

def ensure_python_packages():
    """Ensure necessary Python packages are installed."""
    try:
        import requests
    except ImportError:
        os.system('pip3 install requests requests[socks]')
        print('\033[1;33;40m[INFO] Python packages installed\033[0m')

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear')

def get_external_ip():
    """Get the current external IP address using ipify."""
    url = 'https://api.ipify.org?format=json'
    try:
        response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        response.raise_for_status()
        data = response.json()
        ip = data.get('ip', 'Unknown IP')
    except requests.RequestException as e:
        print(f"\033[1;31;40m[ERROR] Unable to fetch IP address: {e}\033[0m")
        ip = 'Unknown IP'
    
    return ip

def get_ip_info(ip):
    """Get detailed IP information using ip-api.com."""
    url = f'http://ip-api.com/json/{ip}'
    try:
        response = requests.get(url, proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
        response.raise_for_status()
        data = response.json()
        country_name = data.get('country', 'Unknown Country')
        isp = data.get('isp', 'Unknown ISP')
    except requests.RequestException as e:
        print(f"\033[1;31;40m[ERROR] Unable to fetch IP information: {e}\033[0m")
        country_name = 'Unknown Country'
        isp = 'Unknown ISP'
    
    return country_name, isp

def get_external_ip_and_info():
    """Get the current external IP address, country name, and ISP."""
    ip = get_external_ip()
    country_name, isp = get_ip_info(ip)
    return ip, country_name, isp

def change_ip():
    """Change the IP address by reloading the Tor service."""
    os.system('sudo systemctl reload tor')
    ip, country, isp = get_external_ip_and_info()
    print(f'\033[1;32;40m[INFO] IP address updated to: {ip}\033[0m')
    print(f'\033[1;32;40m[INFO] Country: {country}\033[0m')
    print(f'\033[1;32;40m[INFO] ISP: {isp}\033[0m\n')

def print_banner():
    """Print the banner and table with color."""
    banner = '''
\033[1;32;40m
    _____ _    _ _____ ______ _      _____  
   / ____| |  | |_   _|  ____| |    |  __ \ 
  | (___ | |__| | | | | |__  | |    | |  | |
   \___ \|  __  | | | |  __| | |    | |  | |
   ____) | |  | |_| |_| |____| |____| |__| |
  |_____/|_|  |_|_____|______|______|_____/ 
                    
                    Shield V 1.1
          Developed by Muntasir Arafat
\033[0m'''

    table = '''
+----------------+--------------------------------------------------+
|      Field     |                Information                       |
+----------------+--------------------------------------------------+
| Author         | Muntasir Arafat                                  |
| GitHub         | https://github.com/MuntasirArafat                |
| License        | MIT License                                      |
| Tool Name      | Shield V 1.1                                     |
| Description    | A tool to manage and change IP addresses using   |
|                | Tor and display IP information.                  |
+----------------+--------------------------------------------------+
\033[0m'''

    print(banner)
    print(table)

def main():
    install_if_missing('python3-pip', 'python3-pip')
    ensure_python_packages()
    install_if_missing('tor', 'tor')
    clear_screen()
    print_banner()

    os.system('sudo systemctl start tor')
    print("\033[1;32;40m[INFO] Connecting to Tor...\033[0m")
    time.sleep(3)  # Wait for Tor to start

    print("\033[1;32;40m[INFO] Please ensure your SOCKS proxy is set to 127.0.0.1:9050\033[0m")

    try:
        interval = int(input("\033[1;34;40m[INFO] Time to change IP in seconds [default=60] >> \033[0m") or 60)
        iterations = int(input("\033[1;34;40m[INFO] Number of IP changes [default=1000, enter 0 for infinite] >> \033[0m") or 1000)
        
        if iterations == 0:
            while True:
                time.sleep(interval)
                change_ip()
        else:
            for _ in range(iterations):
                time.sleep(interval)
                change_ip()
    except KeyboardInterrupt:
        print('\n\033[1;31;40m[INFO] Shield is deactivated\033[0m')

if __name__ == "__main__":
    main()
