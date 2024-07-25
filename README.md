# Shield V 1.1

![Shield Logo]('hello')

Shield V 1.1 is a tool developed to manage and change IP addresses using Tor and display IP information automatically. This README will guide you through the installation, usage, and features of Shield V 1.1.

## Features

- **IP Management**: Change your IP address periodically using the Tor network.
- **IP Information**: Display detailed information about your current IP address, including country and ISP.
- **Automation**: Set the interval for IP changes and the number of changes to perform automatically.

## Installation

Follow these steps to install Shield V 1.1:

1. **Download the repository**:
    ```bash
    git clone https://github.com/MuntasirArafat/Shield.git
    ```
    ```bash
       cd Shield
    ```
2. **Add  permissions  script**:

 ```bash
   chmod +x installer.py
```
4. **Run the installation script in root mode**:
    ```bash
    sudo python3 installer.py
    ```

   This script will:
   - Set the necessary permissions.
   - Copy the main script to the appropriate directory.
   - Backup the existing web folder and replace it with the new one.
   - Set full permissions for CSS, JS, and images folders.

## Usage

To use Shield V 1.1, simply type `shield` in the terminal:

```bash
shield
```
Upon running the tool, you will see a banner and some initial setup messages. You can configure the time interval for changing IPs and the number of IP changes to perform.

## Changing IPs

The tool will change your IP address using Tor and display the new IP information.

## Example Output

```bash
[INFO] Connecting to Tor...
[INFO] Please ensure your SOCKS proxy is set to 127.0.0.1:9050
[INFO] Time to change IP in seconds [default=60] >> 60
[INFO] Number of IP changes [default=1000, enter 0 for infinite] >> 10

[INFO] IP address updated to: 192.0.2.1
[INFO] Country: Exampleland
[INFO] ISP: ExampleISP
```
## Uninstallation
If you need to uninstall Shield V 1.1, run the following command:

```bash
sudo python3 installer.py
```
Then, select the uninstallation option when prompted. This will remove the tool and restore the original web folder from the backup.

## Support

If you encounter any issues or have questions, please visit the GitHub repository and open an issue.

Enjoy using Shield V 1.1! Developed by <a href="https://github.com/MuntasirArafat">Muntasir Arafat</a>.
```bash

+--------------------------------------------------------------+
|            _____ _    _ _____ ______ _      _____            |
|           / ____| |  | |_   _|  ____| |    |  __ \           |
|          | (___ | |__| | | | | |__  | |    | |  | |          |
|           \___ \|  __  | | | |  __| | |    | |  | |          |
|           ____) | |  | |_| |_| |____| |____| |__| |          |
|          |_____/|_|  |_|_____|______|______|_____/           |
|                                                              |
|                         Shield V 1.1                         |
|                Developed by Muntasir Arafat                  |
+--------------------------------------------------------------+
```


