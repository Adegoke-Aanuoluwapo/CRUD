from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.charField(max_length = 400)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length = 400 )
    date_released = models.Datefield()
    likes = models.integerField()
    duration = models.integerField()
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.title}"

class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()
    song_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    def __str__(self):
        if len(self.content) > 50:
            return f"{self.content[0:50]}..."
        else:
            return f"{self.content}"