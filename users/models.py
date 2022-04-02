from django.db import models

class SessionModel(models.Model):
    
    sessionid = models.TextField(max_length=200)

class UserModel(models.Model):

   # def user(model, userid):

    userid = models.TextField(blank=False)
    sessionid = models.ForeignKey(SessionModel, on_delete=models.CASCADE)

    def __str__(self):

        return self.userid
    
class ActionModel(models.Model):
    
    userID = models.ForeignKey(user, on_delete=models.CASCADE)
    type = models.TextField(blank=False)
    
    
    
#model
