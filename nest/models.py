from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=256, blank=False)
    def __unicode__(self):
        return self.name

