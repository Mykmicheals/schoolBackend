from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from app.models import Teacher

@receiver(post_save, sender=CustomUser)
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.is_teacher:
        Teacher.objects.create(user=instance)