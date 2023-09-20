# Generated by Django 3.2.12 on 2023-08-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zkteco', '0008_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(unique=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]