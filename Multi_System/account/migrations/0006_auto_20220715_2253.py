# Generated by Django 3.0 on 2022-07-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customuser_is_voted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default=False, upload_to='media/'),
        ),
    ]
