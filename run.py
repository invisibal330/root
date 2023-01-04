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
#_________[ TOOL MAIN MENU ]________#
def main():
	banner()
	exit("Hellow World")


if __name__=="__main__":
	main()
