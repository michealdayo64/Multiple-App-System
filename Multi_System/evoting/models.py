from django.db import models
from account.models import CustomUser
# Create your models here.


class CandidateCategory(models.Model):
    name = models.CharField(default = False, max_length = 30)
    user = models.ManyToManyField(CustomUser, null = True, blank = True, related_name = 'user')
    user_voted = models.ManyToManyField(CustomUser, null = True, blank = True, related_name = 'user_voted')

    def __str__(self):
        return self.name