from django.db import models
from django.urls import reverse
# Create your models here.
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from PIL import Image

class ArticleColumn(models.Model):
    title = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    tag = TaggableManager(blank=True)
    avatar = models.ImageField(upload_to='article/%Y%m%d/',blank=True)
    column = models.ForeignKey(ArticleColumn,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='article')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

    def save(self, *args, **kwargs):
        article = super(ArticlePost, self).save(*args, **kwargs)

        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x,y) = image.size
            new_x = 400
            new_y = int(new_x * (y/x))
            resized_image = image.resize((new_x,new_y),Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article



