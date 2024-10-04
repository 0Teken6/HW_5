from django.db import models
from django.contrib.auth.models import User
import random


class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='conf_code')
    code = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_code()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_code(cls):
        return random.randint(100000, 999999)

    def __str__(self):
        return str(self.code)