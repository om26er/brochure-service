from django.db import models


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
    comments = models.CharField(max_length=2000, blank=False)

    def __str__(self):
        return 'Review by {}'.format(self.name)
