from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class InvestmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Instrument(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.PROTECT)
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    ticker_symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    position = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.ticker_symbol})"

class PortfolioDailyValue(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)

class InstrumentDailyValue(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
