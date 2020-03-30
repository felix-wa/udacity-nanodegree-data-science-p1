# udacity-nanodegree-data-science-p1

**Introduction**
The code is used to generate different figures from the Airbnb data seattle 2017. My motivation was to challenge myselfe with a new kind of work (analysis of large datasets) and in best case to give some advises for host and/or customers that use Airbnb.

**Main Questions**
1. Does the length of the description of a accomodation have an effect on the rating?
2. Is the number of amenities related to the price?
3. Do high ratings go with high prices?

All three questions came up when I initially scrolled over the data and connected my personell impression of Airbnb to it. The first question seems for me the most interesting and (depending on the results) it might give nice insights for a host setting up a new post on Airbnb.

**Used libaries**
In this project I used _numpy_, _pandas_ and _matplotlib.pyplot_.

**Architecture**
The project is splited in _data_ and _code_.
_data_
The data is stored in a seperate folder structure named data/seattle. This folder contains three csv files including the Airbnb 2017 Seattle dataset.
_code_
The code is stored in one .py file which is optically seperated in four parts - Comments, Question 1, Question 2 and Question 3. All parts work for their own and result in a figure containing the processed data. 

**Results**
The processed data suggest that for all three questions there is a relation between the analyzed key numbers.
The analysis of the first question suggests that longer descriptions of accomodations go with better ratings but also that the overall ratings are quite good.
The analysis of the second question shows that there is a relation between the price per bed and night and the pure number of amenities.
The analysis of the third question shows that there is a relation between the investigated key numbers but the effect is quite low due to the reason that the overall ratings are quite good.

