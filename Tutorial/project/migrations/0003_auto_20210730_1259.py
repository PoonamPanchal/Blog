# Generated by Django 3.2.5 on 2021-07-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='technology',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]