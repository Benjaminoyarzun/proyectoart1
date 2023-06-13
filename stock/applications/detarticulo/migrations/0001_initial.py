# Generated by Django 4.2.1 on 2023-06-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detarticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=50)),
                ('observacion', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
    ]
