from django.db import models
from login_app.models import User

class IdeaManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 5:
            errors['title'] = 'Title should have at least 5 characters.'

        if len(post_data['description']) < 10:
            errors['description'] = 'Description should have at least 10 characters.'

        return errors

class Idea(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name = "ideas", on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name = 'liked_ideas')
    user_dislikes = models.ManyToManyField(User, related_name = 'disliked_ideas')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = IdeaManager()

