# Generated by Django 2.0.7 on 2020-04-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scrum', '0020_auto_20200424_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumslack',
            name='access_token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]