# Generated by Django 3.2.9 on 2021-11-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20211115_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=8)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
