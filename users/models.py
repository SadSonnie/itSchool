from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    BOOL_CHOICES = ((True, 'Female'), (False, 'Male'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.BooleanField(choices=BOOL_CHOICES, default=True)
    home_university = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    motivation = models.CharField(max_length=1500, blank=True, help_text="Describe your motivation to participate in the IT-School (try to fit in 1500 symbols)")
    social_network_account = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save1(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     location.save(self)
    #     url.save(self)
    #     company.save(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # location.save(self.location)
        # url.save(self.url)
        # company.save(self.company)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
