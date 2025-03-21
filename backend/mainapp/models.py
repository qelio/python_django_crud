from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)
    birth_date = models.DateField(null=True)
    nationality = models.CharField(max_length=150, null=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

