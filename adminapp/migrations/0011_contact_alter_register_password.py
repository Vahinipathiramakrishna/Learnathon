# Generated by Django 4.2.9 on 2024-03-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_alter_admin_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('problem', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
