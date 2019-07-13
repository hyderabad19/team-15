from django.db import models

type = (
    ('Incharge','Incharge'),
    ('LoopManager','LoopManager'),

)

class District(models.Model):
    name = models.CharField(max_length=20)

    def _str_(self):
        return self.name

class Mandal(models.Model):
    name = models.CharField(max_length=20)
    district = models.ForeignKey(District,on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=20,default='sai')
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    contact = models.IntegerField(default=0)
    type = models.CharField(max_length = 20,choices = type,default='Incharge')
    approved = models.BooleanField(default=False)

    def _str_(self):
        return self.email
class Cluster(models.Model):
    cid = models.IntegerField(default=0)
    name = models.CharField(max_length=10)

    def _str_(self):
        return self.cid

class School(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20,default='new')
    verified = models.BooleanField(default=False)
    mandal = models.ForeignKey(Mandal,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)


    def _str_(self):
        return self.name

class ClusterSchool(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster,on_delete=models.CASCADE)

    def _str_(self):
        return self.id

class TypeResource(models.Model):
    type = models.CharField(max_length=20)

    def _str_(self):
        return self.type

class Resource(models.Model):
    school_name = models.CharField(max_length=30)
    resource_name = models.CharField(max_length=30)
    type = models.ForeignKey(TypeResource,on_delete=models.CASCADE)
    verify = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)

    def _str_(self):
        return self.school_name
