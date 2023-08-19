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
    
class PlaytimeStats(RegularData):
    pass    

class MiscStats(RegularData):
    pass    


