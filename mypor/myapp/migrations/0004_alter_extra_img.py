# Generated by Django 5.0.3 on 2024-06-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_extra_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
