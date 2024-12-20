from django.db import models
from django.conf import settings
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    visable = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail_blog", kwargs={"pk": self.pk})


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.comment[:10]}"
    
    def get_absolute_url(self):
        return reverse("blogs")