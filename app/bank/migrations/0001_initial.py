# Generated by Django 2.2.7 on 2019-11-25 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=25)),
                ('city_params', models.CharField(choices=[('fresno', 'FRESNO'), ('clovis', 'CLOVIS'), ('madera', 'MADERA')], default=('fresno', 'FRESNO'), max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_account_params', models.CharField(choices=[('checking', 'CHECKING'), ('savings', 'SAVINGS'), ('none', 'NONE')], default=('checking', 'CHECKING'), max_length=8)),
                ('secondary_account_params', models.CharField(choices=[('checking', 'CHECKING'), ('savings', 'SAVINGS'), ('none', 'NONE')], default=('checking', 'CHECKING'), max_length=8)),
                ('credit_card_params', models.CharField(choices=[('gold', 'GOLD'), ('silver', 'SILVER'), ('platinum', 'PLATINUM'), ('none', 'NONE')], default=('gold', 'GOLD'), max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=50)),
                ('client_email', models.CharField(default='', max_length=50)),
                ('connect_to_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_current_balance', models.FloatField(default='0.00', max_length=500)),
                ('connect_to_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bank.Client')),
                ('connect_to_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Product')),
            ],
        ),
    ]