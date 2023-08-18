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
    total_players = models.IntegerField()
    avg_age = models.FloatField()
    possesion = models.FloatField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    non_penalty_goals = models.IntegerField()
    penalty_created = models.FloatField()
    penalty_attempted = models.FloatField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    non_penalty_expected_goals = models.FloatField()
    expected_assists = models.FloatField()
    progressive_carries = models.FloatField()
    progressive_passes = models.FloatField()

class GoalKeepingStats(RegularData):
    shot_on_target_against = models.IntegerField()
    saves = models.IntegerField()
    # save percentage = (total shots on target - goals conceded)/total shots on target
    save_percentage = models.FloatField()
    clean_sheet = models.IntegerField()
    pk_against = models.IntegerField()
    pk_saved = models.IntegerField()
    pk_missed = models.IntegerField()
    own_goals = models.IntegerField()
    freekick_goals_against = models.IntegerField()
    conrnerkick_goals = models.IntegerField()
    post_shot_expected_goals = models.FloatField()
    post_shot_expected_goals_per_shot_on_target = models.FloatField()
    # post shot xg goal difference
    post_shot_expected_goals_vs_allowed_goals = models.FloatField()
    launches_completed = models.IntegerField()
    launches_attempted = models.IntegerField()
    # avg distances are measured from goal post
    passes_attempted = models.IntegerField()
    throws = models.IntegerField()
    launch_percent = models.FloatField()
    avg_pass_length = models.FloatField()
    total_goal_kick = models.IntegerField()
    goal_kick_percentage = models.FloatField()
    avg_goal_kick_length = models.FloatField()
    crosses_faced = models.IntegerField()
    crosses_stopped = models.IntegerField()
    crosses_stopped_percentage = models.FloatField()
    defensive_action_outside_penalty_area = models.IntegerField()
    avg_distance_from_defensive_action_outside_penalty_area = models.IntegerField()

class ShootingStats(RegularData):
    goals_scored = models.IntegerField()
    total_shots_attempted = models.IntegerField()
    total_shots_attempted_on_target = models.IntegerField()
    shot_on_target_percentage = models.FloatField()
    shots_per_90 = models.FloatField()
    goal_per_shot = models.FloatField()
    goal_per_shot_on_target = models.FloatField()
    shot_on_target_percentage = models.FloatField()
    avg_shot_distance = models.FloatField()
    shots_from_freekicks = models.IntegerField()
    shots_from_penalty = models.IntegerField() #PKAtt
    non_penalty_expected_goal = models.FloatField()
    non_penalty_expected_goal_per_shot = models.FloatField()
    expected_goals_vs_conceded_goals = models.FloatField()
    non_penalty_expected_goals_vs_conceded_non_penalty_goals = models.FloatField()
    

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


