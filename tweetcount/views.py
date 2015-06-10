from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet, User_n
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from django.db.models import Count
from django.template import RequestContext
from django.shortcuts import render_to_response


ckey = ''
csecret = ''
atoken = ''
asecret = ''

class listener(StreamListener):

	def on_data(self, data):
		print data
		data = json.loads(data)
		try:
			sname = data['user']['screen_name']
			name = data['user']['name']
			fcount = data['user']['followers_count']
		except:
			return False
		if sname and name and fcount:
			c1 = User_n(screen_name=sname, user_name=name, followers=fcount)
		else:
			return False
		c1.save()
		try:
			src =data['source']
			ttext = data['text']
		except:
			return False
		if ttext and src:
			c2 = Tweet(id=None, tweet_text=ttext, screen_name=c1, source=src)
		else:
			return False
		c2.save()
		print "done"
		return True

	def on_error(self, status):
		print status


def index(request):
	context = RequestContext(request)
	if request.method == 'POST':
		search = request.POST['search']
		total_tweets = len(Tweet.objects.filter(tweet_text__contains='#'+search))
		total_users = len(Tweet.objects.values("screen_name__screen_name").filter(tweet_text__contains='#'+search).distinct())
		max_tweet_user_all = Tweet.objects.filter(tweet_text__icontains='#'+search).values('screen_name__screen_name').annotate(Count("screen_name__screen_name")).order_by('-screen_name__screen_name__count')
		try:
			max_tweet_user = max_tweet_user_all[0]['screen_name__screen_name']
			context_dict = {'total_tweets':total_tweets, 'total_users':total_users, 'max_tweet_user':max_tweet_user}
		except:
			context_dict = {'total_tweets':0, 'total_users':0, 'max_tweet_user':0}
		return render(request, 'tweetcount/index.html', context_dict)
	else:
		return render_to_response('tweetcount/index.html', {}, context)


def get_tweet(request):
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	twitterStream = Stream(auth, listener())
	twitterStream.filter(locations=[-180,-90,180,90])
	return HttpResponse("All tweets saved")
