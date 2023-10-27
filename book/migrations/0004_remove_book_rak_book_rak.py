# Generated by Django 4.2.5 on 2023-10-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rak_buku', '0001_initial'),
        ('book', '0003_book_rak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='rak',
        ),
        migrations.AddField(
            model_name='book',
            name='rak',
            field=models.ManyToManyField(to='rak_buku.rak'),
        ),
    ]
