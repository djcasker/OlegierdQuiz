# Generated by Django 2.2.3 on 2019-07-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20190722_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uquestion',
            name='wrong_answer_date',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='wrong_answer_date'),
        ),
    ]
