# Generated by Django 3.2.9 on 2021-12-04 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0009_auto_20211204_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semence',
            old_name='frequence_de_culture',
            new_name='frequence_culture',
        ),
    ]
