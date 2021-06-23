import json
import discAutoMsg.discord_automessage as discAutoMsg
import config
import pickle
channelID, serverID, targetID = config.getScope()
daTestDoc = discAutoMsg.exportMessages(channelID)

daTestDoc = pickle.load(daTestDoc.name,"r",encoding="utf-8")
print(len(eval(daTestDoc.read())))
daTestDoc.close()