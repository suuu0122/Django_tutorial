import datetime

from django.contrib import admin
"""https://docs.djangoproject.com/ja/4.2/ref/models/instances/#django.db.models.Model"""
from django.db import models
"""https://docs.djangoproject.com/ja/4.2/ref/utils/#module-django.utils.timezone"""
from django.utils import timezone



class Question(models.Model):
    """https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.CharField"""
    question_text = models.CharField(max_length=200)
    """https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.DateTimeField"""
    pub_date = models.DateTimeField("date published")
    

    def __str__(self):
        return self.question_text
    
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now



class Choice(models.Model):
    """https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.ForeignKey"""
    """
    ForeignKeyを使用してリレーションシップを定義
		それぞれのChoiceが1つのQuestionに関連付けられることをDjangoに伝える.
        Djangoは、多対一、多対多、そして一対一のような一般的なデータベースリレーションシップすべてをサポートする.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

    def __str__(self):
        return self.choice_text