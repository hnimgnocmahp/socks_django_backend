from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=20)  # S, M, L hoặc 35-37, 38-40
    description = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
