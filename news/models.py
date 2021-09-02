from django.db import models
from authentication.models import User


class News(models.Model):

    CATEGORY_OPTIONS = [
        ('ANNOUNCEMENTS', 'announcements'),
        ('COMMENTARY', 'commentary'),
        ('HIGHLIGHTS', 'highlights'),
        ('GUIDES', 'guides'),
        ('PLAYER', 'player'),
        ('FEATURES', 'features'),
        ('MATCH FEATURES', 'match features'),

    ]

    EVENTS_OPTIONS = [
        ('SPRING', 'spring'),
        ('SUMMER', 'summer'),
        ('INTERNATIONAL', 'international'),
        ('ACADEMY', 'academy')
    ]

    FORMAT_OPTIONS = [
        ('VIDEO', 'video'),
        ('ARTICLE', 'article')
    ]
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255,null=True,blank=True)
    formats = models.CharField(choices=FORMAT_OPTIONS, max_length=255,null=True,blank=True)
    events = models.CharField(choices=EVENTS_OPTIONS, max_length=255,null=True,blank=True)

    description = models.TextField(null=True,blank=True)
    title = models.TextField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    video=models.FileField(null=True,blank=True)
    video_link = models.TextField(null=True,blank=True)
    fb_link = models.URLField(null=True,blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    google_link = models.URLField(null=True,blank=True)
    instagram_link = models.URLField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.title)+'s news'
