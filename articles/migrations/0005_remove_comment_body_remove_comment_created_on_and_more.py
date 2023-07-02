# Generated by Django 4.2.1 on 2023-07-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_comment_comment_comment_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
