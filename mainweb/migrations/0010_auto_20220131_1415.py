# Generated by Django 3.1.2 on 2022-01-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0009_alter_post_viewers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/category/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/news/'),
        ),
    ]