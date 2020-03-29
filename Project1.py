

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
#import ImputingValues as t
import seaborn as sns


df_calendar = pd.read_csv('./Data/calendar.csv')
df_listings = pd.read_csv('./Data/listings.csv')
df_reviews = pd.read_csv('./Data/reviews.csv')

#test1 = df_calendar['available'] == 't'
#test2 = df_calendar['price'] == np.nan

#t = df_calendar[(df_calendar['available'] == 't') & (df_calendar['price'] == np.nan)]

############################################################################
############################################################################

#############################################################################
########################## MAIN QUESTIONS TO ANSWER #########################
#############################################################################

# 1. Does the length of the description of a accomodation have an effect on the rating?
#       - more detailed description makes clear what to expect
#       - no suprises in/at the location
#       - is there a difference in the rating of the 'accuracy' compared to the
#         rest?

# 2. Does a host who has run through the ideitification process [host_identity_verified]
#    and/or presents several verifications [host_verifications] a higher utilization?
#       - more trust in the host

# 3. Do positive review scores have an impact on bookings and how many of the guests
#    do rate the accomodation?
#       - is it worth to put some extra efford as host to receive a review?
#       - 

############################################################################
############################################################################

#Question 1:

# Since we do not see a history of the accomodation description I assume that the 
# overall length is not changed over time drasticly.

# experiences_offered is alsways none

#if there is no value (==NAN) I set the values to 0

# for this analysis we use six different categories that are shown in the profile
# named 'accuracy', 'cleanlineness', 'checkin', 'communication', 'location'
# and 'value'
# in a second step we analyze the length of the description only on the rating
# of the 'accuracy' and compare it to the rating of the rest due to the fact
# that I state that the accuraxy should be affected most.

# I dropped all rows, where more than 50% of the review data was missing, when
# it was less than 50% I filled the rows with the mean of the other rows, than
# does not have an effect on the mean of the reviews at all but helps in the
# analyzis where we compare accuracs vs the rest
############################################################################
############################################################################

# rean in relevant information in df_Q1_information
df_Q1_information =  pd.DataFrame(
        {'length_of_desc' : df_listings['summary'].str.len().fillna(0)+
      df_listings['space'].str.len().fillna(0)+
      df_listings['description'].str.len().fillna(0)+
      df_listings['neighborhood_overview'].str.len().fillna(0)+
      df_listings['notes'].str.len().fillna(0)+
      df_listings['transit'].str.len().fillna(0),
       'review_scores_accuracy' : df_listings['review_scores_accuracy'],
       'review_scores_cleanliness' : df_listings['review_scores_cleanliness'],
       'review_scores_checkin' : df_listings['review_scores_checkin'],
       'review_scores_communication' : df_listings['review_scores_communication'],
       'review_scores_location' : df_listings['review_scores_location'],
       'review_scores_value' : df_listings['review_scores_value']
       }, columns = ['length_of_desc',
        'review_scores_accuracy',
        'review_scores_cleanliness',
        'review_scores_checkin',
        'review_scores_communication',
        'review_scores_location',
        'review_scores_value'])

# dropping of rows, drop all rows where we can not find at least 6 NON NA values
df_Q1_information.dropna(thresh = 6,axis=0, inplace = True)

# calculate mean value of reviews
mean = df_Q1_information[
        ['review_scores_accuracy',
         'review_scores_cleanliness',
         'review_scores_checkin',
         'review_scores_communication',
         'review_scores_location',
         'review_scores_value']].mean(axis=1)

# fill NA values
for i, row in enumerate(df_Q1_information):
    df_Q1_information.iloc[:, i].fillna(mean, inplace=True)

# average mean does not change due to replacing nan
df_Q1_information['review_scores_mean'] = mean












