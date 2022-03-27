from django.db import models

# from https://levelup.gitconnected.com/creating-a-recipe-api-with-django-rest-framework-6c2512d71d5b
class recipe(models.Model): #declaration of class
 #diffeerent fields
    name = models.CharField(max_length=400)
    ingriedient = models.CharField(max_length=1000)
    time=models.IntegerField()
    process= models.CharField(max_length=2000)
#function to return the name of record as name
    def __str__(self):
        return self.name
