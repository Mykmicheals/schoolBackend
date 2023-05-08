from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, StudentSubject, Subjects



@receiver(post_save, sender=Subjects)
def link_subject_to_students(sender, instance, created, **kwargs):

    if created:        
        try:
            students = Student.objects.filter(
                user__classroom=instance.class_offered)
            for student in students:
                StudentSubject.objects.create(
                    student=student, subject=instance)

        except Exception as e:
            print(
                f"An error occurred while creating StudentSubject instances: {str(e)}")
