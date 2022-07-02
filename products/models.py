from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45) 

    class Meta:
        db_table = 'menus'

    def __str__(self):
        return self.name 

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45) 
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name 

class Allergy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45) 

    class Meta:
        db_table = 'allergy'

    def __str__(self):
        return self.name 

class Drink(models.Model):
    id = models.AutoField(primary_key=True)
    korean_name = models.CharField(max_length=45) 
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    allergy = models.ManyToManyField(Allergy, null=True)

    class Meta:
        db_table = 'drinks'

    def __str__(self):
        return self.korean_name 

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45) 
    size_ml = models.CharField(max_length=45) 
    size_fluid_ounce = models.CharField(max_length=45) 

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.name 

class Nutrition(models.Model):
    id = models.AutoField(primary_key=True)
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nutritions'

    def __str__(self):
        return self.one_serving_kcal

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.URLField(max_length=2000) 
    drink = models.ForeignKey(Size, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.name 


