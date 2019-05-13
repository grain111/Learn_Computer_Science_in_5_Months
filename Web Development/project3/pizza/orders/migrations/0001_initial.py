# Generated by Django 2.1.7 on 2019-05-13 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraIngridient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCombination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ExtraIngridient')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('p_small', models.FloatField()),
                ('p_large', models.FloatField()),
                ('num_extra', models.IntegerField()),
                ('extras', models.ManyToManyField(related_name='dishes', through='orders.MenuCombination', to='orders.ExtraIngridient')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='orders.Group')),
            ],
        ),
        migrations.AddField(
            model_name='menucombination',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem'),
        ),
    ]
