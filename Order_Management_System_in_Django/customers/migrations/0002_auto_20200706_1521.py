# Generated by Django 3.0.8 on 2020-07-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='status',
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
