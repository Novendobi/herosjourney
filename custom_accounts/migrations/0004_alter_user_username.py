# Generated by Django 4.2.3 on 2023-09-06 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_accounts', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
