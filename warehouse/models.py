# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from time import time
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime
import pytz
from ERP.models import service

def getWareHouseContractUploadPath(instance , filename ):
    return 'warehouse/contracts/%s_%s_%s' % (str(time()).replace('.', '_'), instance.user.username, filename)
def getWareHouseDocUploadPath(instance , filename ):
    return 'warehouse/docs/%s_%s_%s' % (str(time()).replace('.', '_'), instance.user.username, filename)
def checkinUploadPath(instance , filename ):
    return 'warehouse/checkin/%s_%s_%s' % (str(time()).replace('.', '_'), instance.description, filename)



class Service(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 100 , null = False, unique = True)
    user = models.ForeignKey(User , related_name = 'ServicesCreated' , null = False)
    cin = models.CharField(max_length = 100 , null = True)
    tin = models.CharField(max_length = 100 , null = True)
    telephone = models.CharField(max_length = 20 , null = True)
    street = models.CharField(max_length = 300 , null = True)
    pincode = models.PositiveIntegerField(null = True)
    city = models.CharField(max_length = 100 , null = True)
    state = models.CharField(max_length = 50 , null = True)
    country = models.CharField(max_length = 50 , null = True)
    gst = models.CharField(max_length=15, null=True)
    pan = models.CharField(max_length=13, null=True)


    def __str__(self):
        return self.name

class Contact(models.Model):
    user = models.ForeignKey(User , related_name = 'contactsCreated' , null = False)
    name = models.CharField(max_length = 100 , null = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    company = models.ForeignKey(Service , null = False , related_name = 'contacts')
    email = models.EmailField(null = True)
    mobile = models.CharField(max_length = 15 , null = True)
    designation = models.CharField(max_length = 30 , null = True)
    notes = models.TextField(max_length = 300 , null = True)

UNIT_TYPE = (
    ('sqft' , 'sqft'),
    ('msq' , 'msq'),

)

class Space(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User , related_name = 'spaces' , null = False)
    name = models.CharField(max_length = 100 , null = False)
    areas = models.CharField(max_length = 50000 , null = False)
    code = models.CharField(max_length = 100 , null = False)
    areaLength = models.PositiveIntegerField(null = True,default=1)


class Contract(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User , related_name = 'contract' , null = False)
    company = models.ForeignKey(Service , null = False , related_name = 'contracts')
    billingFrequency = models.PositiveIntegerField(null = False)
    billingDates = models.CharField(max_length = 30, null=False)
    rate = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    unitType = models.CharField(choices = UNIT_TYPE, max_length = 15 , default = "sqft")
    dueDays = models.PositiveIntegerField(null = True)
    occupancy = models.CharField(max_length = 50000, null = False)
    areas = models.ForeignKey(Space , related_name='contractSpace' , null=True)
    contractPaper = models.FileField(upload_to=getWareHouseContractUploadPath, null=True)
    otherDocs = models.FileField(upload_to=getWareHouseDocUploadPath, null = True)
    occupancy_screenshort = models.CharField(max_length = 100000 , null = True)
    dueDate = models.DateField(null = True)

CONTRACT_STATE_CHOICES = (
    ('quoted' , 'quoted'),
    ('cancelled' , 'cancelled'),
    ('approved' , 'approved'),
    ('billed' , 'billed'),
    ('received' , 'received'),
    ('dueElapsed' , 'dueElapsed'),
)

class Invoice(models.Model):
    contract = models.ForeignKey(Contract , null = False , related_name="invoices")
    data = models.CharField(max_length = 10000 , null = True)
    value = models.PositiveIntegerField(null = True , default=0)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(choices = CONTRACT_STATE_CHOICES , max_length=12 , default = 'quoted')
    dueDate = models.DateField(null = True)
    billedDate = models.DateTimeField(null = True)
    recievedDate = models.DateTimeField(null = True)
    archivedDate = models.DateTimeField(null = True)
    fromDate = models.DateField(null = True)
    toDate = models.DateField(null = True)
    grandTotal = models.PositiveIntegerField(default=0)

class Checkin(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    # user = models.ForeignKey(User , related_name = 'contract' , null = False)
    contract = models.ForeignKey(Contract , null = True , related_name="checkins")
    description = models.CharField(max_length = 10000 , null = False)
    height = models.PositiveIntegerField(null = True)
    width = models.PositiveIntegerField(null = True)
    length = models.PositiveIntegerField(null = True)
    weight = models.PositiveIntegerField(null = True)
    checkedin = models.BooleanField(default = True)
    qty = models.FloatField(null = True)
    place = models.CharField(max_length = 50000, null = True)
    awb = models.FileField(upload_to=checkinUploadPath, null=True)

CHECKOUT_TYPE_CHOICES = (
    ('qty', 'qty'),
    ('percent', 'percent'),
)

class Checkout(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User , related_name = 'wareHouseCheckouts' , null = False)
    parent = models.ForeignKey(Checkin , related_name='checkouts' , null= False)
    typ = models.CharField(max_length = 10 , default = 'qty' , choices = CHECKOUT_TYPE_CHOICES )
    initial = models.FloatField(null = False)
    value = models.FloatField(null = False)
    final = models.FloatField(null = False)

ITEM_TYPE = (
    ('unit' , 'unit'),
    ('cartan', 'cartan'),
    ('pieces', 'pieces'),
    ('packages', 'packages'),
)

class CustomerCommodity(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    contact = models.ForeignKey(Contact , null = False , related_name="commoditiescontact")

class Commodity(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    contract = models.ForeignKey(Contract , null = True , related_name="commodities")
    name = models.CharField(max_length = 100 , null = False)
    qty =  models.PositiveIntegerField(null = True)
    typ = models.CharField(max_length=10, default='unit', choices = ITEM_TYPE )
    customercommodity = models.ForeignKey(CustomerCommodity , null = True , related_name="contactcommodities")

class CommodityQty(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    checkIn =  models.PositiveIntegerField(null = True)
    checkOut =  models.PositiveIntegerField(null = True)
    balance =  models.PositiveIntegerField(null = True)
    commodity = models.ForeignKey(Commodity , null = True , related_name="commoditypro")

@receiver(pre_save, sender=Invoice, dispatch_uid="update_invoice_details")
def update_invoice_details(sender, instance, **kwargs):
    print "setting the dates"
    if instance.status == 'billed':
        instance.billedDate = datetime.now(pytz.timezone('Asia/Kolkata'))
    elif instance.status == 'received':
        instance.recievedDate = datetime.now(pytz.timezone('Asia/Kolkata'))
    elif instance.status == 'cancelled':
        instance.archivedDate = datetime.now(pytz.timezone('Asia/Kolkata'))
