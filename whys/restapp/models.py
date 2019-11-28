from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=180, blank=False)
    eid = models.DecimalField(decimal_places=0, max_digits=10, blank=False)
    data = models.TextField(max_length=1000, blank=True)
    unique_together = ['name', 'eid']


    def __str__(self):
        return "{} - Id: {}".format(self.name, self.eid)
