# Generated by Django 4.0.2 on 2022-04-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
