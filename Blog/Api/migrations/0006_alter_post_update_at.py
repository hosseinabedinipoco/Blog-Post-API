# Generated by Django 5.1 on 2024-09-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_alter_post_created_at_alter_post_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
