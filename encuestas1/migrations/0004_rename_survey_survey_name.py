# Generated by Django 4.2.4 on 2023-08-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas1', '0003_rename_questionset_survey_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='survey',
            new_name='name',
        ),
    ]