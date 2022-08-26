# Generated by Django 4.1 on 2022-08-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_admins',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('user', 'USER')], max_length=100, null=True),
        ),
    ]
