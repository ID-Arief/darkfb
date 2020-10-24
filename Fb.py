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
