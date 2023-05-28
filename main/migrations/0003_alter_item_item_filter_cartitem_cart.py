<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-04-12 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_item_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_filter',
            field=models.CharField(default='unisex', max_length=30),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.item')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
=======
# Generated by Django 4.1.7 on 2023-04-12 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_item_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_filter',
            field=models.CharField(default='unisex', max_length=30),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.item')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
>>>>>>> daad950f9bf9918ace52347581126bf4060fc0af
