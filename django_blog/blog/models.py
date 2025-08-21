from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # We will route tags by name to match the task’s example path
        return reverse("posts-by-tag", kwargs={"tag_name": self.name})


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User ,on_delete=models.CASCADE,related_name='posts')
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # when created
    updated_at = models.DateTimeField(auto_now=True)      # last edited

    class Meta:
        ordering = ['created_at']  # oldest first (change to ['-created_at'] for newest first)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'