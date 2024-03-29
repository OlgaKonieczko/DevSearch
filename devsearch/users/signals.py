from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        subject = 'Welcome to devSearch'
        body = 'Your account was created. Thank you for joining.'
        send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,
                    [profile.email],
                    fail_silently=False,
                )

def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user=profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)    