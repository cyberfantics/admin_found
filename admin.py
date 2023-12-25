import requests
import os
import  webbrowser
import sys
import time
import platform
import pyfiglet

count = 0
#======== colors ======#
red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
#======== color ======#

#======== paths ======#
lists = [
    '/wp-login.php',
    '/admin/',
    '/wp-config.php',
    '/admin.php',
    '/cpanel/',
    '/wp-admin/',
    '/administrator/',
    '/admin/login.php',
    '/admin/index.php',
    '/admin/login/',
    '/admin/home/',
    '/admin_area/',
    '/adminpanel/',
    '/admincontrol/',
    '/admin1/',
    '/admin2/',
    '/admincp/',
    '/admin123/',
    '/admin4_account/',
    '/admin4_colon/',
    '/admin4_login/',
    '/admin4_password/',
    '/admin4_root/',
    '/admin_/',
    '/admin_login/',
    '/admin_home/',
    '/admin_area/admin/',
    '/admin_area/login/',
    '/admin_area/index.php',
    '/admin_area/home/',
    '/admin_area/login.php',
    '/admin_area/admin.php',
    '/admin_area/administrator/',
    '/admin_area/administrators/',
    '/admin_area/1/',
    '/admin_area/account/',
    '/admin_area/admin/index.php',
    '/admin_area/admin/login.php',
    '/admin_area/admin/home.php',
    '/admin_area/admin_area/',
    '/admin_area/admin/control/',
    '/admin_area/admin_panel/',
    '/admin_area/admin/login/',
    '/admin_area/admin/admin.php',
    '/admin_area/admin/account.php',
    '/admin_area/admin_area/index.php',
    '/admin_area/admin_area/admin.php',
    '/admin_area/admin_area/admin_area.php',
    '/admin_area/admin_area/admin_area/admin.php',
    '/admin_area/administrator/index.php',
    '/admin_area/administrator/login.php',
    '/admin_area/administrator/login/',
    '/admin_area/administrator/home.php',
    '/admin_area/administrator/control/',
    '/admin_area/administrator/account.php',
    '/admin_area/administrator/admin.php',
    '/admin_area/login.html',
    '/admin_area/index.html',
    '/admin_area/admin.html',
    '/admin_area/admin/index.html',
    '/admin_area/admin/login.html',
    '/admin_area/admin_area/index.html',
    '/admin_area/admin_area/admin.html',
    '/admin_area/admin_area/admin_area.html',
    '/admin_area/administrator/login.html',
    '/admin_area/administrator/index.html',
    '/admin_area/administrator/home.html',
    '/login/',
    '/login.php',
    '/login.html',
    '/admin/login.html',
    '/admin/index.html',
    '/admin/login.html',
    '/admin/admin.html',
    '/admin/home.html',
    '/administrator/index.html',
    '/administrator/login.html',
    '/administrator/index.php',
    '/administrator/login.php',
    '/administrator/',
    '/user/login/',
    '/user/index.php',
    '/user/index.html',
    '/user/login.html',
    '/login/administrator/',
    '/login/admin/',
    '/login/account/',
    '/login/administrator/login.php',
    '/login/admin/login.php',
    '/login/admin/account.php',
    '/login/administrator/account.php',
    '/login/account.php',
    '/admin/control.php',
    '/admin/admin/control.php',
    '/admin_area/admin/control.php',
    '/admin_area/admin_area/admin/control.php',
    '/admin_area/admin_area/admin_area/admin/control.php',

    # Additional Paths
    '/_admin',
    '/_login',
    '/_control',
    '/admin/login',
    '/admin/dashboard',
    '/admin/orders',
    '/admin/products',
    '/wp-admin/login.php',
    '/wp-admin/index.php',
    '/wp-admin/login/',
    '/cpanel/login',
    '/cpanel/index.php',
    '/cpanel/login.php',
    '/store/admin',
    '/shop/admin',
    '/cart/admin',
    '/checkout/admin',
    '/admin/blogger/',
    '/blogger/admin/',
    '/blog/admin/',
    '/blog/login/',
    '/wp-content/plugins/wp-useronline/',
    '/wp-content/plugins/imagemagick-engine/',
    '/wp-content/plugins/3dady-real-time-web-stats/',
    '/admin/index.php',

    # Additional Paths - Based on Common Patterns
    '/admin2019/',
    '/admin2020/',
    '/admin2021/',
    '/admin2022/',
    '/admin2023/',
    '/admin2024/',
    '/admin2025/',
    '/admin2026/',
    '/admin2027/',
    '/admin2028/',
    '/admin2029/',
    '/adminportal/',
    '/adminpage/',
    '/admincontrolpanel/',
    '/adminweb/',
    '/adminsite/',
    '/adminconsole/',
    '/adminweb/login.php',
    '/adminsite/login.php',
    '/adminconsole/login.php',
    '/adminweb/index.php',
    '/adminsite/index.php',
    '/adminconsole/index.php',
    '/adminweb/login/',
    '/adminsite/login/',
    '/adminconsole/login/',
    '/adminweb/admin.php',
    '/adminsite/admin.php',
    '/adminconsole/admin.php',
    '/adminweb/admin/',
    '/adminsite/admin/',
    '/adminconsole/admin/',
    '/webadmin/',
    '/webadmin/login.php',
    '/webadmin/index.php',
    '/webadmin/login/',
    '/webadmin/admin.php',
    '/webadmin/admin/',
    '/webadministrator/',
    '/webadminpanel/',
    '/admincp/login.php',
    '/admincp/login/',
    '/admincp/index.php',
    '/admincp/admin.php',
    '/admincp/admin/',
    '/adminlogin.php',
    '/adminlogin/',
    '/admin-login.php',
    '/admin-login/',
    '/admin/home.php',
    '/admin/home/',
    '/admin/admin_login.php',
    '/admin/admin_login/',
    '/admin/control.php',
    '/admin/control/',
    '/admin/admincontrol/',
    '/admin/admin-control/',
    '/admin/adminweb/',
    '/admin/webadmin/',
    '/admin/siteadmin/',
    '/admin/consoleadmin/',
    '/admin/superadmin/',
    '/admin/portal/',
    '/admin/adminportal/',
    '/admin/admin-page/',
    '/admin/administrator/login.php',
    '/admin/administrator/login/',
    '/admin/administrator/index.php',
    '/admin/administrator/index/',
    '/admin/administrator/home.php',
    '/admin/administrator/home/',
    '/admin/administrator/control/',
    '/admin/administrator/account.php',
    '/admin/administrator/account/',
    '/admin/administrator/admin.php',
    '/admin/administrator/admin/',
    '/login/admin/',
    '/login/admin/login.php',
    '/login/admin/login/',
    '/login/admin/admin.php',
    '/login/admin/admin/',
    '/login/administrator/',
    '/login/administrator/login.php',
    '/login/administrator/login/',
    '/login/administrator/index.php',
    '/login/administrator/index/',
    '/login/administrator/home.php',
    '/login/administrator/home/',
    '/login/administrator/control/',
    '/login/administrator/account.php',
    '/login/administrator/account/',
    '/login/administrator/admin.php',
    '/login/administrator/admin/',
    '/user/admin/',
    '/user/admin/login.php',
    '/user/admin/login/',
    '/user/admin/index.php',
    '/user/admin/index/',
    '/user/admin/home.php',
    '/user/admin/home/',
    '/user/admin/control/',
    '/user/admin/account.php',
    '/user/admin/account/',
    '/user/admin/admin.php',
    '/user/admin/admin/',
    '/control/admin/',
    '/control/admin/login.php',
    '/control/admin/login/',
    '/control/admin/index.php',
    '/control/admin/index/',
    '/control/admin/home.php',
    '/control/admin/home/',
    '/control/admin/control/',
    '/control/admin/account.php',
    '/control/admin/account/',
    '/control/admin/admin.php',
    '/control/admin/admin/',
    '/console/admin/',
    '/console/admin/login.php',
    '/console/admin/login/',
    '/console/admin/index.php',
    '/console/admin/index/',
    '/console/admin/home.php',
    '/console/admin/home/',
    '/console/admin/control/',
    '/console/admin/account.php',
    '/console/admin/account/',
    '/console/admin/admin.php',
    '/console/admin/admin/',
    '/superadmin/',
    '/superadmin/login.php',
    '/superadmin/login/',
    '/superadmin/index.php',
    '/superadmin/index/',
    '/superadmin/home.php',
    '/superadmin/home/',
    '/superadmin/control/',
    '/superadmin/account.php',
    '/superadmin/account/',
    '/superadmin/admin.php',
    '/superadmin/admin/',
    '/portal/admin/',
    '/portal/admin/login.php',
    '/portal/admin/login/',
    '/portal/admin/index.php',
    '/portal/admin/index/',
    '/portal/admin/home.php',
    '/portal/admin/home/',
    '/portal/admin/control/',
    '/portal/admin/account.php',
    '/portal/admin/account/',
    '/portal/admin/admin.php',
    '/portal/admin/admin/',
    '/admin2019/login.php',
    '/admin2019/login/',
    '/admin2019/index.php',
    '/admin2019/index/',
    '/admin2019/home.php',
    '/admin2019/home/',
    '/admin2019/control/',
    '/admin2019/account.php',
    '/admin2019/account/',
    '/admin2019/admin.php',
    '/admin2019/admin/',
    '/admin2020/login.php',
    '/admin2020/login/',
    '/admin2020/index.php',
    '/admin2020/index/',
    '/admin2020/home.php',
    '/admin2020/home/',
    '/admin2020/control/',
    '/admin2020/account.php',
    '/admin2020/account/',
    '/admin2020/admin.php',
    '/admin2020/admin/',
    '/admin2021/login.php',
    '/admin2021/login/',
    '/admin2021/index.php',
    '/admin2021/index/',
    '/admin2021/home.php',
    '/admin2021/home/',
    '/admin2021/control/',
    '/admin2021/account.php',
    '/admin2021/account/',
    '/admin2021/admin.php',
    '/admin2021/admin/',
    '/admin2022/login.php',
    '/admin2022/login/',
    '/admin2022/index.php',
    '/admin2022/index/',
    '/admin2022/home.php',
    '/admin2022/home/',
    '/admin2022/control/',
    '/admin2022/account.php',
    '/admin2022/account/',
    '/admin2022/admin.php',
    '/admin2022/admin/',
    '/admin2023/login.php',
    '/admin2023/login/',
    '/admin2023/index.php',
    '/admin2023/index/',
    '/admin2023/home.php',
    '/admin2023/home/',
    '/admin2023/control/',
    '/admin2023/account.php',
    '/admin2023/account/',
    '/admin2023/admin.php',
    '/admin2023/admin/',
    '/admin2024/login.php',
    '/admin2024/login/',
    '/admin2024/index.php',
    '/admin2024/index/',
    '/admin2024/home.php',
    '/admin2024/home/',
    '/admin2024/control/',
    '/admin2024/account.php',
    '/admin2024/account/',
    '/admin2024/admin.php',
    '/admin2024/admin/',
    '/admin2025/login.php',
    '/admin2025/login/',
    '/admin2025/index.php',
    '/admin2025/index/',
    '/admin2025/home.php',
    '/admin2025/home/',
    '/admin2025/control/',
    '/admin2025/account.php',
    '/admin2025/account/',
    '/admin2025/admin.php',
    '/admin2025/admin/',
    '/admin2026/login.php',
    '/admin2026/login/',
    '/admin2026/index.php',
    '/admin2026/index/',
    '/admin2026/home.php',
    '/admin2026/home/',
    '/admin2026/control/',
    '/admin2026/account.php',
    '/admin2026/account/',
    '/admin2026/admin.php',
    '/admin2026/admin/',
    '/admin2027/login.php',
    '/admin2027/login/',
    '/admin2027/index.php',
    '/admin2027/index/',
    '/admin2027/home.php',
    '/admin2027/home/',
    '/admin2027/control/',
    '/admin2027/account.php',
    '/admin2027/account/',
    '/admin2027/admin.php',
    '/admin2027/admin/',
    '/admin2028/login.php',
    '/admin2028/login/',
    '/admin2028/index.php',
    '/admin2028/index/',
    '/admin2028/home.php',
    '/admin2028/home/',
    '/admin2028/control/',
    '/admin2028/account.php',
    '/admin2028/account/',
    '/admin2028/admin.php',
    '/admin2028/admin/',
    '/admin2029/login.php',
    '/admin2029/login/',
    '/admin2029/index.php',
    '/admin2029/index/',
    '/admin2029/home.php',
    '/admin2029/home/',
    '/admin2029/control/',
    '/admin2029/account.php',
    '/admin2029/account/',
    '/admin2029/admin.php',
    '/admin2029/admin/',
    '/adminportal/login.php',
    '/adminportal/login/',
    '/adminportal/index.php',
    '/adminportal/index/',
    '/adminportal/home.php',
    '/adminportal/home/',
    '/adminportal/control/',
    '/adminportal/account.php',
    '/adminportal/account/',
    '/adminportal/admin.php',
    '/adminportal/admin/',
    '/adminpage/login.php',
    '/adminpage/login/',
    '/adminpage/index.php',
    '/adminpage/index/',
    '/adminpage/home.php',
    '/adminpage/home/',
    '/adminpage/control/',
    '/adminpage/account.php',
    '/adminpage/account/',
    '/adminpage/admin.php',
    '/adminpage/admin/',
    '/admincontrol/login.php',
    '/admincontrol/login/',
    '/admincontrol/index.php',
    '/admincontrol/index/',
    '/admincontrol/home.php',
    '/admincontrol/home/',
    '/admincontrol/control/',
    '/admincontrol/account.php',
    '/admincontrol/account/',
    '/admincontrol/admin.php',
    '/admincontrol/admin/',
    '/adminweb/login.php',
    '/adminweb/login/',
    '/adminweb/index.php',
    '/adminweb/index/',
    '/adminweb/home.php',
    '/adminweb/home/',
    '/adminweb/control/',
    '/adminweb/account.php',
    '/adminweb/account/',
    '/adminweb/admin.php',
    '/adminweb/admin/',
    '/adminsite/login.php',
    '/adminsite/login/'
]
#======== paths ======#

