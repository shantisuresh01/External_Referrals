# Generated by Django 4.0.5 on 2022-06-28 20:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting account.', verbose_name='active')),
                ('is_referrer', models.BooleanField(default=True, help_text='Designates whether this user should be treated as a Referrer account. Unselect this instead of deleting account.', verbose_name='referrer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReferrerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(default='', max_length=30)),
                ('state', localflavor.us.models.USStateField(max_length=2)),
                ('zipcode', localflavor.us.models.USPostalCodeField(max_length=2)),
                ('country', models.CharField(default='United States', max_length=50)),
                ('phone', models.CharField(help_text='Contact phone number', max_length=12)),
                ('extension', models.CharField(help_text='Phone extension', max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.user')),
            ],
            options={
                'verbose_name': 'ReferrerProfile',
                'verbose_name_plural': 'ReferrerProfile',
            },
        ),
    ]
