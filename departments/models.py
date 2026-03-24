from django.db import models
from users.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 'MANAGER'}
    )

    def __str__(self):
        return self.name