# Coded By Salfi Hacker

#======== clear ======#
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
#======== clear ======#

#Coded By Salfi Hacker

#======== Intro ======#
def __salfi__():
    clear()
    first_banner()
    print(f"""
{red}[#]{green} Follow me :
{cyan}[1] {green}Telegram Channel
{cyan}[2] {green}Instagram
{cyan}[3] {green}WhatsApp Channel
{cyan}[4] {green}Back Home
{cyan}[0] {green}Exit""")
    try:
        dev_ = input("\033[31m╔═══[\033[32mChoose A Number\033[31m]\n\033[31m╚══》 \033[32m")
        if dev_ =="1":
            webbrowser.open("https://t.me/cyberfantics")
            main()
        elif dev_ =="2":
            webbrowser.open("https://instagram.com/cyberfantics")
            main()
        elif dev_ =="3":
            webbrowser.open("https://whatsapp.com/channel/0029VaFE5Dv5Ejy2MaydYm3Z")
            main()
        elif dev_ =="4":
            main()
        elif dev_=="0":
            os.system("exit")
        else:
            main()
    except:
    	first_banner()
    	print(f'''
{red}==============================
	{green}Error Info:
{red}==============================''')
    	print(f'{red}\t[!] {green}Exited Due To {cyan} Keyboard Intereption{cyan}.{green}{ramadi}\n')
