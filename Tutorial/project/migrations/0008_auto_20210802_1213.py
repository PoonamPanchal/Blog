# Generated by Django 3.2.5 on 2021-08-02 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20210802_1210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]