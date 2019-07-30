# Generated by Django 2.2 on 2019-07-18 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay_Question',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Essay style question',
                'verbose_name_plural': 'Essay style questions',
            },
            bases=('quiz.question',),
        ),
    ]