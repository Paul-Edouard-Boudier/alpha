# Generated by Django 3.2.9 on 2021-12-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0008_auto_20211204_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='semence',
            name='annee_recolte',
            field=models.CharField(default='', max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='semence',
            name='frequence_de_culture',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AddField(
            model_name='semence',
            name='rang_de_culture',
            field=models.CharField(default='', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='semence',
            name='temperature_base',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]