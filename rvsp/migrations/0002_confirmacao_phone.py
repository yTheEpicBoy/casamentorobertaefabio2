# Generated by Django 3.2.15 on 2023-08-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rvsp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmacao',
            name='phone',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
