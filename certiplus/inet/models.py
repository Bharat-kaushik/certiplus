from django.db import models


class SectionCategory(models.Model):
    title = models.CharField(max_length=250, null=True, db_column="title")
    created_at = models.DateTimeField(auto_now_add= True, null=True)

    def __str__(self):
        return self.title


class GrowSection(models.Model):
    title = models.CharField(max_length=250,null=True)
    background_color = models.CharField(max_length=10,null=True,blank=True)
    text_color = models.CharField(max_length=10, null=True, blank=True)
    section_category = models.ForeignKey(SectionCategory, on_delete=models.CASCADE, null=True)

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

class ContectSections(models.Model):
    image = models.ImageField(upload_to="images/SubGrow", default="")


class ContectSubSections(models.Model):
    image = models.ImageField(upload_to="images/SubGrow", default="")
    description = models.TextField(null=True)
    sub_section = models.OneToOneField(ContectSections,on_delete=models.CASCADE)
    def __str__(self):
        return self.description


class SubContectDetails(models.Model):
    image = models.ImageField(upload_to="images/SubGrow", default="")
    description = models.TextField(null=True)
    sub_section = models.OneToOneField(ContectSubSections,on_delete=models.CASCADE)
    def __str__(self):
        return self.description
class News(models.Model):
    news = models.TextField(null=True)


