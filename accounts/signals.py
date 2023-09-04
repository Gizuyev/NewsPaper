from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from main.models import Author

@receiver(post_save, sender=CustomUser)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        instance.save()
        print('Author created')