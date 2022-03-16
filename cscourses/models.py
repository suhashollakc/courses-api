from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 200)
    professor = models.CharField(max_length = 300)
    code = models.CharField(max_length = 10)

    def __str__(self):
        return self.name