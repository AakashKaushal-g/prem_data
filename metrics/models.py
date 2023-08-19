from django.db import models
from math import round
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

class StandardStats(RegularData):
    total_players = models.IntegerField()
    avg_age = models.FloatField()
    possesion = models.FloatField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    non_penalty_goals = models.IntegerField()
    penalty_scored = models.IntegerField()
    penalty_attempted = models.FloatField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    non_penalty_expected_goals = models.FloatField()
    expected_assists = models.FloatField()
    progressive_carries = models.IntegerField()
    progressive_passes = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.goals_scored and self.penalty_scored:
            self.non_penalty_goals = abs(self.goals_scored - self.penalty_scored)
        super().save(*args, **kwargs)

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

    def save(self, *args, **kwargs):
        if self.post_shot_expected_goals and self.goals_against:
            self.post_shot_expected_goals_vs_allowed_goals = abs(self.post_shot_expected_goals - self.goals_against)
        super().save(*args, **kwargs)

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
    
    def save(self, *args, **kwargs):
        if self.total_shots_attempted and self.total_shots_attempted_on_target:
            self.shot_on_target_percentage = round(((self.total_shots_attempted - self.total_shots_attempted_on_target)/self.total_shots_attempted)*100,3)

        if self.total_shots_attempted :
            self.shots_per_90 = round(self.total_shots_attempted/90,3)

        if self.goals_scored and self.total_shots_attempted :
            self.goal_per_shot = round(self.goals_scored/self.total_shots_attempted,3)

        if self.goals_scored and self.total_shots_attempted_on_target:
            self.goal_per_shot_on_target = round(self.goals_scored/self.total_shots_attempted_on_target,3)

        if self.non_penalty_expected_goal and self.total_shots_attempted :
            self.non_penalty_expected_goal_per_shot = round(self.non_penalty_expected_goal/self.total_shots_attempted,3)

        super().save(*args, **kwargs)
    
class PassingStats(RegularData):
   player = models.IntegerField()
   passes_attempted = models.IntegerField()
   passes_completed = models.IntegerField()
   pass_completion_percent = models.FloatField()
   pass_distance = models.FloatField()
   progressive_pass_distance = models.FloatField()
   short_passes_attempted = models.IntegerField()
   short_passes_completed = models.IntegerField()
   short_pass_completion_percent = models.FloatField()
   medium_passes_attempted = models.IntegerField()
   medium_passes_completed = models.IntegerField()
   medium_pass_completion_percent = models.FloatField()
   long_passes_attempted = models.IntegerField()
   long_passes_completed = models.IntegerField()
   long_pass_completion_percent = models.FloatField()
   assists = models.IntegerField()
   # xG which follows a pass that assists a shot
   expected_assisted_goals = models.FloatField()
   # likelihood each completed pass becomes a goal assists given the pass type, phase of play, location and distance
   expected_assists = models.FloatField()
   assists_vs_expected_assists_difference = models.FloatField()
   key_passed = models.IntegerField()
   passes_into_final_third = models.IntegerField()
   passes_into_penalty_area = models.IntegerField()
   crosses_into_penalty_area = models.IntegerField()
   progressive_passes = models.IntegerField()

   live_passes = models.IntegerField()
   dead_ball_passes = models.IntegerField()
   freekick_attempted = models.IntegerField()
   through_ball = models.IntegerField()
   # any pass travelled more than 40 yrds along thewidth of field
   switch = models.IntegerField()
   thorw_in = models.IntegerField()
   cross = models.IntegerField()
   corner = models.IntegerField()
   inswing_corner = models.IntegerField()
   outswing_corner = models.IntegerField()
   straight_corner = models.IntegerField()
   passes_offside = models.IntegerField()
   passes_blocked_by_opposition = models.IntegerField()

   shot_creating_actions = models.IntegerField()
   shot_creating_actions_p90 = models.IntegerField()
   sca_by_live_passes = models.IntegerField()
   sca_by_dead_balls = models.IntegerField()
   sca_by_take_ons = models.IntegerField()
   sca_by_shot = models.IntegerField()
   sca_by_defensive_action = models.IntegerField()
   sca_by_foul_drawn = models.IntegerField()
   goal_creating_actions = models.IntegerField()
   goal_creating_actions_p90 = models.IntegerField()
   gca_by_live_passes = models.IntegerField()
   gca_by_dead_balls = models.IntegerField()
   gca_by_take_ons = models.IntegerField()
   gca_by_shot = models.IntegerField()
   gca_by_defensive_action = models.IntegerField()
   gca_by_foul_drawn = models.IntegerField()

   def save(self, *args, **kwargs):
        if self.passes_attempted and self.passes_completed:
            self.pass_completion_percent = round((self.passes_completed/self.passes_attempted)*100,3)
        
        if self.short_passes_attempted and self.short_passes_completed:
            self.short_pass_completion_percent = round((self.short_passes_completed/self.short_passes_attempted)*100,3)
        
        if self.medium_passes_attempted and self.medium_passes_completed:
            self.medium_pass_completion_percent = round((self.medium_passes_completed/self.medium_passes_attempted)*100,3)

        if self.long_passes_attempted and self.long_passes_completed:
            self.long_pass_completion_percent = round((self.long_passes_completed/self.long_passes_attempted)*100,3)

        if self.expected_assists and self.assists:
            self.assists_vs_expected_assists_difference = round(self.assists - self.expected_assists,3)

        if self.shot_creating_actions:
            self.shot_creating_actions_p90 = round(self.shot_creating_actions/90,3)

        if self.goal_creating_actions:
            self.goal_creating_actions_p90 = round(self.goal_creating_actions/90,3)


        super().save(*args, **kwargs)
    