#======== Intro ======#
        
# Coded By Salfi Hacker

#======== Info ======#
def info():
    print(f"""
{green}============================
{red}[+] {green}Coded By @SalfiHacker
{red}[+] {green}Gift From Cyber Fantics
{red}[+] {green}Use It To Find {red}Admin Page{green} Of Sites
{green}============================""")

#======== Info ======#
        
# Coded By Salfi Hacker

#======== first banner of cyber fantics ======#
def first_banner():
    clear()
    salfi = pyfiglet.Figlet(font="slant")
    banner = salfi.renderText("Cyber Fantics")
    print(f'{red}{banner}')
    #======== first banner of cyber fantics ======#

# Coded By Salfi Hacker

#======== logo ======#
def adminPageLogo():
    clear()
    print(f"""\033[0;96m
░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ░██╗░░░░░░░██╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ░██║░░██╗░░██║██╔══██╗{red}
███████║██║░░██║██╔████╔██║██║██╔██╗██║  ░╚██╗████╗██╔╝██████╔╝
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ░░████╔═████║░██╔═══╝░
{green}██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ░░╚██╔╝░╚██╔╝░██║░░░░░
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚═╝░░╚═╝░░░░░
            {red}Channel Telegram :{cyan} {hell}@cyberfantics{labyadh}
""")
#======== logo ======#

