# Generated by Django 3.0.5 on 2020-04-10 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0003_auto_20200410_0935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materia',
            options={'ordering': ['id']},
        ),
    ]