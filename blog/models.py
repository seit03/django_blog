from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    text = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.CharField()
    get = models.TextField()
    delete = models.Transform()
    put = models.Model()

    def __str__(self):
        return  f'{self.text}'

    def _check_model(self):
        return  f'{self.get}'

    def model(self):
        return  f'{self.delete}'

    def put_model(self):
        return  f'{self.put}'
