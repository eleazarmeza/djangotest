
from django.db import models

# campos de mis tablas modelados con clases
# no escribo SQL, el ORM convierte a SQL

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #que pasa si se borra un question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)