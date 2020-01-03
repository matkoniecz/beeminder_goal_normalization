import time
import datetime
from pyminder.pyminder import Pyminder

def main():
    validate_settings()

def token():
    return open("token.secret").read()

def validate_settings():
    pyminder = Pyminder(user='[your username - dummy field]', token=token())

    goals = pyminder.get_goals()

    for goal in goals:
        # Goal objects expose all API data as dynamic properties.
        # http://api.beeminder.com/#attributes-2

        if(goal.runits != "d"):
            print("goal", goal.slug, "has rate set to something other than daily")
        if(goal.secret != True):
            print("goal", goal.slug, "is not set to be secret")
        if(goal.datapublic != False):
            print("goal", goal.slug, "is not set to have secret datapoints")
        
        print()
        print(goal.slug)
        print(goal.fineprint)
        """
        deadline (number): Seconds by which your deadline differs from midnight.
        Negative is before midnight, positive is after midnight. Allowed range is -17*3600 to 6*3600 (7am to 6am).

        leadtime (number): Days before derailing we start sending you reminders.
        Zero means we start sending them on the eep day, when you will derail later that day.

        alertstart (number): Seconds after midnight that we start sending you reminders
        (on the day that you're scheduled to start getting them, see leadtime above).
        """
        if(goal.deadline < 0):
            print("goal", goal.slug, "has deadline BEFORE midnight")


        # Goal objects also implement a handful of helper functions.
        # Note: These functions probably contain bugs! Issues & pull requests welcome.
        # https://github.com/narthur/pyminder/blob/master/pyminder/goal.py
        now = time.time()
        sum_ = goal.get_data_sum(now)
        needed = goal.get_needed(now)

main()