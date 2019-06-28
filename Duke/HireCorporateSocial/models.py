from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class HireCorporate(models.Model):
    SERVICE = (
        ('corporate', 'corporate'),
        ('social','social')
    )
    applicant_name = models.CharField(max_length=100, blank=False, null=False)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=100, blank=False, null=False)
    service = models.CharField(choices=SERVICE, max_length=20)
    application_description = models.TextField(max_length=500, default='Your application', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.applicant_name