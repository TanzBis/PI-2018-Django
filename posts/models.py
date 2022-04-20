from django.db import models

from users.models import CustomUser


class Post(models.Model):
    status = models.CharField(max_length=1024)
    lookingForAJob = models.BooleanField(default=False)
    lookingForAJobDescription = models.CharField(max_length=1024)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)



    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.user}'