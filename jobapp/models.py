from django.db import models
from django.urls import reverse
from djrichtextfield.models import RichTextField
# Create your models here.

class Nursing(models.Model):
    job_title = models.CharField(max_length=164)
    job_company = models.CharField(max_length=164)
    location = models.CharField(max_length=164)
    description = RichTextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=500, blank=True)

    def __str__(self):
        return u'%s' % (str(self.job_title))

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})

class Welding(models.Model):
    job_title = models.CharField(max_length=164)
    job_company = models.CharField(max_length=164)
    location = models.CharField(max_length=164)
    description = RichTextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=500, blank=True)

    def __str__(self):
        return u'%s' % (str(self.job_title))

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})

class Driving(models.Model):
    job_title = models.CharField(max_length=164)
    job_company = models.CharField(max_length=164)
    location = models.CharField(max_length=164)
    description = RichTextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=500, blank=True)

    def __str__(self):
        return u'%s' % (str(self.job_title))

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})


class Development(models.Model):
    job_title = models.CharField(max_length=164)
    job_company = models.CharField(max_length=164)
    location = models.CharField(max_length=164)
    description = RichTextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=500, blank=True)

    def __str__(self):
        return u'%s' % (str(self.job_title))

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug': self.slug})