# udacity-nanodegree-data-science-p1

**Introduction**

The code is used to generate different figures from the Airbnb data Seattle 2017. My motivation was to challenge myself with a new kind of work (analysis of large data sets) and in best case to give some advises for host and/or customers that use Airbnb.

**Main Questions**

1. Does the length of the description of a accommodation have an effect on the rating?
2. Is the number of amenities related to the price?
3. Do high ratings go with high prices?

All three questions came up when I initially scrolled over the data and connected my personnel impression of Airbnb to it. The first question seems for me the most interesting and (depending on the results) it might give nice insights for a host setting up a new post on Airbnb.

**Used Libaries**

In this project I used _numpy_, _pandas_ and _matplotlib.pyplot_.

**Architecture**

The project is divided in _data_ and _code_.
_data_
The data is stored in a separate folder structure named data/seattle. This folder contains three csv files including the Airbnb 2017 Seattle data set.
_code_
The code is stored in one .py file which is optically separated in fife parts - Comments, Definitions, Question 1, Question 2 and Question 3. All parts work for their own and result in a figure containing the processed data.

**Results**

The processed data suggest that there are relations between the length of the description and the rating and the price and the rating. The number of amenities does not have an impact on the price.
The analysis of the first question suggests that longer descriptions of accommodations go with better ratings but also that the overall ratings are quite good.
The analysis of the second question shows that there is no direct correlation between the pure number of amenities and the price per person and night.
The analysis of the third question shows that there is a relation between the investigated key numbers but the effect is quite low due to the reason that the overall ratings are quite good.

**CRISP-DM**

_Business_ _understanding_: 

	What is the goal for each participant in the process?
        - Airbnb: Is the platform that allows hosts to advertise accommodations and receives a share of the overall accommodation costs. They set up a reviewing process that allows to share impressions over guests and accommodations
        - Host: The host advertises its accommodation by its own and is willing to have high utilization.
        - Guest: The guest is willing to find a suitable accommodation at reasonable cost
    I focus on the hosts and the guests and show interesting possibilities how they can improve
   
_Data_ _understanding_: 

	What kind of data do we have?
    In general we have three different data sets where each of them contains various information. In my preanalysis I worked thru the data and came up with the main questions raised above in the part _Main_ _Questions_
   
_Prepare _Data_:

    In the data preparation I had to clear some of the data. In detail I did the following steps:
        - Filling up or deleting rows: Using the reviews of the accommodation I searched them for missing values. If there were more than 50% (at least 4 out of 6) I filled the missing values with the mean of the existing values, otherwise I deleted the rows. Overall the number of               dropped rows was minimal but to me it made sense to drop those with minimal information rather than extrapolate a small number of reviews for different categories
        - plotting the raw data and look for outliers. In my analysis I found some extrem outliers (e.g. there was one accommodation with nightly costs of more than 400 US$ per person per night) and excluded them from the plotting
       
_Evaluate_ _the_ _Results_
   
    I presented figures where I aggregated the data to several bins. For the evaluation I played around with the size of the bins and checked whether the arguments I worked out hold or if I have to rethink them.
   

**Challenges and Learnings**

Till not I have made out two main challenges that have changed my way of thinking about data analysis. Firstly, it took a very long time to understand the raw data and due to the fact that there was no explanation of the fields, I struggled a long time identifying data I was able to use. There are many columns in the data where I could not completely understand what they are for and so I had to drop them for my analysis even if they look very interesting. Secondly, I learned much about the aggregation of data. I aggregated the data on a several ways and gained completely different results for each aggregation. For example I created equidistant bins to sort data in and analyzed it afterwords. This leads to the issue, that there are bins with hundreds of elements and some bins with only two elements. In the further analysis and the visualization they had the same weight. Finally I came up with a solution where I created the bins on a way that every bin has the same amount of elements.





