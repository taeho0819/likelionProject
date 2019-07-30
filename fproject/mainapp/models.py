from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
# title 변수에 models안에 있는 char타입으로 정의하겠다.
    pub_date=models.DateTimeField('date published')
    body = models.TextField(default='SOME STRING')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] # 본문내용을 리턴
