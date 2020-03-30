    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_calendar = pd.read_csv('./Data/seattle/calendar.csv')
df_listings = pd.read_csv('./Data/seattle/listings.csv')
df_reviews = pd.read_csv('./Data/seattle/reviews.csv')

#############################################################################
########################## MAIN QUESTIONS TO ANSWER #########################
#############################################################################

# 1. Does the length of the description of a accomodation have an effect on the rating?
#       - more detailed description makes clear what to expect
#       - no suprises in/at the location
#       - is there a difference in the rating of the 'accuracy' compared to the
#         rest?

# 2. Is the number of amenities related to the price?
#       - if it is correlated it might suggest that well equipped accomodations
#         are more often booked and the owner were able to adjust their prices 

# 3. Do high ratings go with high prices?
#       - If it is correlated it is possible that well owners know that their
#         accomodations are nice and adjust the price
#
############################################################################
############################################################################

#Question 1 remarks:

# Since we do not see a history of the accomodation description I assume that the 
# overall length is not changed over time drasticly.

#if there is no value in the description (==NAN) I set the length to 0

# for this analysis we use six different review categories that are shown in the profile
# named 'accuracy', 'cleanlineness', 'checkin', 'communication', 'location'
# and 'value'
# in a second step we analyze the length of the description only on the rating
# of the 'accuracy' where I expece a higher impact than on the general rating 

# I dropped all rows, where more than 50% of the review data was missing, the 
# other fields I filled with the mean of the other rows

# I filled the data in equidistant bins to receive a nice plot that is not
# overloaded
# 
############################################################################
############################################################################

# read in relevant information in df_Q1_information
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

print(df_Q1_information.head())

# dropping of rows, drop all rows where we can not find at least 6 NON NA values
# this step sorts out these rows, that have
df_Q1_information.dropna(thresh = 6,axis=0, inplace = True);

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
# To reduce the number of dots in the figure -> create bins and aggregate
#number of bins
nbr_of_bins = 30
#including bins in dataframe
df_Q1_information['bin'] = pd.cut(df_Q1_information['length_of_desc'], nbr_of_bins)

#aggredating data for plt
df_plt = df_Q1_information[['bin', 'length_of_desc', 'review_scores_mean']].groupby('bin').mean().dropna().reset_index()
############################################################################
# Interesting key numbers (nice to get a feeling of the avg size of an desc)
# For comparison: A DinA4 page contains roughly 2500 letters
#print('Average number of letters per description:',df_Q1_information['length_of_desc'].mean())
############################################################################
#plot grafic with bins
plt.figure()
# set size of figure
plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
#set type of plt 
plt.scatter(df_plt['length_of_desc'], df_plt['review_scores_mean'], color = 'black')
# change limits of y-axis to make figure nice
plt.ylim(9.1,10.1)

#Labeling
plt.title('Influence of the length on the evaluation')
plt.ylabel('Rating of accomodation')
plt.xlabel('Length in letters')
#delete black box around figure
plt.box(False)
# delete ticks at the axis
plt.tick_params(axis='x', which='both', bottom=False, top=False, right = False, left = False, labelbottom=True) 
plt.tick_params(axis='y', which='both', bottom=False, top=False, right = False, left = False, labelbottom=False) 
# Add correlation line
axes = plt.gca()
# calculate relevant values for regression
m, b = np.polyfit(df_plt['length_of_desc'], df_plt['review_scores_mean'], 1)
# incline m gives an impression of the change
#print('incline of regression in general:',m)
# include regression in plt
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
plt.plot(X_plot, m*X_plot + b, '--', color = 'black')
#
#############################################################################
# THE NEXT PART USES ONLY THE review_accuracy score
#df_plt = df_Q1_information[['bin', 'length_of_desc', 'review_scores_accuracy']].groupby('bin').mean().dropna().reset_index()
##plot grafic with bins
#plt.figure()
#plt.scatter(df_plt['length_of_desc'], df_plt['review_scores_accuracy'], color = 'black')
#plt.ylim(9.1,10.1)
##Labeling
#plt.title('Influence of the length on the evaluation')
#plt.ylabel('Rating of accomodation')
#plt.xlabel('Length in letters')
#plt.box(False)
## Add correlation line
#axes = plt.gca()
#m, b = np.polyfit(df_plt['length_of_desc'], df_plt['review_scores_accuracy'], 1)
#print('incline of regression in accuracy:',m)
#X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
#plt.plot(X_plot, m*X_plot + b, '--', color = 'black')



