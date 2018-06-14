#!/usr/bin/python3
import subprocess,sys

def main():
	menu()

def menu():
	ruleDump()
	print("")
	print("Options:")
	# Ingress
	print(appliedBox(ruleMatch(I1)) + "I1) Only Allow Incoming Traffic (Very Restrictive)")
	# Egress
	print("E1) Only Allow Top 10,000 Sites (Somewhat Restrictive)")
	print("E2) Only Allow 53,80,443 OUT")
	# Block Actions
	print(appliedBox(ruleMatch(B1)) + "B1) Block Domain Transfers")
	print(appliedBox(ruleMatch(B2)) + "B2) Block ICMP")

	option = input("Selection: ")
	warning()
	setRule(I1) #Temp

def warning():
	print("This might effect your access to the internet")
	warning = input("Continue?(y/N) ")
	if warning.lower() == "y":
		#rules()
		print("Applying Rules...")
	elif warning.lower() == "n":
		sys.exit()
	elif warning == "":
		sys.exit()
	else:
		print("unknown input")

## Rules
#I1 = ['''-A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT''','''-A OUTPUT -j REJECT''']
I1 = ['''ufw-not-local -j DROP'''] #For testing purposes
B1 = ['''-A INPUT -p tcp --dport 53 -j DROP''']
B2 = ['''-A INPUT -p icmp -j REJECT --reject-with icmp-port-unreachable''']



def setRule(ruleID):
	for i in ruleID:
		print("/sbin/iptables "+i)
	#cmd("iptables -A OUTPUT -m state --state RELATED,ESTABLISHED -j ACCEPT") # Allow initiated connections out
	#cmd("iptables -A OUTPUT -j REJECT") # Drop all other traffic
	#print("applied")

## Check if Rules are Applied 
def ruleMatch(ruleArray):
	for lineRule in ruleArray:
		if lineMatch(lineRule) == False:
			return False
	return True

def lineMatch(lineRule):
	matchedLine = False
	with open("/tmp/current.rules") as f:
			for line in f:
				if lineRule == "-A "+line.rstrip():
					matchedLine = True
	return matchedLine

def ruleDump():
	cmd("iptables-save > /tmp/current.rules")

def appliedBox(ruleBool):
	if ruleBool == True:
		return "[x] "
	elif ruleBool == False:
		return "[ ] "
	else:
		return "err "

# I'm lazy
def cmd(command):
	subprocess.run(command, shell=True, check=True)

main()

