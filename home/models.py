from django.db import models

# Create your models here.
class ToDoList(models.Model):
    titletext = models.TextField(max_length=50)
    textdiscrip = models.TextField()
    time= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titletext