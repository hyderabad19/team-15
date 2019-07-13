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
