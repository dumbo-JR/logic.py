import os
import subprocess
from datetime import datetime

RED = "\033[31m"
RESET = "\033[0m"
banner = """
	 ▄█        ▄██████▄     ▄██████▄   ▄█   ▄████████ 
	███       ███    ███   ███    ███ ███  ███    ███ 
	███       ███    ███   ███    █▀  ███▌ ███    █▀  
	███       ███    ███  ▄███        ███▌ ███        
	███       ███    ███ ▀▀███ ████▄  ███▌ ███        
	███       ███    ███   ███    ███ ███  ███    █▄  
	███▌    ▄ ███    ███   ███    ███ ███  ███    ███ 
	█████▄▄██  ▀██████▀    ████████▀  █▀   ████████▀  
	▀                                                 
"""
print(RED + banner + RESET)

def get_choice():
    print("Choose the type of device you want to scan:")
    print("1. Web Server")
    print("2. Router")
    choice = input("Enter 1 or 2: ")
    return choice

def get_target():
    target = input("Enter the IP address or URL of the device: ")
    return target

def run_nmap(command, target, output_file):
    full_command = f"nmap {command} {target}"
    print(f"Running command: {full_command}")
    
    try:
        result = subprocess.check_output(full_command, shell=True, text=True)
        with open(output_file, "a") as file:
            file.write(result)
        print(f"Results have been saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    # Get the user's choice
    choice = get_choice()

    # Validate the user's choice
    if choice not in ['1', '2']:
        print("Invalid choice. Please run the script again and choose 1 or 2.")
        return

    # Get the target IP/URL
    target = get_target()

    # Define the Nmap command based on the user's choice
    if choice == '1':
        nmap_command = "-p 80,443,22,21,25,3306 -A"  # Scanning common web server ports and using aggressive scan for details
        device_type = "WebServer"
    elif choice == '2':
        nmap_command = "-sP -O"  # Simple ping scan with OS detection for routers
        device_type = "Router"

    # Create the output file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"nmap_scan_{device_type}_{timestamp}.txt"

    # Run the Nmap command and save the output
    run_nmap(nmap_command, target, output_file)

if __name__ == "__main__":
    main()
