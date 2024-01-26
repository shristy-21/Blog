from django.db import models

# Create your models here.


class  Article(models.Model):
    Title=models.CharField(max_length=100)
    Content=models.TextField(max_length=200)
    img=models.ImageField(upload_to='article_images/',default='default_img.jpg')
    pub_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.Title
