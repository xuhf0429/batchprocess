from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import HttpResponse
import requests
import json
from django.core import serializers
from models import UserModel, SessionModel, ActionModel


def users(request, userid):

    json_userlist = []
    users = UserModel.objects.get(userid = userid)
    
    with open("user.json","w") as output:
        

        for user in users:
            action = ActionModel.objects.get(userid=userID)
            action_dict = {
                "time":str(datetime.now()),
                "type":action.type
            }
            user_dict = {
                "userId":user.userid,
                "sessionId":user.sessionid,
                "actions":action_dict
            }
            
            json_userlist.append(user_dict)
            json.dump(json_userlist, output)
    
   # return HttpResponse(json.dumps(json_userlist))

