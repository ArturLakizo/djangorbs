from django.db import models
import json
import uuid
from django.utils import datetime_safe
from django import forms



class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    sex = models.CharField(choices=(("М", " Male"), ("Ж", "Female")), max_length=1, default="М")
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    agent = models.CharField(max_length=50)
    bank_id = models.IntegerField     #(max_length=11)
    product = models.CharField(max_length=200)
    url = models.CharField(max_length=202)
    groups = models.CharField(max_length=200, blank=True, default='')
    priority = models.IntegerField   #(max_length=11)
    status = models.IntegerField   #(max_length=11)
    stoprouting = models.IntegerField   #(max_length=4)
    fieldset = models.CharField
    ip = models.CharField(max_length=200, blank=True, default='')
    operator = models.CharField(max_length=200)
    comment = models.CharField
    StatusExpire = models.DateTimeField("Дата просрочки", auto_now=False, blank=True, default='')
    date = models.DateTimeField("Дата заключения контракта", auto_now=True)
    lastname2 = models.CharField(max_length=200, blank=True, default='')
    firstname2 = models.CharField(max_length=200, blank=True, default='')
    middlename2 = models.CharField(max_length=200, blank=True, default='')
    phone2 = models.CharField(max_length=200, blank=True, default='')
    email2 = models.CharField(max_length=200, blank=True, default='')
    product2 = models.CharField(max_length=200, blank=True, default='')
    PRIMARY = models.CharField(max_length=200, blank=True, default='')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if "+375" not in self.phone:
            raise forms.ValidationError("You have wrong telephone number")
        super(Bid, self).save(force_insert, force_update)






class Choice(models.Model):
    question = models.ForeignKey(Bid, on_delete=models.CASCADE)
    some_text = models.CharField(max_length=200)
    some_integer = models.IntegerField(default=0)