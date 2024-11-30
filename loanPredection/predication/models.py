from django.db import models

# Create your models here.

class Loan(models.Model):
    customer_id = models.IntegerField()
    loan_id = models.IntegerField(unique=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure = models.IntegerField()
    interest_rate = models.FloatField()
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    emis_paid_on_time = models.IntegerField()
    date_of_approval = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Loan {self.loan_id} for Customer {self.customer_id}"


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15, unique=True)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    approved_limit = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