# Coded By Salfi Hacker

#======== Input URL ======#
def getUrl():
    adminPageLogo()
    try:
        url = input(f"\033[90m╔═══{red}[root{green}@CyberFantics{red}]\n╚══>>>   \033[32m{cyan}")
        return url
    except:
    	first_banner()
    	print(f'''{red}=======================
	{green}Error Info:
{red}=======================''')
    	print(f'{red}\t[!] {green}Exited Due To {cyan} Keyboard Intereption.')
    	time.sleep(1)
#======== Input URL ======

##======== Input PATH 
def getPath():
    adminPageLogo()
    try:
        path = input(f"\033[90m╔═══{red}[root{green}@CyberFantics{red}]\n╚══>>>   \033[32m{cyan}")
        return path
    except KeyboardInterrupt:
        first_banner()
        print(f'''{red}=======================
    {green}Error Info:
{red}=======================''')
        print(f'{red}\t[!] {green}Exited Due To {cyan}Keyboard Interruption.')
        time.sleep(1)

#======== Input PATH ======#

# Coded By Salfi Hacker

# ======== Find Url ======#
def find_url(url):
    global count
    first_banner()
    print(f'''{green}=============================================================

     {cyan}Cyber Fantics Trying To Find Your {red}{hell}Admin Page{labyadh} {cyan}Urls:

{green}=============================================================\n''')
    if count > 0:
        print(f'''{red}====================================================================
{hell}[-]{labyadh} {green}We are going to target {cyan}{hell}{count}{labyadh} {green}url, which is{cyan}{hell} {url}{labyadh}
{red}====================================================================\n''')
        count += 1
    for inn in lists:
        try:
            target_url = f"{url}{inn}"
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"{red}\t{hell}[+]{labyadh} {green}{url}{inn} {red}==>{cyan} Found")
                salfi = open("sites.txt", "a")
                salfi.write(f"{red}[-] {cyan}Ok {red}:{green} {url}{inn}\n")
                salfi.close()
                print(f"{red}\t{hell}[!]{labyadh} {cyan}Save The Site File Name {red}==:> {green}sites.txt")
                time.sleep(3)
                break
            else:
                print(f"\t{hell}{red}[-]{labyadh} {green}{url}{inn}{cyan} ==> {hell}{red}Not Found{labyadh}")

        except:
            clear()
            adminPageLogo()
            print(f'''
{cyan}Error Status{green}:''')
            print(f"{red}\t[-] {green}Error The Site {red}https://{green} or {red}http://")
            print(f"\t{red}[-] {green}Exit write {red}(e) {green}restart write {red}(y){green} ?")
            slact = input(f'\t{red}[+] {cyan}')
            if slact.lower() == "y":
                os.system("python admin.py")
            elif slact.lower() == 'e':
                print(f"{red}\t[!]{cyan}Exit Now{green} ...")
                sys.exit()
            else:
                main()
