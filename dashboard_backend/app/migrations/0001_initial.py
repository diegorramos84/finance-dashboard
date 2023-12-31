# Generated by Django 4.2.4 on 2023-08-10 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_symbol', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('position', models.DecimalField(decimal_places=2, max_digits=12)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.currency')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.institution')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioDailyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentDailyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instrument')),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='investment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.investmenttype'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.portfolio'),
        ),
    ]
