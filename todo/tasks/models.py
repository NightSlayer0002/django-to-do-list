from django.db import models

# Create your models here.

class Task(models.Model):  # create a model called task
    title = models.CharField(max_length=200)  # name of the task as title
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
