from django.db import models

# Create your models here.



class contacts(models.Model):

    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    job = models.CharField(max_length=30)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    DWY = models.SmallIntegerField()                #  DWY => (Duration) of (Work) (Year)
    DWM = models.SmallIntegerField()                #  DWM => (Duration) of (Work) (Month)
    favorites = models.CharField(max_length=300)


    def __str__(self):
        return f'family => {self.lName} | '





        # {
        #     'fName': self.fName,
        #     'lName': self.lName,
        #     'age'  : self.age,
        #     'city' : self.city,
        #     'country': self.country,
        #     'job'  : self.job,
        #     'phoneNumber': self.phoneNumber,
        #     'email': self.email,
        #     'DWY': self.DWY,
        #     'DWM': self.DWM,
        #     'favorites': self.favorites
        # }
    


        
    
