from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import random
from app.accounts.models import Account


class Category(models.Model):
    thumbnail = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=160, unique=True)
    slug_name = models.SlugField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(Category, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Category, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(Category, self).create(*args, **kwargs)

    class Meta:
        db_table = "categories"


admin.site.register(Category)


class Dish(models.Model):
    profile = models.ForeignKey(Account, on_delete=models.CASCADE)
    thumbnail = models.URLField(
        blank=True,
        null=True,
        default="/static/app/admin/assets/images/pexels.jpeg")
    name = models.CharField(max_length=160)
    slug_name = models.SlugField(max_length=350)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_veg = models.BooleanField(_('is_veg'), default=False)
    description = models.TextField()
    time_slot = models.TextField()
    mrp = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField(default=0)
    offer_price = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(Dish, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Dish, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(Dish, self).create(*args, **kwargs)

    class Meta:
        db_table = "dishes"


admin.site.register(Dish)


class DishImage(models.Model):
    thumbnail = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=160)
    # category = models.ForeignKey(Series, on_delete=models.CASCADE)
    is_veg = models.BooleanField(_('is_veg'), default=False)
    description = models.TextField()
    time_slot = models.TextField()
    mrp = models.PositiveSmallIntegerField()
    offer_price = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(DishImage, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(DishImage, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(random.randint(1, 21)))
        super(DishImage, self).create(*args, **kwargs)

    class Meta:
        db_table = "dish_images"