import json
import config

channelID,serverID,targetID = config.getScope()
daTestDoc = open("TestDoc","r",encoding="utf-8")
inputList = open("inputList","w",encoding="utf-8")
messageDict = {}
daMessageList = eval(daTestDoc.read())
for message in daMessageList:
	if message["author"]["id"] == targetID:
		if message.get("message_reference") != None:
			print(message["referenced_message"])
			message["referenced_message"]["content"]
		else:
			print("is not reply")
daTestDoc.close()
