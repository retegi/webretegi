# Generated by Django 4.0.4 on 2022-04-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='label',
            field=models.ManyToManyField(blank=True, to='home.label'),
        ),
    ]
