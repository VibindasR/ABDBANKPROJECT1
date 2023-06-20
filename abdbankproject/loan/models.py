from django.db import models

from banking.models import District, Branch
from credentials.models import Material

# Create your models here.
gend=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]

acc=[
    ('Current','Current'),
    ('Savings','Savings'),
]

lt=[
    ('Home_Loan','Home Loan'),
    ('Business_Loan','Business Loan'),
    ('Education_Loan','Education Loan'),
    ('Car_Loan','Car Loan')
]


class Loan(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.TextField()
    email = models.EmailField()
    gender = models.CharField(max_length=100,choices=gend)
    phoneNum = models.CharField(max_length=10)
    DOB = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    materials = models.ManyToManyField(Material)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, blank=True, null=True)
    account = models.CharField(max_length=100,choices=acc)
    loan_type = models.CharField(max_length=100,choices=lt)

    def __str__(self):
        return '{}'.format(self.email)