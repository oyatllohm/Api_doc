from django.db import models
from ckeditor.fields import RichTextField
from django_mysql.models import ListCharField



class Department(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



class Themes(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='themes')
    name = models.CharField(max_length=30)
    title = models.TextField(max_length=100,null=True,blank=True)
    text = models.TextField(max_length=200,null=True,blank=True)

    
    
    def __str__(self) -> str:
        return self.name



class Simple_section(models.Model):
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE,related_name='simple_section')
    name = models.CharField(max_length=30)
    title = models.TextField(max_length=100,null=True,blank=True)
    text = models.TextField(max_length=200,null=True,blank=True)
    ck_text = RichTextField(null=True)

    def __str__(self) -> str:
        return self.name




class Pre_section(models.Model):
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE,related_name='pre_section')
    title = models.TextField(max_length=100,null=True)
    text = models.TextField(max_length=200,null=True,blank=True)
    tags = RichTextField(null=True)
    def __str__(self):
    	return self.title


class Table_section(models.Model):
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE,related_name='table_sections')
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50,null=True,blank=True)
    ck_text = RichTextField(null=True,blank=True)
    th = ListCharField(
        null = True,
        base_field= models.CharField(max_length=50),
        max_length=(100)
    )
    def __str__(self):
    	return self.name

    


class Tr_td(models.Model):
    table = models.ForeignKey(Table_section, on_delete=models.CASCADE,related_name='tr_td')
    td = ListCharField(
        null = True,
        base_field= models.CharField(max_length=50),
        max_length=(100)
    )






    




