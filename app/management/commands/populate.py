from django.core.management.base import BaseCommand
from app.models import Student,Subjects,StudentSubject

class Command(BaseCommand):
    help = 'My custom command.'

    def handle(self, *args, **options):
        # Your command code goes here
        jss1_students = Student.objects.filter(student_class=1)
        jss1_subjects = Subjects.objects.all()

        for student in jss1_students:
            for subject in jss1_subjects:
                StudentSubject.objects.create(student=student, subject=subject)
                self.stdout.write(self.style.SUCCESS('added subjects to students'))
