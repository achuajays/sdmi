from django.db import models

# Create your models here.

class notifc(models.Model):
    title = models.CharField(max_length = 100)
    loc = models.CharField(max_length = 100)
    ph = models.CharField(max_length = 100)
    dis = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    

class log(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class et(models.Model):
    loc = models.CharField(max_length=100)


class logteam(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)




class reffun(models.Model):
    title = models.CharField(max_length=100)
    dis= models.CharField(max_length=100)
    link = models.CharField(max_length=100)



class food(models.Model):
    name = models.CharField(max_length = 100 )
    loc = models.CharField(max_length = 100 )
    p = models.IntegerField(default=1)


class waste(models.Model):
    name = models.CharField(max_length=100)
    loc  = models.CharField(max_length=100) 
    ton= models.CharField(max_length=100)


class es(models.Model):
    loc = models.CharField( max_length=100)
    ph = models.IntegerField ()

