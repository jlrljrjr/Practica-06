# Generated by Django 5.0.2 on 2024-03-03 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jorge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cereales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreC', models.CharField(max_length=20)),
                ('presentacion', models.CharField(max_length=20)),
                ('gramos', models.CharField(max_length=20)),
            ],
        ),
    ]
