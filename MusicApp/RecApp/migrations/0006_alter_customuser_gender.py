# Generated by Django 3.2.4 on 2022-03-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecApp', '0005_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female')], max_length=6),
        ),
    ]
