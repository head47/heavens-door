#!/bin/python3
import subprocess
import os
import module_add_user

database_name = "origin"

#Create first table and add here zero user
def create_table_users(path):
        command = "sqlite3 " + path + " 'create table users (id int, name string, ip string, time int, tg string)'"
        #print(command)
        subprocess.check_output(command, shell=True)

#Create second table and add here zero user
def create_table_time(path):
        command = "sqlite3 " + path + " 'create table time (id int, ip string, hours int, minutes int)'"
        #print(command)
        subprocess.check_output(command, shell=True)

#Path for creating database
def create_path():
        global database_name
        return '/'.join(os.path.abspath(os.curdir).split("/"))+"/database/" + database_name

#Add zero user
#def add_zero_user(path):
#       module_add_user.add("admin:10.10.10.10:111111")

#Main function
def create():
        path = create_path()
#       print(path)
        create_table_users(path)
        create_table_time(path)
#add_zero_user(path)
#dir = '/'.join(os.path.abspath(os.curdir).split("/")[:-1])+"/database/"
