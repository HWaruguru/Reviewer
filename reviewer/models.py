from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Project(models.Model):
    title = models.CharField(max_length=155)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='projects/', default='default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    
    def __str__(self):
        return f'{self.title}'

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()


class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project.title} Rating'

@receiver(post_save, sender=Rating)
def update_project_rating(sender, instance, **kwargs):
    project_rating = ProjectRating.objects.filter(project__id=instance.project.id).first()
    if project_rating:
        ratings = Rating.get_ratings(instance.project.id).count()
        project_rating.design_average = ((project_rating.design_average * (ratings - 1)) + instance.design) / ratings
        project_rating.usability_average = ((project_rating.usability_average * (ratings - 1)) + instance.usability) / ratings
        project_rating.content_average = ((project_rating.content_average * (ratings - 1)) + instance.usability) / ratings
        project_rating.score = (project_rating.design_average + project_rating.usability_average + project_rating.content_average) / 3
        project_rating.save()
    else:
        score = (instance.design + instance.usability + instance.content) / 3
        project_rating = ProjectRating(
            score=score,
            design_average=instance.design,
            usability_average=instance.usability,
            content_average=instance.content,
            project=instance.project)
        project_rating.save()

class ProjectRating(models.Model):
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='projectrating', null=True)

    def save_rating(self):
        self.save()

    def __str__(self):
        return f'{self.score} ProjectRating'