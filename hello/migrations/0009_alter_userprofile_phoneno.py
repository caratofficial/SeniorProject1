# Generated by Django 4.2 on 2023-06-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0008_shoefeatures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phoneno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]