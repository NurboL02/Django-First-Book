from django.db import models


class Book(models.Model):
    CHOISES = (
        ("HORROR", "HORROR"),
        ("COMEDY", "COMEDY"),
        ("DRAMA", "DRAMA"),
        ("ЛИРИКА", "ЛИРИКА"),
        ("ЭПОСА", "ЭПОСА"),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='', null=True, blank=True)
    description = models.TextField(max_length=300, default='')
    type_book = models.TextField()
    genre = models.CharField(max_length=1000, choices=CHOISES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
