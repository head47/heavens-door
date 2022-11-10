#!/bin/python3
import sys

#Import modules
try:
        import os
        base_dir = os.path.dirname(__file__) or '.'
        dir_scripts = os.path.join(base_dir, 'scripts')
        sys.path.append(dir_scripts)
except:
        print("Error: cannot import modules")
        sys.exit()

#Install sqlite3
#import subprocess
#subprocess.check_output("apt install sqlite3", shell=True)

#Create database
try:
        import module_create_database
        module_create_database.create()
except:
        print("Error: cannot create database")
        sys.exit()

#Create admin user
try:
        import module_add_admin
        name = input("What is your admin name? ")
        ip = input("What is your admin ip? ")
        tg = input("What is your admin Telegram id? ")

        module_add_admin.add(name+":"+ip+":"+tg)
except:
        print("Error: cannot create admin")
        sys.exit()

print("Installation completed")
