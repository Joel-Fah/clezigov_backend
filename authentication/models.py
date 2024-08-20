from django.db import models
from django.contrib.auth.models import User
from core.models import Category


class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    class Occupations(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'

    class Genders(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, choices=Occupations.choices, blank=True, null=True)
    gender = models.CharField(max_length=255, choices=Genders.choices, blank=True, null=True)
    interests = models.ManyToManyField(Category, related_name='interested_profiles', blank=True)

    @property
    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "media/avatars/pfp.jpg"

    def __str__(self):
        return f'{self.user.first_name}: {self.user.email}'
