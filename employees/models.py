from django.db import models
from users.models import User
from departments.models import Department

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name='employees')
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.designation}"
