# Generated by Django 3.2.22 on 2023-10-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whereToEat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'custom_table_name',
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
