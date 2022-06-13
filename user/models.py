from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.
class User(models.Model):
    class GenderChoice(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        NONBINARY = "Non-binary"
        UNDISCLOSED = "Prefer not to say"

    username = models.CharField(max_length = 10, unique = True, blank = False, null = False)
    firstname = models.CharField(max_length = 20, blank = False, null = False)
    lastname = models.CharField(max_length = 20, blank = False, null = False)
    telephone = PhoneNumberField(blank = False, null = False)
    gender = models.CharField(max_length = 20, choices = GenderChoice.choices, blank = False, null = False)
    country = CountryField(blank = False, null = False)
    state = models.CharField(max_length = 20, blank = False, null = False)
    email = models.EmailField(max_length = 20, blank = False, null = False)
    password = models.CharField(max_length = 32, blank = False, null = False)

class Contact(models.Model):
    username = models.CharField(max_length = 10, unique = True, blank = False, null = False)
    email = models.EmailField(max_length = 20, blank = False, null = False)
    message = models.TextField(blank = False, null = False)