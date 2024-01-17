import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        current_time = timezone.now()
        return current_time - datetime.timedelta(days=1) <= self.pub_date <= current_time
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text