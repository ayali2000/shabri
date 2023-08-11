from django.db import models

# Create your models here.

class Post(models.Model):
    post_id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    intro = models.TextField(null = True, blank =True)
    file = models.FileField(null = True, blank =True)
    is_Video = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.title
    
    class Meta:
        ordering = ['-date_added']
        
class More_post(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField(null = True, blank =True)
    file = models.FileField(null = True, blank =True)
    date_added = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['date_added']       
        
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    email = models.EmailField()
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-comment_date']