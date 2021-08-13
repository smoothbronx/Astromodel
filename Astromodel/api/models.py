from django.db import models
from django.utils.timezone import datetime

class Query(models.Model):
    time = datetime.now().timestamp()

    id = models.AutoField(primary_key=True, null=False)
    datetime = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    protocol = models.CharField(blank=False, null=False, max_length=25)
    request = models.FileField(upload_to=f'jsons/{time}/', blank=False, null=False)
    response = models.FileField(upload_to=f'jsons/{time}/', blank=False, null=False)
    debug = models.BooleanField(blank=False, null=False, default=False)
    
    class Meta:
        verbose_name = ("Query")
        verbose_name_plural = ("Queries")

    def __str__(self):
        return f'Query id{self.id}: {self.protocol}'
    
    
class WeekActivity(models.Model):

    id = models.AutoField(primary_key=True, null=False)
    year = models.IntegerField(null=False, blank=False)
    week = models.IntegerField(null=False, blank=False)
    activity = models.IntegerField(null=False, blank=False)
    protocol = models.CharField(blank=False, null=False, max_length=25)

    class Meta:
        verbose_name = ("WeekActivity")
        verbose_name_plural = ("WeekActivities")

    def __str__(self):
        return f'<Activity {self.week}:{self.year}>'

    
    