# --coding-- utf-8

import socket
import re

irc_host = "irc.libera.chat"
irc_port = 6667
irc_chan = "##huan"#,#tuna

bot_name = "huanbot"
usr_name = "huan_bot"
ral_name = "HuanRobot"

irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc_sock.connect((irc_host, irc_port))


irc_sock.send(("NICK " + bot_name + "\r\n").encode())
irc_sock.send(("USER " + bot_name + " " + bot_name + " " + usr_name + " :" + ral_name + "\r\n").encode())
irc_sock.send(("JOIN " + irc_chan + "\r\n").encode())


while True:
	data = irc_sock.makefile(encoding='utf-8')
	for line in data:
		if (("libera.chat" in line) and ("ChanServ" in line) and ("services" in line)):
			
			print(line.encode('utf-8').decode())
			
		elif ("hello" in line):
			print(line.encode('utf-8').decode())
			hello = bytes("hello","utf-8")
			a = "PRIVMSG " + "##huan" + " :"  + "hello\r\n"
			a = a.encode("utf-8")
			irc_sock.send(a)
			print("[robot] hello")
		elif ("Ping timeout" in line):
			irc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			irc_sock.connect((irc_host, irc_port))
			irc_sock.send(("NICK " + bot_name + "\r\n").encode())
			irc_sock.send(("USER " + bot_name + " " + bot_name + " " + usr_name + " :" + ral_name + "\r\n").encode())
			irc_sock.send(("JOIN " + irc_chan + "\r\n").encode())
		else:
			print(line.encode('utf-8').decode())
