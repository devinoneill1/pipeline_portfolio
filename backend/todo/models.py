from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    createdDTF = models.DateField(auto_now_add=True)
    completedDTF = models.DateField(blank=True, null=True)

    def _str_(self):
        return self.title