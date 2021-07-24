import socket
import subprocess
from subprocess import PIPE


def getIP():
	try:
	    res = subprocess.check_output('ifconfig')
	except:
	    print("Error.")

	return str(res).split("eth0:")[1].split("inet ")[1].split(" ")[0]



def getIPandsendIP():
	HOST = '192.168.127.130'
	PORT = 9998

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))

	client.send(getIP().encode("utf-8"))
	response = client.recv(4096)
	print(response.decode('utf-8'))

	client.close()

def buildSSH():
	res = subprocess.run("sudo systemctl start ssh", shell=True, stdout=PIPE, stderr=PIPE, text=True)


if __name__=="__main__":
	getIPandsendIP()
	buildSSH()