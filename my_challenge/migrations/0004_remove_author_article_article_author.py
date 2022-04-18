# Generated by Django 4.0.4 on 2022-04-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_challenge', '0003_rename_author_author_article_alter_article_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_challenge.author'),
        ),
    ]
