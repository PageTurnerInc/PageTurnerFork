# Generated by Django 4.2.5 on 2023-10-26 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_rak_book_rak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rak',
        ),
    ]
