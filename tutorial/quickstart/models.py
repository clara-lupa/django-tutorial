from django.db import models

# Create your models here.
class FederalState(models.Model):
    letter_code = models.CharField(max_length=2)
    spec_yield = models.IntegerField()
    # created = models.DateTimeField(auto_now_add=True)
    # title = models.CharField(max_length=100, blank=True, default='')
    # code = models.TextField()
    # linenos = models.BooleanField(default=False)
    # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['letter_code']
