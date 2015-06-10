# By Karan Dev

from django.db import models

# Create your models here.


class User_n(models.Model):
    screen_name = models.CharField(max_length=200)  # screen_name is the twitter's username
    user_name = models.CharField(max_length=200)    # user_name is the real name
    followers = models.IntegerField(default=0)      # extra field

    def __unicode__(self):
        return self.screen_name

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)   # tweet
    screen_name = models.ForeignKey(User_n)
    source = models.CharField(max_length=200)       # extra field

    def __unicode__(self):              
        return self.tweet_text


    