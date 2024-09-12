# Generated by Django 5.1 on 2024-09-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.JSONField(null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]