############################################################################
############################################################################
########################### QUESTION 2 #####################################
############################################################################
############################################################################
# 2. Is the number of amenities related to the price?
#
#Question 2 remarks:
#
# I assume, that an average stay in an Airbnb is 3 nights what seems to be a 
# lower bound for the length og the stay (http://insideairbnb.com/about.html)
#
# Since we need to find an price per bed per night I assume an average stay of 
# 3 nights and the price per night is calculated as follows:
# price_night = (3*price+cleaning_fee)/3/beds
#
# I do not seperate the amenities, I calculate the number of those
#
# I deleted those accomodations where the price per night for each bed was higher
# than 400 Dollar. The plott suggests that they are outliers.
# The same holds for accomodations with moren than 25 amenities 
# I implemented a switch called 'show_outliers_Q2' to be able to show them
# The outliers would support my arguments even more but seem to be wrong

#read in relevant information
df_Q2_information = df_listings[['price', 'cleaning_fee', 'beds', 'amenities']]
# generate necessary columns
df_Q2_information['nbr_of_amenities'] = np.nan;#0
df_Q2_information['price_per_bed_night'] = np.nan;#0
# prepare columns to make cleaning later on more easy
# I assume that a NAN value in the 'cleaning_fee' column means that there is non
df_Q2_information['cleaning_fee'] = df_Q2_information['cleaning_fee'].fillna('$0.00') # for later deletion
# dropping of rowswithout price, bed or amenities
# we cna not use there rows in the analysis and there is no proper way to fill them
df_Q2_information.dropna(subset = ['price', 'beds', 'amenities'],axis=0, inplace = True)

#
for index, row in df_Q2_information.iterrows():
    nbr_of_amen = int(len(row['amenities'].split(",")))
    df_Q2_information.set_value(index,'nbr_of_amenities',nbr_of_amen)
    # Delete '$' AND '.00' AND the ',' that seperates tousands
    price_no_dollar = int(row['price'][1::][:-3].replace(",",""))
    #df_Q2_information.set_value(index,'price',price_no_dollar)
    df_Q2_information.at[index,'price'] =price_no_dollar
    
    # Delete '$' AND '.00' AND the ',' that seperates tousands
    fee_no_dollar = int(row['cleaning_fee'][1::][:-3].replace(",",""))
    #df_Q2_information.set_value(index,'cleaning_fee',fee_no_dollar)
    df_Q2_information.at[index,'cleaning_fee'] = fee_no_dollar
    
    #calculate the relevant number (price per bed and night)
    nbr_of_beds = row['beds']
    price_per_bed__night = (price_no_dollar*3+fee_no_dollar)/3/nbr_of_beds
    #df_Q2_information.set_value(index,'price_per_bed_night',price_per_bed__night)
    df_Q2_information.at[index,'price_per_bed_night'] = price_per_bed__night
 
###############################
# this part allows to show outliers in figure
    # more explenation about the exclusion follows below
show_outliers_Q2 = False
if (show_outliers_Q2):
    price_per_b_n_outlier = 10000
    nbr_amen_outlier = 100
else:
    price_per_b_n_outlier = 400  
    nbr_amen_outlier = 25
###############################    
    
# a price of more than price_per_b_n_outlier Dollar per night suggests to be an outliers
df_Q2_information = df_Q2_information[df_Q2_information['price_per_bed_night']<price_per_b_n_outlier]
#the plott suggests, that the accomodations with more amenities are outliers
df_Q2_information = df_Q2_information[df_Q2_information['nbr_of_amenities']<nbr_amen_outlier]

# in the following we create bins to generate nice and clean plots
#number of bins = max number of amenities
nbr_of_bins_Q2 = 30
#including bins in dataframe
df_Q2_information['bin'] = pd.cut(df_Q2_information['price_per_bed_night'], nbr_of_bins_Q2)
# grouping the information according to the bins
df_Q2_information = df_Q2_information[['bin', 'nbr_of_amenities', 'price_per_bed_night']].groupby('bin').mean().dropna().reset_index()

# plotting the figure:
plt.figure()
# setting the size of the figure
plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
# selecting type of figure
plt.scatter(df_Q2_information['price_per_bed_night'], df_Q2_information['nbr_of_amenities'], color = 'black')

#calculating regression values
axes = plt.gca()
m, b = np.polyfit(df_Q2_information['price_per_bed_night'], df_Q2_information['nbr_of_amenities'], 1)
#print('incline of regression in accuracy Q2:',m)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
#labeling the figure
plt.title('Influence of number of amenities on price')
plt.ylabel('Number of amenities')
plt.xlabel('Price per person per night in US$')
#deleting the black box around the figures
plt.box(False)
#deleting the ticks at the axis
plt.tick_params(axis='x', which='both', bottom=False, top=False, right = False, left = False, labelbottom=True) 
plt.tick_params(axis='y', which='both', bottom=False, top=False, right = False, left = False, labelbottom=False) 
#blotting the regression
plt.plot(X_plot, m*X_plot + b, '--', color = 'black')



