# Generated by Django 5.1.3 on 2024-12-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_stock_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='is_AFA',
            field=models.BooleanField(default=True),
        ),
    ]