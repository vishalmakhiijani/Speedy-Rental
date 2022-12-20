from django.db import models

class teams(models.Model):
    name=models.CharField(max_length=100,blank=False)
    designation=models.CharField(max_length=200,blank=False)
    twitter=models.CharField(max_length=256)
    facebook=models.CharField(max_length=256)
    linkedin=models.CharField(max_length=256)
    # Commented Due to Pipe Install Issue
    # team_image=models.ImageField(upload_to='uploads/teams/')

    @staticmethod
    def get_all_team_members():
        return teams.objects.all()


    def __str__(self):
        return self.name