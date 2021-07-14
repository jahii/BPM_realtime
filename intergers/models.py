from django.db import models

# Create your models here.
class Serial_data(models.Model):
    class Meta:
        db_table = "serial"
    
    data = models.IntegerField(default = 0)