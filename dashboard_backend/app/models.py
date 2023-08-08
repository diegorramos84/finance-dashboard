from django.db import models
from django.contrib.auth.models import User

# investment Types (ISA, 401k)
class InvestmentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# institutions (brokers, banks that are holding the investment)
class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Portfolio
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Instrument (stocks, bonds)
class Instrument(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_type = models.ForeignKey(InvestmentType, on_delete=models.CASCADE)
    Institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    ticker_symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    position = models.DecimalField(max_digits=12, decimal_places=2)
    market_value = models.DecimalField(max_digits=12, decimal_places=2)
    # api data
    last_known_market_value = models.DecimalField(max_digits=12, decimal_places=2)
    last_updated_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.name} - {self.ticker_symbol}"
