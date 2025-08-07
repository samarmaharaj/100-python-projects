import subprocess

def get_wifi_passwords():
    # Run the command to get the list of all WiFi profiles
    command = "netsh wlan show profiles"
    networks = subprocess.check_output(command, shell=True).decode('utf-8', errors="backslashreplace").split('\n')
    
    # Extract the WiFi profile names from the command output
    profiles = [line.split(":")[1].strip() for line in networks if "All User Profile" in line]

    wifi_details = []

    for profile in profiles:
        # Run the command to get the details of each profile
        profile_info_cmd = f"netsh wlan show profile name=\"{profile}\" key=clear"
        profile_info = subprocess.check_output(profile_info_cmd, shell=True).decode('utf-8', errors="backslashreplace").split('\n')
        
        # Extract the WiFi password from the profile details
        password_line = [line.split(":")[1].strip() for line in profile_info if "Key Content" in line]

        password = password_line[0] if password_line else None

        wifi_details.append({"Profile": profile, "Password": password})
    
    return wifi_details

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    for wifi in wifi_passwords:
        print(f"Profile: {wifi['Profile']}, Password: {wifi['Password']}")
