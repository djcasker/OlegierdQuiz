# Generated by Django 2.2.3 on 2019-07-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190730_0602'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedquiz',
            name='question_attemp',
            field=models.IntegerField(blank=True, default=0, max_length=24, null=True, verbose_name='Current Score'),
        ),
    ]