from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_alter_account_is_premium'),
        ('book', '0001_initial'),
        ('book', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
                ('cart', models.ManyToManyField(related_name='cart', to='book.book')),
                ('owned_books', models.ManyToManyField(related_name='owned_books', to='book.book')),
            ],
        ),
    ]
