from django.db import models

# Create your models here.


class Availability(models.Model):
    user_id = models.IntegerField()
    is_interviewer = models.BooleanField(default=False)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.user_id)