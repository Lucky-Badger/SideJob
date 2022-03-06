# Generated by Django 4.0.2 on 2022-02-17 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('A', 'Administrator'), ('U', 'User')], default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Group3Capstone.user')),
            ],
            bases=('Group3Capstone.user',),
        ),
    ]
