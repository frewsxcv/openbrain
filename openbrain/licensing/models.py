from django.db import models


class License(models.Model):
    license = models.CharField(max_length=70)
    text_url = models.URLField(blank=True)
    # icon?
    
    def __unicode__(self):
        return self.license
