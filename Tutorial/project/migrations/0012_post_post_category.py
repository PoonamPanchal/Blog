# Generated by Django 3.2.5 on 2021-08-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project.category'),
        ),
    ]
