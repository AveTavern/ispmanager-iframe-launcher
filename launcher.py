# ispmanager iframe installation kit
import subprocess
cmd = 'pip'+' install'+' requests'
subprocess.run([cmd], shell=True)

import requests
url = 'https://raw.githubusercontent.com/AveTavern/ispmanager-iframe-launcher/Development/ispmgr_mod_testframe.xml'
response = requests.get(url)
with open ('/usr/local/mgr5/etc/xml/ispmgr_mod_testframe.xml', 'w+') as file:
    file.write(response.text)
    file.close()
print("ispmgr_mod_testframe.xml file createed in /usr/local/mgr5/etc/xml")

file = open('/usr/local/mgr5/etc/xml/ispmgr_mod_testframe.xml', 'a')
lang_name = input("Choose localisation options\n 1)English\n 2)Russian\n 3)English and Russian\n")
if lang_name == "1":
    file.write('     <lang name="en">\n'
                '        <messages name="desktop">')
    group_menu_name = input("Input the group menu name in English\n")
    file.write('<msg name="modernmenu_my_group">'+group_menu_name+'</msg>\n')

    menu_item_name = input("Input the menu item name title in English\n")
    file.write('<msg name="modernmenu_testframe">'+menu_item_name+'</msg>\n'
                '    </messages>\n'
                '</lang>\n'
                '</mgrdata>\n')
elif lang_name == "2":
    file.write('     <lang name="ru">\n'
                '        <messages name="desktop">')
    group_menu_name = input("Input the group menu name in Russian\n")
    file.write('<msg name="modernmenu_my_group">'+group_menu_name+'</msg>\n')

    menu_item_name = input("Input the menu item name title in Russian\n")
    file.write('<msg name="modernmenu_testframe">'+menu_item_name+'</msg>\n'
                '    </messages>\n'
                '</lang>\n'
                '</mgrdata>\n')
elif lang_name == "3":
    file.write('     <lang name="en">\n'
                '        <messages name="desktop">')
    group_menu_name = input("Input the group menu name in English\n")
    file.write('<msg name="modernmenu_my_group">'+group_menu_name+'</msg>\n')

    menu_item_name = input("Input the menu item name title in English\n")
    file.write('<msg name="modernmenu_testframe">'+menu_item_name+'</msg>\n'
                '    </messages>\n'
                '</lang>\n'
                '</mgrdata>\n')
    
    file.write('     <lang name="ru">\n'
                '        <messages name="desktop">')
    group_menu_name = input("Input the group menu name in Russian\n")
    file.write('<msg name="modernmenu_my_group">'+group_menu_name+'</msg>\n')

    menu_item_name = input("Input the menu item name title in Russian\n")
    file.write('<msg name="modernmenu_testframe">'+menu_item_name+'</msg>\n'
                '    </messages>\n'
                '</lang>\n'
                '</mgrdata>\n')
else:
    print("English language is set up as default")
    file.write('     <lang name="en">\n'
                '        <messages name="desktop">')
    group_menu_name = input("Input the group menu name\n")
    file.write('<msg name="modernmenu_my_group">'+group_menu_name+'</msg>\n')

    menu_item_name = input("Input the menu item name title\n")
    file.write('<msg name="modernmenu_testframe">'+menu_item_name+'</msg>\n'
                '    </messages>\n'
                '</lang>\n'
                '</mgrdata>\n')
file.close()

url = 'https://raw.githubusercontent.com/AveTavern/ispmanager-iframe-launcher/Development/testframe.sh'
response = requests.get(url)
with open ('/usr/local/mgr5/addon//testframe.sh', 'w+') as file:
    file.write(response.text)
    file.close()
print("testframe.sh file createed in /usr/local/mgr5/addon/")

cmd = 'chmod 755 /usr/local/mgr5/addon/testframe.sh'
subprocess.run([cmd], shell=True)
print("Handler testframe.sh was given rights to plugin handler")

url  = 'https://raw.githubusercontent.com/AveTavern/ispmanager-iframe-launcher/Development/testframe.xml'
response = requests.get(url)
with open ('/usr/local/mgr5/addon/testframe.xml', 'w+') as file:
    file.write(response.text)
    file.close()
print("testframe.xml file createed in /usr/local/mgr5/addon/")

title_name = input("Input the Tab title\n")
file = open('/usr/local/mgr5/addon/testframe.xml', 'a')
file.write('        <msg name="title">'+title_name+'</msg>\n')

frame_name = input("Input the frame title\n")
file.write('        <msg name="frame">'+frame_name+'</msg>\n'
            '    </messages>\n')
    
frame_url = input("Input the iframe url, use https:domain.com mask\n")
file.write('    <roundcubeframe>'+frame_url+'</roundcubeframe>\n'
            '</doc>')
file.close()

# Addons installation (Yandex Metrics)
install_package = input("Would you like to install integration with Yandex.Metrics Y/N \n")
python_env = input("Input your Python environment name\n")
if install_package == "Y":
    import os
    os.chdir("/var/www/")
    os.mkdir("yandex-integration")

    url = 'https://raw.githubusercontent.com/AveTavern/yandex-ispmanager/main/yandex-launcher.py'
    response = requests.get(url)
    with open ('/var/www/yandex-integration/yandex-launcher.py', 'w+') as file:
        file.write(response.text)
        file.close()
    print("yandex-laucnher.py file createed in /var/www/yandex-integration/yandex-laucnher.py")

    # addon mark installation
    with open ('/var/www/yandex-integration/deleteme.txt', 'w+') as file:
        file.write("yandex-addon")
    
    cmd = python_env+'//bin/python3.11 /var/www/yandex-integration/yandex-launcher.py'
    subprocess.run([cmd], shell=True)

# cleaner start
url = 'https://raw.githubusercontent.com/AveTavern/ispmanager-iframe-launcher/Development/cleaner.py'
response = requests.get(url)
with open ('/var/www/iframe-launcher-cleaner.py', 'w+') as file:
    file.write(response.text)
    file.close()
print("iframe-laucnher-cleaner.py file createed in /var/www/")

cmd = python_env+'/bin/python3.11 /var/www/iframe-launcher-cleaner.py'
subprocess.run([cmd], shell=True)
