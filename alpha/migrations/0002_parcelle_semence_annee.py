# Generated by Django 4.1.dev20211203115706 on 2021-12-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcelle',
            name='semence',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='alpha.semence'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcelles', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='alpha.parcelle')),
            ],
        ),
    ]
