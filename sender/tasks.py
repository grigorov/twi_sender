from __future__ import absolute_import
from celery import shared_task
import tweepy

@shared_task
def add(x, y):
    return x + y
@shared_task
def follow_all(source, destination):
        source_auth = tweepy.OAuthHandler(source.consumer_key, source.consumer_secret)
        source_auth.set_access_token(source.access_token, source.access_token_secret)
        destination_auth = tweepy.OAuthHandler(destination.consumer_key, destination.consumer_secret)
        destination_auth.set_access_token(destination.access_token, destination.access_token_secret)
        try:
            source_api = tweepy.API(source_auth)
            destination_api = tweepy.API(destination_auth)
            if not source_api.lookup_friendships(destination_api.followers_ids()):
                   source_api.create_friendship(destination_api.followers_ids)
#            for follower in tweepy.Cursor(api.followers).items():
#                follower.follow()
            return True
        except tweepy.TweepError as e:
            print(e)

@shared_task
def retweet(id_status, destination):
    destination_auth = tweepy.OAuthHandler(destination.consumer_key, destination.consumer_secret)
    destination_auth.set_access_token(destination.access_token, destination.access_token_secret)
    try:
        destination_api = tweepy.API(destination_auth)
        destination_api.retweet(id_status)
    except tweepy.TweepError as e:
        print(e)
@shared_task
def mass_retweet(objects, id_status):
    for obj in objects:
        retweet.delay(id_status=id_status, destination=obj)
