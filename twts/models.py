"""
DJANGO 3.0.3
PYTHON 3.7.0
BOOTSTRAP 3.4.1
"""




import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class TwtPoster(models.Model):
    # this is a de facto user model, which has the attributes of email and password.
    twtposter_text = models.CharField('twtposter username/email', max_length=200, default="emptyuser")
    twtposter_password = models.CharField('twtposter password', max_length=200, default="emptypassword")

    def __str__(self):
        return self.twtposter_text


class Twt(models.Model):
    twt_text = models.CharField('twt text', max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    twtposter = models.ForeignKey(TwtPoster,on_delete=models.CASCADE) # this connects every individual twt to a TwtPoster user

    def __str__(self):
        return self.twt_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Reply(models.Model):
    twt = models.ForeignKey(Twt,on_delete=models.CASCADE) # related to a twt
    reply_poster = models.ForeignKey(TwtPoster,on_delete=models.CASCADE) # related to twtposter
    reply_text = models.CharField('twt text', max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return self.reply_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
