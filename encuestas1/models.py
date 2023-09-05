from django.db import models

# Create your models here.


class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.text


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text
