# Generated by Django 2.0.7 on 2018-07-29 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreIGR_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreIGR_app.User'),
        ),
    ]