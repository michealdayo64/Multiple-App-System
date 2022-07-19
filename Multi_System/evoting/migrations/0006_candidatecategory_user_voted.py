# Generated by Django 3.0 on 2022-07-11 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evoting', '0005_remove_candidatecategory_vote_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatecategory',
            name='user_voted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
