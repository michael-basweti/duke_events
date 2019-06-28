from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField()
    user_description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name