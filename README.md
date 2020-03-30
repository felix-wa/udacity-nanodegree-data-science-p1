# udacity-nanodegree-data-science-p1

**Introduction**

The code is used to generate different figures from the Airbnb data seattle 2017. My motivation was to challenge myselfe with a new kind of work (analysis of large datasets) and in best case to give some advises for host and/or customers that use Airbnb.

**Main Questions**

1. Does the length of the description of a accomodation have an effect on the rating?
2. Is the number of amenities related to the price?
3. Do high ratings go with high prices?

All three questions came up when I initially scrolled over the data and connected my personell impression of Airbnb to it. The first question seems for me the most interesting and (depending on the results) it might give nice insights for a host setting up a new post on Airbnb.

**Used Libaries**

In this project I used _numpy_, _pandas_ and _matplotlib.pyplot_.

**Architecture**

The project is splited in _data_ and _code_.
_data_
The data is stored in a seperate folder structure named data/seattle. This folder contains three csv files including the Airbnb 2017 Seattle dataset.
_code_
The code is stored in one .py file which is optically seperated in fife parts - Comments, Definitions, Question 1, Question 2 and Question 3. All parts work for their own and result in a figure containing the processed data. 

**Results**

The processed data suggest that there are relations between the length of the description and the rating and the price and the rating. The number of amenities does not have an impact on the price.
The analysis of the first question suggests that longer descriptions of accomodations go with better ratings but also that the overall ratings are quite good.
The analysis of the second question shows that there is no direct correlation between the pure number of amenities and the price per person and nicht.
The analysis of the third question shows that there is a relation between the investigated key numbers but the effect is quite low due to the reason that the overall ratings are quite good.

**Challenges and Learnings**

Till not I have made out two main challenges that have changed my way of thinking about data analyzis. Firstly, it took a very long time to understand the raw data and due tu the fact that there was no explenation of the fields, I struggeled a long time identifiing data I was able to use. There are many columns in the data where I could not completely understand what they are for and so I had to drop them for my analysis even if they look very interesting. Secondly, I learned much about the aggregation of data. I aggregated the data on a several ways and gained completely different results for each aggregation. For example I created equidistand bins to sort data in and analyzed it afterwords. This leads to the issue, that there are bins with hunderets of elements and some bins with only two elements. In the further analyzis and the viszalization they had the same weight. Finally I came up with a solution where I created the bins on a way that every bin has the same amount of elements.




