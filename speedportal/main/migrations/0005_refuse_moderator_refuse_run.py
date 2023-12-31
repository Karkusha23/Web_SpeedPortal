# Generated by Django 4.2.6 on 2023-11-14 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_moderator'),
        ('main', '0004_refuse_run_is_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='refuse',
            name='moderator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.moderator'),
        ),
        migrations.AddField(
            model_name='refuse',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.run'),
        ),
    ]
