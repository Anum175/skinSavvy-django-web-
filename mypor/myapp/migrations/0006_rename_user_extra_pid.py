# Generated by Django 5.0.3 on 2024-06-30 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_pid_extra_user_alter_extra_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extra',
            old_name='user',
            new_name='pid',
        ),
    ]
