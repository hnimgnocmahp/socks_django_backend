from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # tự động cập nhật khi cập nhật model

    def __str__(self):
        return self.full_name
