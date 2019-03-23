from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'Subscribers list'


class Reviews(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    birthday = models.CharField(max_length=48, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Reviews'
        verbose_name_plural = 'List reviews'



# Create your models here.
