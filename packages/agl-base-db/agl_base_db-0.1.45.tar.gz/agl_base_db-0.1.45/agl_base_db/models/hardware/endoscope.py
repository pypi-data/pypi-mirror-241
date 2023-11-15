from django.db import models

class EndoscopeManager(models.Manager):
    def get_by_natural_key(self, name, sn):
        return self.get(name=name, sn=sn)
    
class Endoscope(models.Model):
    objects = EndoscopeManager()
    
    name = models.CharField(max_length=255)
    sn = models.CharField(max_length=255)
    
    def natural_key(self):
        return (self.name, self.sn)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Endoscope'
        verbose_name_plural = 'Endoscopes'
