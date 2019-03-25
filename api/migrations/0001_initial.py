# Generated by Django 2.0.3 on 2019-03-25 04:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('from_rate', models.CharField(max_length=50)),
                ('to_rate', models.CharField(max_length=50)),
                ('on_delete', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'foreign_currency_exchange_rate',
            },
        ),
        migrations.CreateModel(
            name='ExchangeRateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_rate', models.DateField(default=django.utils.timezone.now)),
                ('rate', models.FloatField(max_length=100)),
                ('exchange_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ExchangeRate')),
            ],
            options={
                'db_table': 'foreign_currency_exchange_rate_log',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_maintenance', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'foreign_currency_setting',
            },
        ),
        migrations.AlterUniqueTogether(
            name='exchangerate',
            unique_together={('from_rate', 'to_rate')},
        ),
        migrations.AlterIndexTogether(
            name='exchangerate',
            index_together={('from_rate', 'to_rate', 'on_delete'), ('on_delete',)},
        ),
        migrations.AlterUniqueTogether(
            name='exchangeratelog',
            unique_together={('exchange_rate', 'date_rate')},
        ),
    ]