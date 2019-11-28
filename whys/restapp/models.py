from django.db import models


class AttributeName(models.Model):
    id = models.DecimalField(decimal_places=0, max_digits=10, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=180, blank=False)

    def __str__(self):
        return "{} - Id: {}".format(self.name, self.id)


class Data(models.Model):
    name = models.CharField(max_length=180, blank=False)
    eid = models.DecimalField(decimal_places=0, max_digits=10, blank=False)
    data = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return "{} - Id: {}".format(self.name, self.eid)