# Generated by Django 3.2.9 on 2021-12-04 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0007_remove_parcelle_annees_remove_parcelle_semence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semence',
            name='besoin_eau',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='semence',
            name='besoin_temperature',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='semence',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='semence',
            name='recolte',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='semence',
            name='semis',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
