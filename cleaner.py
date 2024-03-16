import os
import subprocess

ispmanager_user = input("Print user that is used to execute script\n")
os.remove("/"+ispmanager_user+"/launcher.py")

if os.path.exists("/var/www/deleteme.txt"):
        file = open('/var/www/deleteme.txt', 'r')
        file = read()
        if file == "yandex-addon":
                file = close()
                os.remove("/var/www/deleteme.txt")
        else:
                print(file+" idk what is it")
else:
        print("no adons installed")

reboot_validation = input("You should reboot server. Can we reboot now? Y / N\n")
if reboot_validation == "Y":
        print("Reboot confirmed, please wait")
        cmd = '/usr/local/mgr5/sbin/mgrctl'+' -m'+' ispmgr'+' reboot_confirm'+' sok=ok'
        subprocess.run([cmd], shell=True)
else:
    print("Reboot cancelled")
