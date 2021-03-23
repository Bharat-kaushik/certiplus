from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField( default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.name
class GrowSection(models.Model):
    title = models.CharField(max_length=250,null=True)
    color = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.title

class GrowSubSection(models.Model):
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to="images/SubGrow", default="")
    description = models.TextField(null=True)
    section = models.ForeignKey(GrowSection, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class SubSectionDetails(models.Model):
    image = models.ImageField(upload_to="images/SubGrow", default="")
    description = models.TextField(null=True)
    sub_section = models.OneToOneField(GrowSubSection,on_delete=models.CASCADE)
    def __str__(self):
        return self.description



