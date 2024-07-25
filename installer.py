import os
import shutil
import sys

def print_banner():
    """Print the tool banner with color."""
    banner = '''
\033[1;32;40m
+--------------------------------------------------------------+
|            _____ _    _ _____ ______ _      _____            |
|           / ____| |  | |_   _|  ____| |    |  __ \\           |
|          | (___ | |__| | | | | |__  | |    | |  | |          |
|           \\___ \\|  __  | | | |  __| | |    | |  | |          |
|           ____) | |  | |_| |_| |____| |____| |__| |          |
|          |_____/|_|  |_|_____|______|______|_____/           |
|                                                              |
|                         Shield V 1.1                         |
|                Developed by Muntasir Arafat                  |
+--------------------------------------------------------------+
\033[0m
'''
    print(banner)

def install():
    """Install the tool."""
    print('\033[1;34;40mStarting installation...\033[0m')
    try:
        os.system('chmod 777 shield.py')
        os.makedirs('/usr/share/shield', exist_ok=True)
        shutil.copy('shield.py', '/usr/share/shield/shield.py')

        cmnd = '#! /bin/sh\nexec python3 /usr/share/shield/shield.py "$@"'
        with open('/usr/bin/shield', 'w') as file:
            file.write(cmnd)
        os.system('chmod +x /usr/bin/shield && chmod +x /usr/share/shield/shield.py')

        print('\n\033[1;32;40mCongratulations! Shield is installed successfully.\033[0m')
        print('From now on, just type \033[1;36;40mshield\033[0m in the terminal to run the tool.')

        # Backup and replace web folder
        backup_folder = '/usr/share/kali-defaults/old_web_backup'
        web_folder = '/usr/share/kali-defaults/web'
        config_web_folder = 'config/web'

        if os.path.exists(web_folder):
            os.makedirs(backup_folder, exist_ok=True)
            shutil.move(web_folder, backup_folder)
            print('\n\033[1;32;40mWeb folder backed up successfully.\033[0m')
        shutil.copytree(config_web_folder, web_folder)
        print('\033[1;32;40mWeb folder replaced successfully.\033[0m')

        # Set full permissions for CSS, JS, and images folders
        for folder in ['css', 'js', 'images']:
            folder_path = os.path.join(web_folder, folder)
            if os.path.exists(folder_path):
                os.system(f'chmod -R 777 {folder_path}')
                print(f'\033[1;32;40mPermissions set for {folder} folder.\033[0m')

    except PermissionError as e:
        print(f'\033[1;31;40mPermissionError: {e}\033[0m')
        print('\033[1;31;40mPlease run the script as root or use sudo.\033[0m')
    except FileNotFoundError as e:
        print(f'\033[1;31;40mFileNotFoundError: {e}\033[0m')
        print('\033[1;31;40mMake sure all necessary files are in the correct location.\033[0m')
    except Exception as e:
        print(f'\033[1;31;40mAn unexpected error occurred: {e}\033[0m')

def uninstall():
    """Uninstall the tool."""
    print('\033[1;34;40mStarting uninstallation...\033[0m')
    try:
        # Remove the tool files
        if os.path.exists('/usr/share/shield/shield.py'):
            os.system('rm -r /usr/share/shield')
            os.system('rm /usr/bin/shield')
            print('\n\033[1;31;40mShield has been removed successfully.\033[0m')

            # Restore the web folder from backup
            backup_folder = '/usr/share/kali-defaults/old_web_backup'
            web_folder = '/usr/share/kali-defaults/web'

            if os.path.exists(backup_folder):
                # Ensure the destination web folder does not exist before restoring
                if os.path.exists(web_folder):
                    shutil.rmtree(web_folder)
                
                shutil.move(os.path.join(backup_folder, 'web'), web_folder)
                shutil.rmtree(backup_folder)
                print('\033[1;32;40mWeb folder restored from backup successfully.\033[0m')
            else:
                print('\033[1;31;40mNo backup folder found. Web folder was not restored.\033[0m')

        else:
            print('\n\033[1;31;40mError: The tool is not installed.\033[0m')
    except PermissionError as e:
        print(f'\033[1;31;40mPermissionError: {e}\033[0m')
        print('\033[1;31;40mPlease run the script as root or use sudo.\033[0m')
    except FileNotFoundError as e:
        print(f'\033[1;31;40mFileNotFoundError: {e}\033[0m')
        print('\033[1;31;40mMake sure the backup folder and files are in the correct location.\033[0m')
    except Exception as e:
        print(f'\033[1;31;40mAn unexpected error occurred: {e}\033[0m')


def main():
    """Main function to handle installation or uninstallation."""
    os.system('clear')  # Clear the terminal
    print_banner()
    try:
        choice = input('[+] To install, press (Y). To uninstall, press (N) >> ').strip().upper()
        if choice == 'Y':
            install()
        elif choice == 'N':
            uninstall()
        else:
            print('\n\033[1;33;40mInvalid choice. Please enter (Y) or (N).\033[0m')
    except KeyboardInterrupt:
        print('\n\033[1;31;40mOperation cancelled by user. Shield is deactivated.\033[0m')

if __name__ == "__main__":
    main()
