# Generated by Django 4.2.4 on 2023-08-26 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas1', '0004_rename_survey_survey_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choise',
            old_name='choise_Text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='text',
        ),
    ]
