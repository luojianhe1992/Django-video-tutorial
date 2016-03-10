from __future__ import unicode_literals

from django.db import models


from django.contrib.auth.models import User

# Create your models here.



class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=1000)
    body = models.TextField(max_length=10000)
    date_created = models.DateField(auto_now_add=True)
    date_changed = models.DateField(auto_now=True)
    like = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s %s" %(self.user, self.title)



