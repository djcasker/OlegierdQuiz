# Generated by Django 2.2.3 on 2019-08-05 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190805_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timezone1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Timezone'),
        ),
    ]