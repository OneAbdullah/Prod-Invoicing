from datetime import date
from django.db import models
from django.contrib.auth.models import User

type_of_user_choices = (
    ('d','Default'),
    ('v','Read Only'),
    ('w','Read and Write')
)

class invoice_owner(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name

class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    type_of_user = models.CharField(max_length=20,choices=type_of_user_choices,default='d')
    download_report_allowed = models.BooleanField(default=True)
    delete_invoice_allowed = models.BooleanField(default=True)
    invoice_owner_allowed = models.ManyToManyField(invoice_owner,blank=True)

    def __str__(self):
        return "Profile for user - {}".format(self.user.username)
    
class user_permission(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    download_report_allowed = models.BooleanField(default=True)
    delete_invoice_allowed = models.BooleanField(default=True)
    invoice_owner_allowed = models.ManyToManyField(invoice_owner,blank=True)
    
class building(models.Model):
    name = models.CharField(max_length=300,null=True,blank=True)
    owner = models.ForeignKey(invoice_owner,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def apartment_count(self):
        return (len(apartment.objects.filter(building=self)) == 0)

class apartment(models.Model):
    aprt_number = models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=300,null=True,blank=True)
    phone_nmber = models.CharField(max_length=50,null=True,blank=True)
    type_of = models.CharField(max_length=300,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    contract_number = models.CharField(max_length=300,null=True,blank=True)
    elect_number = models.CharField(max_length=300,null=True,blank=True)
    note = models.TextField(max_length=2000,null=True,blank=True)
    building = models.ForeignKey(building,on_delete=models.CASCADE)
    annual_rent = models.CharField(max_length=50,null=True,blank=True)
    payment_method = models.CharField(max_length=10,null=True,blank=True)

    temp_del = models.BooleanField(default=False)
    temp_del_date = models.DateField(null=True,blank=True)

    aprt_link = models.ForeignKey("tenant_link",on_delete=models.SET_NULL,blank=True,null=True)
    new_tenant_added = models.BooleanField(default=False)

    display_order = models.IntegerField(default=0)

    def __str__(self):
        return self.building.name + " - " + self.aprt_number
    
    def getDisplayName(self):
        aprt_types = {"Apartment":"شقة","Floor":"دور","Home":"غرفة","Store":"محل ","Studio":"ملحق"}
        try:
            return aprt_types[self.type_of]
        except:
            return self.type_of

    def getShowColor(self):
        invs = invoice.objects.filter(apartment=self).order_by("today_date")
        if (len(invs) == 0):
            return "green"
        inv = invs[len(invs) - 1]
        comp_date = date.today()
        to_date = date(inv.to_date.year,inv.to_date.month,inv.to_date.day)
        if (to_date >= comp_date):
            return "green"
        else:
            comp = comp_date - to_date
            if (comp.days <= 30):
                return "yellow"
            elif (comp.days > 30 and comp.days <= 90):
                return "red"
            else:
                return "black"
            
    def getLastToDate(self):
        invs = invoice.objects.filter(apartment=self).order_by("today_date")
        if (len(invs) == 0):
            return ""
        inv = invs[len(invs) - 1]
        to_date = date(inv.to_date.year,inv.to_date.month,inv.to_date.day)
        return "{}".format(to_date)
    

class tenant_link(models.Model):
    apartments = models.ManyToManyField(apartment)

class invoice(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    received_by = models.CharField(max_length=200,null=True,blank=True,default="-")
    apartment = models.ForeignKey(apartment,on_delete=models.SET_NULL,null=True,blank=True)
    owner = models.ForeignKey(invoice_owner,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=100,null=True,blank=True)
    bank_of_transfer = models.CharField(max_length=300,null=True,blank=True)
    transfer_date = models.DateField(null=True,blank=True)
    from_date = models.DateField(null=True,blank=True)
    to_date = models.DateField(null=True,blank=True)
    today_date = models.DateField(auto_now_add=True)
    remaining_amount = models.IntegerField(default=0)
    note = models.TextField(max_length=2000,null=True,blank=True)

    invoice_number = models.IntegerField(default=0)

    is_deleted = models.BooleanField(default=False)

    other_payment = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.apartment.building.name + " - " + self.apartment.aprt_number + " - {}".format(self.id)

class maintenance_invoice(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    apartment = models.ForeignKey(apartment,on_delete=models.SET_NULL,null=True,blank=True)
    owner = models.ForeignKey(invoice_owner,on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    today_date = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=2000,null=True,blank=True)

    invoice_number = models.IntegerField(default=0)
    
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.apartment.building.name + " - " + self.apartment.aprt_number + " - {}".format(self.id)