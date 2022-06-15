from django.db import models


class NewPerson(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    work_experience = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name