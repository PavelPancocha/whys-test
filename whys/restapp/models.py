from django.db import models


class Data(models.Model):
    ed = models.DecimalField(decimal_places=0, max_digits=10, verbose_name="Id")
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=180, blank=False)
    data = models.TextField(max_length=2000, blank=True)
