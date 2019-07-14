from django.db import models
# import datetime


type = (
    ('Incharge','Incharge'),
    ('LoopManager','LoopManager'),

)

class TypeUsers(models.Model):
    #id = models.AutoField()
    type = models.CharField(max_length=30)
    def __str__(self):
        return self.id

class Users(models.Model):
    uid = models.ForeignKey(TypeUsers,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    contact = models.IntegerField(default=0)
    type = models.CharField(max_length = 20,choices = type,default='Incharge')

    def __str__(self):
        return self.name


# class Resource(models.Model):
#     id = models.AutoField(primary_key=True)
#     type  = models.CharField(max_length=30)
#     resource_name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.school_name



class Mandal(models.Model):
    #id = models.IntegerField()
    name = models.CharField(max_length=10)
    district = models.CharField(max_length=20)

    def __str__(self):
        return self.id

class District(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=10)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.id

class State(models.Model):
    #id = models.AutoField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.id

class School(models.Model):
    #sid = models.AutoField()
    number = models.IntegerField(default=0)
    password = models.CharField(max_length=30)
    verified = models.BooleanField(default=False)
    #mandal = models.ForeignKey(Mandal,on_delete=models.CASCADE)
    #district = models.ForeignKey(District,on_delete=models.CASCADE)
    #state = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.sid


class Cluster(models.Model):
    cid = models.IntegerField(default=0)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.cid

class SchoolCluster(models.Model):
    #id = models.AutoField(primary_key=True)
    sid = models.IntegerField(default=0)
    cid = models.IntegerField(default=0)

    def __str__(self):
        return self.sid







class Report(models.Model):
    source_school = models.IntegerField(default=0)
    dest_school   = models.IntegerField(default=0)
    start_time    = models.CharField(max_length=30)
    end_time      = models.CharField(max_length=30)
    date          = models.CharField(max_length=20)

    print(date)
    def __str__(self):
        return str(self.source_school)





#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
# # class Publication(models.Model):
# #     title = models.CharField(max_length=30)
# #
# #     class Meta:
# #         ordering = ('title',)
# #
# #     def __str__(self):
# #         return self.title
# #
# # class Article(models.Model):
# #     headline = models.CharField(max_length=100)
# #     publications = models.ManyToManyField(Publication)
# #
# #     class Meta:
# #         ordering = ('headline',)
# #
# #     def __str__(self):
# #         return self.headline



class NewReport(models.Model):
    source_school = models.IntegerField(default=0)
    dest_school   = models.IntegerField(default=0)
    start_time    = models.CharField(max_length=30)
    end_time      = models.CharField(max_length=30)
    date          = models.CharField(max_length=20)

    print(date)
    def __str__(self):
        return str(self.source_school)