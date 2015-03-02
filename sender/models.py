from django.db import models
import tweepy

# Create your models here.
class TwitterAccount(models.Model):
    name = models.CharField(verbose_name="Twitter Name/Nick",help_text="Твиттер имя",max_length=250,editable=False)
    id_twitter = models.IntegerField(unique=True, editable=False)
    consumer_key = models.CharField(verbose_name="Consumer key",help_text="dev.twitter.com/app необходимо получить ключи",max_length=250)
    consumer_secret = models.CharField(verbose_name="Consumer secret",max_length=250)
    access_token = models.CharField(verbose_name="Access token",max_length=250)
    access_token_secret = models.CharField(verbose_name="Access token Secret",max_length=250)
    active = models.BooleanField(default=False,editable=False)

    def __unicode__(self):
        return self.name
   
    def save(self, *args, **kwargs):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        try:
            api = tweepy.API(auth)
            if api.verify_credentials():
                me = api.me()
                self.id_twitter = me.id
                self.active = True
                self.name = me.screen_name
                super(TwitterAccount, self).save(*args, **kwargs)
        except tweepy.TweepError as e:
            print(e)