# ======== Find Url ======#

# Coded By Salfi Hacker

#======== Find Url In List ======#

# Coded By Salfi Hacker

def adminFromList(path):
    global count
    count = 1
    try:
        with open(path,'r') as file:
            for url in file:
                find_url(url.strip())
    except FileNotFoundError:
        first_banner()
        print(f'''{red}=======================
    {green}Error Info:
{red}=======================''')
        print(f'{red}[!] {green}File Not Found {cyan} Try Again.')
        time.sleep(2)
        adminFromList(getPath())
        

#======== Find Url In List ======#

#======== main ======#
def main():
    first_banner()
    info()
    option = input(f"""
    {green}[1] {red}Enter 1 For Finding Through Url
    {green}[2] {red}Enter 2 For Finding Through File
    {green}[3] {red}Enter 2 For About
    {green}[4] {red}Enter 3 For Exit {cyan}
    
    {red}[-] {cyan}""")
    
    if option == '1' or option == '01':
    	find_url(getUrl())
    elif option == '2' or option == '02':
    	adminFromList(getPath())
    elif option == '3' or option == '03':
    	__salfi__()
    elif option == '4' or option == '04':
    	sys.exit()
    else:
    	main()
#======== main ======#

# Coded By Salfi Hacker
if __name__ == '__main__':
	main()
