# Generated by Django 4.2.2 on 2023-06-26 13:44

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=10)),
                ('nickname', models.TextField(max_length=10)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('남성', '남성'), ('여성', '여성'), ('기타', '기타')], default='기타', max_length=8, null=True)),
                ('major', models.TextField(blank=True, max_length=15)),
                ('contact', models.TextField(blank=True, max_length=15)),
                ('about_me', models.TextField(blank=True, max_length=200)),
                ('profile_pic', models.ImageField(default='default/profile_pic_default.png', upload_to=accounts.models.profile_pic_path)),
            ],
        ),
    ]
