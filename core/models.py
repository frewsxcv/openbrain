from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Category(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', blank=True, null=True)
    # description?
    # order or category?

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=30)
    prereqs = models.ManyToManyField('Topic', blank=True)
    category = models.ForeignKey('Category', blank=True, null=True)
    # description = models.TextField(blank=True)
    # other resources? wikipedia? simple university? wikibooks? wikiuniversity?

    def __unicode__(self):
        return self.name


class Video(models.Model):
    source_url = models.URLField()
    topic = models.ForeignKey('Topic')
    download_url = models.URLField(blank=True)
    license = models.ForeignKey('License')
    next_video = models.OneToOneField('self', blank=True, null=True)
    # practice_url = models.URLField(blank=True)
    # content_time = models.TimeField() #need a better name
    # series of videos [?] self

    def get_series(self):
        """
        Returns a list of all previous videos of a series
        TODO: should also list videos ahead in series
        """
        try:
            prev = Video.objects.get(next_video=self)
        except ObjectDoesNotExist:
            return [self]
        return prev.get_series() + [self]
        
    def __unicode__(self):
        return "{0}: {1}" .format(self.topic, self.source_url)


class License(models.Model):
    license = models.CharField(max_length=70)
    text_url = models.URLField(blank=True)
    # icon?
    
    def __unicode__(self):
        return self.license

'''
class Rating(models.Model):
    user
    video
    rating1
    rating2
'''
