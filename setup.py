import os
import time

if (sys.platform.startswith("linux")) :
        if (subprocess.getoutput("whoami")) != "root" :
                print("[!] Please run with 'sudo' permissions")
                sys.exit() #exit
        else:
                pass
else:
    pass

os.system('sudo apt install -y software-properties-common')
os.system('sudo dpkg --add-architecture i386')
os.system('wget -nc https://dl.winehq.org/wine-builds/winehq.key')
os.system('sudo apt-key add winehq.key')
os.system("sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/debian/ buster main'")
os.system('sudo apt update')
os.system('sudo apt install wine wine64 winbind winetricks')
os.system('curl "https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe" -o python399.exe')
time.sleep(5)
os.system('sudo winecfg')
os.system('sudo wine python399.exe')
os.system('sudo rm -r python399.exe')
