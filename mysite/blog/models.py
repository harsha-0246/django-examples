# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    class:          defining an object
    Post:           Name of the model
    models.Model:   definine Post as a Django model, Django will save this in
        database

    models.CharField:       define text with required number of char's.
    models.TextField:       define a long text without limit.
    models.DateTimeField:   define a date time
    models.ForeignKey:      define a link to another model
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
