import json
import config
import random

channelID,serverID,targetID = config.getScope()
daTestDoc = open("TestDoc","r",encoding="utf-8")
inputListDoc = open("inputList","w",encoding="utf-8")
outputListDoc = open("outputList","w",encoding="utf-8")
inputList = []
outputList = []
messageDict = {}
daMessageList = eval(daTestDoc.read())
print(len(daMessageList))
for i in range(len(daMessageList)):
	message = daMessageList[i]
	if message["author"]["id"] == str(targetID):
		if type(message.get("referenced_message"))!=dict:
			print("not a reply")
			print(i)
			print(len(daMessageList))
			if len(daMessageList) != i:
				outputList.append(message["content"])
				message = daMessageList[i+1]
				inputList.append(message["content"])
			else:
				pass
		else:
			print(type(message.get("referenced_message")))
			print(message.get("referenced_message"))
			inputList.append(message["referenced_message"]["content"])
			outputList.append(message["content"])

print(len(outputList))
print(len(inputList))
myIndice = random.randint(0,len(inputList))
print(myIndice)
print("input: "+ inputList[myIndice])
print("output: "+ outputList[myIndice])

inputListDoc.write(str(inputList),"utf-8")
outputListDoc.write(str(inputList),"utf-8")

daTestDoc.close()
inputListDoc.close()
outputListDoc.close()