# Generated by Django 2.2.3 on 2019-07-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20190730_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalizedquiz',
            name='question_repe',
            field=models.IntegerField(blank=True, default=0, max_length=24, null=True, verbose_name='question_repe'),
        ),
    ]