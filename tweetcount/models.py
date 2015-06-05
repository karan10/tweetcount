from django.db import models

# Create your models here.

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):              
        return self.tweet_text


class User(models.Model):
    screen_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    followers = models.IntegerField(default=0)

    def __unicode__(self):
        return self.screen_name