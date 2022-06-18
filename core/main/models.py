from django.db import models

# Create your models here.


class Homepage(models.Model): 
    name1 = models.CharField('Homepage name1', max_length=30) 
    name2 = models.CharField('Homepage name2', max_length=30) 
    about = models.TextField('Homepage about') 
    img = models.ImageField('Homepage img', upload_to='media') 
     
     
    def __str__(self): 
        return self.name1 

    class Meta: 
        verbose_name = 'Homepage' 
        verbose_name_plural = 'Homepages'



class HomePagePictures(models.Model): 
    name = models.CharField('Homepage name1', max_length=30)
    img = models.ImageField('Homepage img', upload_to='media') 
    price = models.CharField('Homepage name2', max_length=30) 
    
     
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePagePicture' 
        verbose_name_plural = 'HomePagePictures'





class HomePageCategory1(models.Model): 
    name = models.CharField('HomePageCategory1 name', max_length=30)
    img = models.ImageField('HomePageCategory1 img', upload_to='media') 
    price = models.CharField('HomePageCategory1 price', max_length=30) 
    
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePage1Category' 
        verbose_name_plural = 'HomePage1Categores'

class HomePageCategory2(models.Model): 
    name = models.CharField('HomePageCategory2 name', max_length=30)
    img = models.ImageField('HomePageCategory2 img', upload_to='media') 
    price = models.CharField('HomePageCategory2 price', max_length=30) 
    
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePage2Category' 
        verbose_name_plural = 'HomePage2Categores'

class HomePageCategory3(models.Model): 
    name = models.CharField('HomePageCategory3 name', max_length=30)
    img = models.ImageField('HomePageCategory3 img', upload_to='media') 
    price = models.CharField('HomePageCategory3 price', max_length=30) 
    
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePage3Category' 
        verbose_name_plural = 'HomePage3Categores'

class HomePageCategory4(models.Model): 
    name = models.CharField('HomePageCategory4 name', max_length=30)
    img = models.ImageField('HomePageCategory4 img', upload_to='media') 
    price = models.CharField('HomePageCategory4 price', max_length=30) 
    
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePage4Category' 
        verbose_name_plural = 'HomePage4Categores'

class HomePageCategory5(models.Model): 
    name = models.CharField('HomePageCategory5 name', max_length=30)
    img = models.ImageField('HomePageCategory5 img', upload_to='media') 
    price = models.CharField('HomePageCategory5 price', max_length=30) 
    
    def __str__(self): 
        return self.name 

    class Meta: 
        verbose_name = 'HomePage5Category' 
        verbose_name_plural = 'HomePage5Categores'



class Category(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Shoose(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catshoose')
    name  = models.CharField('Shoose name', max_length=30)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shoose'
        verbose_name_plural = 'Shooses'
