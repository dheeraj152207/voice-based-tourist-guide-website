# Generated by Django 4.0.3 on 2022-03-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220323_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]