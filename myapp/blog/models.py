from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    img_url= models.ImageField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    

def __str__(self):
    return self.title


#contact model

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


#aboutus
class AboutUs(models.Model):  
    content = models.TextField()

    def __str__(self):
        return "About Us Page"
