import os

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


@receiver(pre_delete)
def delete_leftover(sender, instance, **kwargs):
    if sender == Brochure:
        if os.path.isfile(instance.brochure.path):
            os.remove(instance.brochure.path)


class Brochure(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    brochure = models.FileField(blank=False)

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=True)
    answer1 = models.CharField(max_length=2000, blank=False)
    answer2 = models.CharField(max_length=2000, blank=False)
    answer3 = models.CharField(max_length=2000, blank=False)
    comments = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return 'Review by {}'.format(self.name)
