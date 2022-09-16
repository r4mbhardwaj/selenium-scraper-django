from django.db import models

class Plan(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_data = models.TextField(null=True)
    benifits = models.JSONField(null=True)
