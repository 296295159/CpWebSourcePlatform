# Generated by Django 2.0 on 2018-06-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20180526_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='userleavingmessage',
            name='subject',
            field=models.CharField(default='', help_text='主题', max_length=100, verbose_name='主题'),
        ),
    ]
