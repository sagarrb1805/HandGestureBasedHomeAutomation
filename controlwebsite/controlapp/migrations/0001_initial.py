# Generated by Django 3.2.5 on 2022-03-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('switch_1', models.BooleanField(default=False)),
                ('switch_2', models.BooleanField(default=False)),
                ('switch_3', models.BooleanField(default=False)),
                ('switch_4', models.BooleanField(default=False)),
                ('switch_5', models.BooleanField(default=False)),
            ],
        ),
    ]