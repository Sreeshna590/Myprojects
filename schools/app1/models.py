from django.db import models

# Create your models here.
from django.db import models  # Use models from django.db, not django.shortcuts

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=30)
    principal = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()  # Corrected from `integerField` to `IntegerField` and removed `max_length`
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")  # Fixed `Foreignkey` to `ForeignKey` and corrected `related-name` to `related_name`

    def __str__(self):
        return self.name
