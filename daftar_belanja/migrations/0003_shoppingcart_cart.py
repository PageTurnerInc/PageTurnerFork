# Generated by Django 4.2.6 on 2023-10-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_alter_book_user"),
        ("daftar_belanja", "0002_remove_shoppingcart_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="shoppingcart",
            name="cart",
            field=models.ManyToManyField(to="book.book"),
        ),
    ]
