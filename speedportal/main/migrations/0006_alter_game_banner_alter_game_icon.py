# Generated by Django 4.2.6 on 2023-11-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_game_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='banner',
            field=models.ImageField(default='games_banners/default_game_banner.jpg', upload_to='games_banners'),
        ),
        migrations.AlterField(
            model_name='game',
            name='icon',
            field=models.ImageField(default='games_icons/default_game_icon.jpg', upload_to='games_icons'),
        ),
    ]
