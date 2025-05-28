from django.db import models
import datetime as dt

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.published_date >= dt.datetime.now() - dt.timedelta(days=7)
    

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post.title}'