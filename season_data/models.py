from django.db import models
from metrics.models import RegularData,DefensiveActions,GoalKeepingStats,StandardStats,MiscStats,PassingStats,PlaytimeStats,PossesionStats,Team,ShootingStats
# Create your models here.

class Season(models.Model):
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    country = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    divison = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name} ({self.country}) | {self.start_year}-{str(self.end_year).strip(' ')[-2:]}"
    
class RegularSeason(RegularData):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # def save(self, *args, **kwargs):
    #     if self.x:
    #         self.pi_x = self.x / 3.14
    #     super().save(*args, **kwargs)

class SeasonStandardStats(StandardStats):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Standard Stats
    

class SeasonGoalKeepingStats(GoalKeepingStats):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Goal Keeping and Advanced Goal Keeping
    

class SeasonShootingStats(ShootingStats):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Shooting 
    

class SeasonPassingStats(PassingStats):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    # Passing,PassTypes
    

class SeasonDefensiveActions(DefensiveActions):
    # Goal and shot creation
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    
class SeasonPossesionStats(PossesionStats):
    # Possesion Stats
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    
class SeasonPlaytimeStats(PlaytimeStats):
    #PlayTime
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    

class SeasonMiscStats(MiscStats):
    # Misc
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    


