# Generated by Django 5.1.7 on 2025-03-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_projectdetail_key_features_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='details',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
