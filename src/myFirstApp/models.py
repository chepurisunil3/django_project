from django.db import models
import random
import os

def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):
    print(instance)
    new_filename = random.randint(1,4324234234)
    name,ext = get_file_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)


class FirstAppQuerySet(models.query.QuerySet):
    def isAvailable(self):
        return self.filter(isAvailable=True)

class FirstAppManager(models.Manager):
    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None
    def isAvailable(self):
        qs = self.get_queryset().filter(isAvailable=True)
        if qs.count() >= 1:
            return qs
        else:
            return None

class FirstApp(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    image = models.FileField(upload_to=upload_image_path,null=True,blank=True)
    isAvailable = models.BooleanField(default=False)
    
    objects = FirstAppManager()
    
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
