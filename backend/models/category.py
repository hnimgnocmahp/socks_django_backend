from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    