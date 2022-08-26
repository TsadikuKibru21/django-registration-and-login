# Generated by Django 4.0.6 on 2022-08-20 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_remove_account_accid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Role1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleName', models.CharField(max_length=15)),
                ('accId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.account1')),
            ],
        ),
        migrations.RemoveField(
            model_name='role',
            name='accId',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
