# Generated by Django 5.0.3 on 2024-06-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='desgination',
        ),
        migrations.RemoveField(
            model_name='extra',
            name='salary',
        ),
        migrations.AddField(
            model_name='extra',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
