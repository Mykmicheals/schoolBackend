# Generated by Django 3.2 on 2023-02-26 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20230226_2156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentDetails',
            new_name='Student',
        ),
        migrations.AlterModelOptions(
            name='subjects',
            options={'verbose_name_plural': 'Subjects'},
        ),
    ]