############################################################################
############################################################################
########################### QUESTION 3 #####################################
############################################################################
############################################################################
# 3. Do high ratings go with high prices?
#       - If it is correlated it is possible that well owners know that their
#         accomodations are nice and adjust the price per person per night
#
#Question 3 remarks:

#reading in relevant information
df_Q3_information =  df_listings[['price'
                                  , 'cleaning_fee'
                                  , 'beds'
                                  , 'review_scores_accuracy'
                                  , 'review_scores_cleanliness'
                                  , 'review_scores_checkin'
                                  , 'review_scores_communication'
                                  , 'review_scores_location'
                                  , 'review_scores_value']]

#preparing data for data cleaning
df_Q3_information['cleaning_fee'] = df_Q3_information['cleaning_fee'].fillna('$0.00') # for later deletion
# dropping of rows, drop all rows where we can not find at least 6 NON NA values
df_Q3_information.dropna(thresh = 6,axis=0, inplace = True)

# calculate mean value of reviews
mean_Q3 = df_Q3_information[
        ['review_scores_accuracy',
         'review_scores_cleanliness',
         'review_scores_checkin',
         'review_scores_communication',
         'review_scores_location',
         'review_scores_value']].mean(axis=1)

# fill NA values
for i, row in enumerate(df_Q3_information):
    df_Q3_information.iloc[:, i].fillna(mean_Q3, inplace=True)

# average mean does not change due to replacing nan
df_Q3_information['review_scores_mean'] = mean
df_Q3_information['price_per_bed_night'] = 0

# this loop cleans cleans the data and generates the necesarry key values
for index, row in df_Q3_information.iterrows():
    # Delete '$' AND '.00' AND the ',' that seperates tousands
    price_no_dollar = int(row['price'][1::][:-3].replace(",",""))
    #df_Q3_information.set_value(index,'price',price_no_dollar)
    df_Q3_information.at[index,'price'] = price_no_dollar
    
    # Delete '$' AND '.00' AND the ',' that seperates tousands
    fee_no_dollar = int(row['cleaning_fee'][1::][:-3].replace(",",""))
    #df_Q3_information.set_value(index,'cleaning_fee',fee_no_dollar)
    df_Q3_information.at[index,'cleaning_fee'] = fee_no_dollar
    
    #calculate the relevant number (price per bed and night)
    nbr_of_beds = row['beds']
    price_per_bed__night = (price_no_dollar*3+fee_no_dollar)/3/nbr_of_beds
    #df_Q3_information.set_value(index,'price_per_bed_night',price_per_bed__night)
    df_Q3_information.at[index,'price_per_bed_night'] = price_per_bed__night

df_Q3_information.drop(columns = {'price', 
                                  'cleaning_fee', 
                                  'beds', 
                                  'review_scores_accuracy',
                                  'review_scores_cleanliness',
                                  'review_scores_checkin',
                                  'review_scores_communication',
                                  'review_scores_location',
                                  'review_scores_value'
                                  }, inplace = True)

###############################
# this part allows to show outliers in figure
# more explenation about the exclusion follows below
show_outliers_Q3 = False
if (show_outliers_Q3):
    price_per_b_n_outlier = 10000
else:
    price_per_b_n_outlier = 400  
###############################  

# a price of more than price_per_b_n_outlier Dollar per night suggests to be an outliers
df_Q3_information = df_Q3_information[df_Q3_information['price_per_bed_night'] < price_per_b_n_outlier]

# in the following we create bins to generate nice and clean plots
#number of bins
nbr_of_bins_Q3 = 30
#including bins in dataframe
df_Q3_information['bin'] = pd.cut(df_Q3_information['price_per_bed_night'], nbr_of_bins_Q3)

# grouping the data by the bins
df_Q3_information = df_Q3_information[['bin', 'price_per_bed_night', 'review_scores_mean']].groupby('bin').mean().dropna().reset_index()

# create figure
plt.figure()
# set size of figure
plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
#select type of figure and data
plt.scatter(df_Q3_information['price_per_bed_night'], df_Q3_information['review_scores_mean'], color = 'black')
# calculate relecant values for regression
axes = plt.gca()
m, b = np.polyfit(df_Q3_information['price_per_bed_night'], df_Q3_information['review_scores_mean'], 1)
#print('incline of regression in accuracy Q3:',m)
X_plot = np.linspace(axes.get_xlim()[0],axes.get_xlim()[1],100)
# label figure
plt.title('Relation between rating and price')
plt.ylabel('Rating of accomodation')
plt.xlabel('Price per person per night in US$')
# delete black box around figure
plt.box(False)
# delete ticks at the axis
plt.tick_params(axis='x', which='both', bottom=False, top=False, right = False, left = False, labelbottom=True) 
plt.tick_params(axis='y', which='both', bottom=False, top=False, right = False, left = False, labelbottom=False) 
#plot regression
plt.plot(X_plot, m*X_plot + b, '--', color = 'black')






