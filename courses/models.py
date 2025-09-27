from django.db import models


class Course(models.Model):
    FORMAT_CHOICES = [
        ('video', 'Video'),
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_weeks = models.IntegerField()
    mentor_info = models.TextField()
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES)
    is_free = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(null=True, blank=True)
    duration_minutes = models.IntegerField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (Course: {self.course.title})"
