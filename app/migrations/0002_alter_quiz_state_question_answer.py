# Generated by Django 4.2.3 on 2023-07-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="state_question_answer",
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
