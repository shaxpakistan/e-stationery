from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user                = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_picture     = models.ImageField(upload_to = "profile/", null = True, blank = True)
    date_of_birth       = models.DateField(null=True, blank=True)
    phone_number        = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("profile")

# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender = User)
# def save_user_profile(sender,  instance, created, **kwargs):
#     instance.userprofile.save()