from django.db import models

# Create your models here.
    
class Team(models.Models) : 
    team_name = models.CharField(max_length=30)
    team_url = models.URLField()
    country = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RegularData(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches = models.IntegerField()
    matches_won = models.IntegerField()
    matches_draw = models.IntegerField()
    matches_lost = models.IntegerField()
    points = models.IntegerField()
    goals_for = models.IntegerField()
    expected_goals = models.FloatField()
    goals_against = models.IntegerField()
    expected_goals_against = models.FloatField()
    goal_difference = models.IntegerField()
    expected_goals_difference = models.FloatField()
    expected_goals_difference_p90 = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.x:
    #         self.pi_x = self.x / 3.14
    #     super().save(*args, **kwargs)

class StandardStats(RegularData):
    # Standard Stats
    pass    

class GoalKeepingStats(RegularData):
    # Goal Keeping and Advanced Goal Keeping
    pass    

class ShootingStats(RegularData):
    # Shooting 
    pass    

class PassingStats(RegularData):
    # Passing,PassTypes
    pass    

class DefensiveActions(RegularData):
    # Goal and shot creation
    pass    

class PossesionStats(RegularData):
    pass    

class PlaytimeStats(RegularData):
    pass    

class MiscStats(RegularData):
    pass    


