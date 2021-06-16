import json
import discAutoMsg.discord_automessage as discAutoMsg
import config
channelID, serverID, targetID = config.getScope()
# trainingData = open("Training_Data","w")
daChannel = discAutoMsg.searchMessages(serverID,False,channel_id=channelID)
#daChannel = discAutoMsg.searchMessages(channelID,True)#this is for dm
totalResults = json.loads(daChannel)["total_results"]
print(totalResults)
daTestDoc = discAutoMsg.exportMessages(channelID)
daTestDoc = open(daTestDoc.name,"r",encoding="utf-8")
print(len(eval(daTestDoc.read())))
daTestDoc.close()