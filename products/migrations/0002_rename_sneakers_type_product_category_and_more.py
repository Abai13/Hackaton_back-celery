# Generated by Django 4.0.5 on 2022-07-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sneakers_type',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.IntegerField(choices=[('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47')]),
        ),
    ]