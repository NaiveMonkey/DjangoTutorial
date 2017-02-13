from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    # ForeignKey: 다른 모델에 대한 링크
    author = models.ForeignKey('auth.User')

    # CharField: 글자 수가 제한된 텍스트 정의
    title = models.CharField(max_length=200)
    # TextField: 글자 수 제한이 x
    text = models.TextField()

    created_date = models.DateTimeField(
        default=timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
