from django.db import models
from django.core.urlresolvers import reverse

#Apps
from utils import get_random_token

class Link(models.Model):
    token = models.CharField(max_length=5, unique=True, null=True)
    url = models.URLField()
    
    @staticmethod
    def shorten(obj):
        link, _ = Link.objects.get_or_create(url=obj.url)
        return str(link.token)

    @staticmethod
    def expand(slug):
        token = str(slug)
        link = Link.objects.get(token=token)
        return link.url

    def get_absolute_url(self):
        return reverse('link_show',kwargs={'token':self.token})

    def save(self, *args, **kwargs):
        if not self.id:
            def __get_unique_token():
                token = get_random_token()
                if Link.objects.filter(token=token).count() > 0:
                    return __get_unique_token()
                return token
            self.token = __get_unique_token()
        return super(Link, self).save(*args, **kwargs)
