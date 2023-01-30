import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class Message(models.Model):
    message = models.CharField(max_length=160)
    user = models.CharField(max_length=30)
    date_time = models.DateTimeField('date published', default=datetime.datetime.now)

    def __str__(self):
        return self.message

    def was_published_recently(self):
        return self.date_time >= timezone.now() - datetime.timedelta(days=1)