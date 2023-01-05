#creater: 
#toolname: root
#toolveraion: 0.0.1

#_________[ IMPORTING MODULES ]__________#
from data.modules import *
#_________[ IMPORTING COLORS ]__________#
from data.colour import *
#_________[ IMPORTING LOGO ]________#
try:
	logo = open("data/logo.txt","r").read()
except FileNotFoundError:
	exit("[+] Logo not found")
#_________[ IMPORTING INFO ]________#
from data.toolinfo import tool_name
from data.toolinfo import tool_version
from data.toolinfo import tool_github
#_________[ TOOL SERVER ]________#
from server.server import securitychack
from server.server import updatechack
from server.server import mainchack
#_________[ TOOL BANNER ]________#
def banner():
	cmd("clear")
	print(logo)
	print("-"*50)
	print(f"   [{green}+{white}] Tool : {rad}{tool_name}{white}")
	print(f"   [{green}+{white}] Version : {tool_version}")
	print(f"   [{green}+{white}] GitHub : {tool_github}")
	print("-"*50)
#_________[ UPLOAD FILE ]________>>
def upload_file(cmdID):
	if len(cmdID)==3:
		if cmdID[0]=="file_upload" and cmdID[1]=="-f":
			try:
				file = cmdID[2]
				open(file,"r").read()
			except FileNotFoundError:
				print("\n\tFile Not Found.. \n")
			try:
				api_endpoint = "https://file.io"
				file_to_upload = {"file": open(file, "rb")}
				response = post(api_endpoint, files=file_to_upload)
				print("----------------------------------------------")
				print(" [*] Upload Status: "+str(response.json()['status']))
				print(" [*] Upload ID: "+str(response.json()['id']))
				print(" [*] Upload Key: "+str(response.json()['key']))
				print(" [*] NodeType: "+str(response.json()['nodeType']))
				print(" [*] File Name: "+str(response.json()['name']))
				print(" [*] File Size: "+str(response.json()['size'])+"KB")
				print(" [*] File Link: "+str(response.json()['link']))
				print(" [*] File Created: "+str(response.json()['created']))
				print(" [*] Link Expire Date: "+str(response.json()['expires']))
				print(" [*] File Download: "+str(response.json()['downloads']))
				print("----------------------------------------------")
			except:
				print("\n\terror in uploading\n")
#___________[ WEB HEADER ]__________>>
def web_header(cmdID):
	try:
		if cmdID[0] in ["website_header","web_header"]:
			if cmdID[1] == "-w":
				url = cmdID[2]
				response = get(url)
				headers = dict(response.headers)
				print("----------------------------------------")
				for key, value in headers.items():
					print(key, value)
				print("----------------------------------------")
	except:
		print("website_header -w https://example.com")
#_________[ TOOL MAIN MENU ]________#
def main():
	banner()
	while True:
		"ID" == "IDX"
		usr_cmd = input("\n[->] Input your command: ")
		usr_cmdx = usr_cmd.split(" ")
		if usr_cmd in ["ls","clear"]:
			print("")
			cmd(usr_cmd)
		elif usr_cmdx[0]=="file_upload":
			upload_file(usr_cmdx)
		elif usr_cmdx[0] in ["website_header","web_header"]:
			web_header(usr_cmdx)
		else:
			slp(0.2)
			print(f"\n\t {rad}Command not found..{white}")
if __name__=="__main__":
	main()
