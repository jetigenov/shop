# Generated by Django 2.2 on 2019-12-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20191218_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='123', max_length=20),
            preserve_default=False,
        ),
    ]
