# Generated by Django 2.2.4 on 2020-05-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoNinjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='old dojo', max_length=255),
            preserve_default=False,
        ),
    ]
