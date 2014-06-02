__author__ = 'Craig'

import os

def populate():
    # add the users for testing
    dave = User.objects.create_user('Dave', 'dave@dave.com', 'davepw')
    john = User.objects.create_user('John', 'john@john.com', 'johnpw')
    stan = User.objects.create_user('Stan', 'stan@stan.com', 'stanpw')

    # now add their sample demographics
    dave_demographic = add_demographic(dave, 1, 1, 1, 4, 7, 2, 3)
    john_demographic = add_demographic(john, 1, 2, 1, 2, 15, 3, 2)
    stan_demographic = add_demographic(stan, 0, 3, 1, 3, 4, 2, 3)

    # and their sample experiences
    dave_experience = add_experience(dave, 7, 4, 6, 7, 4, 5, 1, 3, 'Great app, really easy to use')
    john_experience = add_experience(john, 8, 2, 7, 5, 3, 1, 1, 2, 'A little slow at time but otherwise fine')
    stan_experience = add_experience(stan, 5, 5, 6, 7, 5, 6, 7, 8, 'I found this really confusing and hard to use')


# function to add each user's demographic
# assuming the demographics entered in the questionnaire have already been converted to the integer format
# and condition has been randomly allocated on creation of account
def add_demographic(user, condition, age_cat, sex, education, subject, confidence, search_freq):
    d = Demographic.objects.get_or_create(user=user, condition=condition, age_cat=age_cat, sex=sex,
                                          education=education, subject=subject, confidence=confidence,
                                          search_freq=search_freq)
    print 'adding demographic for: ' + str(user)
    return d[0]


# function to add each user's experience of the App
# assuming the experience entered in the questionnaire have already been converted to the integer format
def add_experience(user, ease, boredom, rage, frustration, excitement, indifference, confusion, anxiety, comment):
    e = Experience.objects.get_or_create(user=user, ease=ease, boredom=boredom, rage=rage, frustration=frustration,
                                         excitement=excitement, indifference=indifference, confusion=confusion,
                                         anxiety=anxiety, comment=comment)
    print 'adding Experience for ' + str(user)
    return e[0]


if __name__ == '__main__':
    print "Starting AB Search App population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ABSearch.settings')
    from ABSearchApp.models import User, Demographic, Experience
    populate()