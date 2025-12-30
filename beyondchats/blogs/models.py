from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    source_url = models.URLField()
    published_date = models.DateField(null=True, blank=True)
    is_updates = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_content = models.TextField(blank=True)

    def __str__(self):
        return self.title
