# Generated by Django 3.1.7 on 2021-04-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_auth'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='auth',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
