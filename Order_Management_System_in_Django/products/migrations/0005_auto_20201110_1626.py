# Generated by Django 3.0.8 on 2020-11-10 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201108_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('', 'Choose Product Unit'), ('Kg', 'kg'), ('L', 'litre'), ('Pcs', 'pcs'), ('Gm', 'gm'), ('m2', 'm2'), ('m3', 'm3'), ('ml', 'ml')], default='', max_length=50),
        ),
    ]
