from django.db import models
from django.contrib.auth.models import User


# information about the user, will be obtained from introductory questionnaire
# integers are used to correspond to categories to store information from drop down/choice menus
# therefore the form will prevent impossible answers being entered
class Demographic(models.Model):
    user = models.OneToOneField(User)  # link to user profile
    condition = models.IntegerField()  # allocated condition (A/B)
                                       # (0 = A, 1 = B)
    age_cat = models.IntegerField()  # age category of the user
                                     #  (0 = 0-17, 1 = 18-25, 2 = 26-50, 3 = 50+)
    sex = models.IntegerField()  # sex of user
                                 # (0 = F, 1 = M)
    education = models.IntegerField()  # level of academic education of user
                                       # (0 = High School, 1 = College Diploma/Apprenticeship,
                                       # 2 = Uni Bachelor's/Master's Degree, 3 = PhD or higher)
    subject = models.IntegerField()  # degree/employment subject area of the user
                                     # (0 = Finance, 1 = Business, 2 = Arts, 3 = Engineering, 4 = Health, 5 = IT/CS
                                     # 6 = PR/Marketing, 7 = Construction/Property, 8 = HR, 9 = Science, 10 = logistics,
                                     # 11 = Emergency/Armed Forces, 12 = Voluntary, 13 = Energy/Utilities,
                                     # 14 = Environmental/Agriculture, 15 = Hospitality/Sport, 15 = Law, 17 = Media,
                                     # 18 = Public Sector, 19 = Retail, 20 = Education, 21 = Unemployed/Not Applicable)
    confidence = models.IntegerField()  # level of user's experience/confidence with internet search
                                        # (0 = Little/No Experience, 1 = Apprehensive, 2 = Fairly Confident
                                        # 3 = Highly Experienced/Confident)
    search_freq = models.IntegerField()  # frequency category of use of search engines by user
                                         # (0 = Never used search engine before, 1 = several times per month,
                                         # 2 = several times per week, 3 = several times per day)

    def __unicode__(self):
        return self.user.username


# information about the user's experience of the AB Search App, will be obtained from final questionnaire
# integers are used to correspond to categories to store information from slider menus
# 0 being the lowest and 1 being the highest level of experience
# therefore the form will prevent impossible answers being entered
class Experience(models.Model):
    user = models.OneToOneField(User)  # link to user profile
    ease = models.IntegerField()  # level of ease of use of AB Search App
    boredom = models.IntegerField()  # level of boredom experienced by user when using AB Search App
    rage = models.IntegerField()  # level of rage experienced by user when using AB Search App
    frustration = models.IntegerField()  # level of frustration experienced by user when using AB Search App
    excitement = models.IntegerField()  # level of excitement experienced by user when using AB Search App
    indifference = models.IntegerField()  # level of indifference experienced by user when using AB Search App
    confusion = models.IntegerField()  # level of confusion experienced by user when using AB Search App
    anxiety = models.IntegerField()  # level of anxiety experienced by user when using AB Search App
    comment = models.TextField()  # any additional comments the user wishes to add about their
                                  # experience of the AB Search App

    def __unicode__(self):
        return self.user.username

