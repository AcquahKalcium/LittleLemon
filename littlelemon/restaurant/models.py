from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   id = models.IntegerField(primary_key=True)
   title =  models.CharField(max_length=255)
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.IntegerField() 

   def __str__(self): 
        return f'{self.title} : {str(self.price)}'
   
