# Generated by Django 4.2.2 on 2023-06-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_apply_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='status',
            field=models.CharField(choices=[('review', '검토중'), ('accept', '수락됨'), ('reject', '거절됨')], default='review', max_length=8),
        ),
    ]