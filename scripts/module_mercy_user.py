#!/bin/python3
import subprocess
import sys
import module_database

def check_status(tg):

        example = module_database.get("select time from users where tg="+str(tg))
        example = ''.join(example).split("\n")
        return example

def change_status(tg):
        result = module_database.change("update users set time = \"0\" where tg = "+str(tg)) 

#Get ip from telergram id account
def get_ip(tg):
        try:
                example = module_database.get("select ip from users where tg="+str(tg))
                list_ip = ''.join(example).split("\n")
                return(list_ip)

        except:
#               print("Database error")
                sys.exit()

#Use ip for block user by ip
def mercy_user(list_ip):
        try:
                for ip in list_ip:
                        subprocess.check_output("iptables -D FORWARD -s " + ip + " -j REJECT", shell=True)
                        #print("iptables -A FORWARD -s", ip, "-j REJECT")
        except:
#               print("Iptables error")
                sys.exit()
#Return successful code

def by_tg(tg):
        if str(check_status(tg)[0]) == "2":
                mercy_user(get_ip(tg))
                change_status(tg)
                return 0
        else:
                return 1
