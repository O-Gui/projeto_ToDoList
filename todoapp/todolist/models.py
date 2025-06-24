from django.db import models

# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=200)
    isCompleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.isCompleted) + '|' + self.created_at.strftime('%d/%m/%Y') 
    