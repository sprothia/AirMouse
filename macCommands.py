import subprocess
import os
import webbrowser as Browser

#COMPUTER COMMANDS----------------------------------------------------------
def open_website(website_name):
    applescript_cmd = f'tell application "Chrome" to open location "https://{website_name}/"'
    subprocess.run(['osascript', '-e', applescript_cmd], check=True)
    
def increment_volume():
    
    get_volume_cmd = 'output volume of (get volume settings)'
    set_volume_cmd = 'set volume output volume {}'
    
    output = subprocess.check_output(['osascript', '-e', get_volume_cmd])
    current_volume = int(output.strip())
    
    volume_increment = 10
    new_volume = min(100, max(0, current_volume + volume_increment))
    
    subprocess.run(['osascript', '-e', set_volume_cmd.format(new_volume)], check=True)

def decrement_volume():
    
    get_volume_cmd = 'output volume of (get volume settings)'
    set_volume_cmd = 'set volume output volume {}'
    
    output = subprocess.check_output(['osascript', '-e', get_volume_cmd])
    current_volume = int(output.strip())
    
    volume_increment = -10
    new_volume = min(100, max(0, current_volume + volume_increment))
    
    subprocess.run(['osascript', '-e', set_volume_cmd.format(new_volume)], check=True)
    
def open_application():
    cmd = 'osascript -e \'tell app "Spotify" to activate\''
    subprocess.run(cmd, shell=True)

def shutdown_mac():
    script = '''
    tell application "System Events" to shut down
    '''

    subprocess.run(['osascript', '-e', script])

def restart_mac():
    script = '''
    tell application "System Events" to restart
    '''

    subprocess.run(['osascript', '-e', script])
    
def sleep_mac():
    script = '''
    tell application "System Events" to sleep
    '''

    subprocess.run(['osascript', '-e', script])
    

def launch_application():
    script = '''tell application "Android Studio" to launch'''
    subprocess.run(['osascript', '-e', script])
    
    
def close_application(app_name):
    script = f'''
    tell application "{app_name}"
        quit
    end tell
    '''

    subprocess.run(['osascript', '-e', script])

def get_tab_count():
    browser = Browser()
    tabs = browser.list_tab()
    tab_count = len(tabs)
    browser.close_tab(tabs)
    return tab_count


def switch_between_applications():
    script = """
    tell application "System Events"
        key code 48 using {command down}
    end tell
    """
    os.system(f"osascript -e '{script}'")

def switch_to_previous_tab():
    script = """
    tell application "Google Chrome"
        activate
        tell application "System Events"
            keystroke "[" using {command down, shift down}
        end tell
    end tell
    """
    os.system(f"osascript -e '{script}'")
    
def switch_to_next_tab():
    script = """
    tell application "Google Chrome"
        activate
        tell application "System Events"
            keystroke "]" using {command down, shift down}
        end tell
    end tell
    """
    os.system(f"osascript -e '{script}'")

def turn_on_wifi():
    os.system("networksetup -setairportpower airport on")

def turn_off_wifi():
    os.system("networksetup -setairportpower airport off")

def draft_email(email):
    url = f"https://mail.google.com/mail/?view=cm&fs=1&to={email}"
    Browser.open(url)
    
