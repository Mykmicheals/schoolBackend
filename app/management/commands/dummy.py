from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from app.models import CustomUser, ClassRoom
from faker import Faker
import random



class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()

    # Create 30 teachers
        for _ in range(30):
            email = fake.email()
            while User.objects.filter(email=email).exists():
                email = fake.email()

            user = User.objects.create(
                email=email,
                first_name=fake.first_name(),
                middle_name=fake.last_name(),
                last_name=fake.last_name(),
                is_teacher=True,
                password='password1234'
            )
            user.save()

        # Create 5 principals
        for _ in range(5):
            email = fake.email()
            while User.objects.filter(email=email).exists():
                email = fake.email()

            user = User.objects.create(
                email=email,
                first_name=fake.first_name(),
                middle_name=fake.last_name(),
                last_name=fake.last_name(),
                is_principal=True,
                password='password1234'
            )
            user.save()

        # Get the list of classrooms
        classrooms = ClassRoom.objects.all()

        # Create remaining students
        for _ in range(965):
            email = fake.email()
            while User.objects.filter(email=email).exists():
                email = fake.email()

            classroom = random.choice(classrooms)
            user = User.objects.create(
                email=email,
                first_name=fake.first_name(),
                middle_name=fake.last_name(),
                last_name=fake.last_name(),
                is_student=True,
                classroom=classroom,
                password='password1234'
            )
            user.save()

        self.stdout.write(self.style.SUCCESS('Dummy data created successfully'))
