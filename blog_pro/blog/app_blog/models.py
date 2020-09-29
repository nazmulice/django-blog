from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=250, verbose_name="Put a Title")
    slug = models.SlugField(max_length=250, unique=True,allow_unicode=True)
    blog_content = models.TextField(verbose_name="what is on your mind")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title

    def _generate_unique_slug(self):
        unique_slug = slugify(self.blog_title,allow_unicode=True)
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)
    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")

    def __str__(self):
        return self.user + "likes" + self.blog

