# Generated by Django 5.1.3 on 2024-12-08 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_rename_lang_id_snippet_lang_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lang',
            name='standard',
        ),
    ]
