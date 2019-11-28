from django.db import models


# Create your models here.

class HanreiPost(models.Model):
    court_name = models.CharField(max_length=30)
    case_number = models.CharField(max_length=30)
    date = models.DateField()
    case_name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    x_attorney_name = models.CharField(max_length=30)
    y_attorney_name = models.CharField(max_length=30)
    judge_name = models.CharField(max_length=30)
    text = models.TextField()
    judgement = models.FileField(
        upload_to="uploads/%Y/%m/%d/",
    )

    def __str__(self):
        return self.text


class Shrine(models.Model):
    name = models.CharField(max_length=200)
    locate = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    photo = models.FileField(
        upload_to="uploads/%Y/%m/%d",
    )

    def __str__(self):
        return self.name
