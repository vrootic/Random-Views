from hashlib import md5

from django.db import models


class UrlMapping(models.Model):
    URL_PREFIX = 'http://test.vicyang.com:8000/url/'

    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def click(self):
        self.click += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.URL_PREFIX}{self.url_hash}'
