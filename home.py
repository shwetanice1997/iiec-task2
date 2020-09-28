#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

x = mydata.getvalue("c")


o = subprocess.getoutput("sudo " + x)

print("Command Run : ",x)

print("<br />")
print("<br />")

print("*****************************************************************************************************************************************************************************************************")
print("<br />")
print("<br />")

print("Output is:",o)
