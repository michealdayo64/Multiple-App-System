from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


class CustomUser(AbstractUser):
    user_type_data = (
        ("1", "ADMIN"),
        ("2", "CANDIDATES"),
        ("3", "VOTERS")
    )
    user_type = models.CharField(default = "1", choices = user_type_data, max_length = 10)
    phone_no = models.PositiveIntegerField(default = False, validators=[MaxValueValidator(99999999999999999)])
    image = models.ImageField(upload_to = 'media/', default = False, blank = True)
    vote_count = models.PositiveIntegerField(default = 0)
    #is_voted = models.BooleanField(default = False)
    account_updated = models.BooleanField(default = False)

    
    
