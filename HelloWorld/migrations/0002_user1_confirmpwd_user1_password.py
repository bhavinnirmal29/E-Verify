# Generated by Django 4.1.2 on 2022-11-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HelloWorld", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user1",
            name="confirmPwd",
            field=models.CharField(default=10, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user1",
            name="password",
            field=models.CharField(default=121, max_length=50),
            preserve_default=False,
        ),
    ]