class DefensiveActions(RegularData):
    players = models.IntegerField()
    tackles_attempted = models.IntegerField()
    tackles_won = models.IntegerField()
    tackle_win_percentage = models.FloatField()
    tackles_made_in_defensive_third = models.IntegerField()
    tackles_made_in_midfield_third = models.IntegerField()
    tackles_made_in_offensive_third = models.IntegerField()
    challenges_made = models.IntegerField()
    challenges_won = models.IntegerField()
    challenges_win_percentage = models.FloatField()
    blocks_made = models.IntegerField()
    shots_blocked = models.IntegerField()
    passes_blocked = models.IntegerField()
    inteceptions_made = models.IntegerField()
    clearences_made = models.IntegerField()
    error_leading_to_shot = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.tackles_won and self.tackles_attempted:
            self.tackle_win_percentage = round((self.tackles_won/self.tackles_attempted)*100,3)
        
        if self.challenges_made and self.challenges_won:
            self.challenges_win_percentage = round((self.challenges_won/self.challenges_made)*100,3)
        
        super().save(*args, **kwargs)

class PossesionStats(RegularData):
    players = models.IntegerField()
    total_touches = models.IntegerField()
    total_touches_in_defensive_penalty_area = models.IntegerField()
    total_touches_in_defensive_third = models.IntegerField()
    total_touches_in_midfield_third = models.IntegerField()
    total_touches_in_offensive_third = models.IntegerField()
    total_touches_in_offensive_penalty_area = models.IntegerField()
    take_ons_attempted = models.IntegerField()
    successful_take_ons = models.IntegerField()
    take_on_success_percentage = models.FloatField()
    tackled_on_take_on = models.IntegerField()
    tackled_on_take_on_percentage = models.FloatField()
    total_carries = models.IntegerField()
    total_distance_carries = models.IntegerField()
    total_progressive_distance_carries = models.IntegerField()
    progressive_carries = models.IntegerField()
    carries_into_final_third = models.IntegerField()
    carries_into_penalty_area = models.IntegerField()
    miscontrols = models.IntegerField()
    dispossesed = models.IntegerField()
    passes_recieved = models.IntegerField()
    # Completed passes that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes,
    # or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch.
    progressive_passes_recieved = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if self.successful_take_ons and self.take_ons_attempted:
            self.take_on_success_percentage = round((self.successful_take_ons/self.take_ons_attempted)*100,3)
        
        super().save(*args, **kwargs)


class MiscStats(RegularData):
    yellow_cards = models.IntegerField()  
    red_cards = models.IntegerField()  
    second_yellow_cards = models.IntegerField()
    fouls_committed = models.IntegerField()
    fouls_drawn = models.IntegerField()
    crosses_attempted = models.IntegerField()
    offsides = models.IntegerField()
    interceptions = models.IntegerField()
    tackles_won = models.IntegerField()
    penalty_kicks_won = models.IntegerField()
    penalty_kicks_conceded = models.IntegerField()
    own_goals = models.IntegerField()
    ball_recoveries = models.IntegerField()
    aerial_duels_attempted = models.IntegerField()
    aerial_duels_won = models.IntegerField()
    aerial_duels_win_percentage = models.FloatField()



