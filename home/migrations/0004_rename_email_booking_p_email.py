# Generated by Django 4.0 on 2022-09-27 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='email',
            new_name='p_email',
        ),
    ]