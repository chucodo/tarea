# Generated by Django 4.2.4 on 2023-08-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas1', '0002_questionset_question_question_set'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionSet',
            new_name='Survey',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_set',
            new_name='survey',
        ),
        migrations.RenameField(
            model_name='survey',
            old_name='question_set_name',
            new_name='survey',
        ),
    ]
