# Mohamed Moussa count

Analyzing the number of people with my name on LinkedIn along with spelling patterns

## Purpose

Both my first name, Mohamed, as well as my last name, Moussa, are fairly common names. However, they both have multiple variations on their spelling in English due to their Arabic origins. For a long time I've wondered how many people there are with the same name as me, regardless of spelling. Additionally, I was curious to know what the most common variations were. One day I was bored so I decided to try to answer these questions.

## Methodology

In an ideal situation, one could look at birth and death records for every individual in the world and determine exactly how many people with my name were alive at any time, but this method is far from practical. I decided to restrict my search to individuals using LinkedIn. Admittedly, this heavily restricts the counts I determine because a majority of the world's population does not use LinkedIn. Additionally, the data is skewed because some countries likely to use certain spellings have a much larger percentage of their population using LinkedIn than other countries with different spellings. For example, a lower percentage of individuals living in the MENA region use LinkedIn than individuals living in North America. Individuals in the MENA region can be expected to use the Arabic spelling of their name more often than individuals in North America due to the difference in primary language. With all of this taken into consideration, this little investigation is clearly not representative of the full sample population, but the investigation is just for fun to satisfy my own curiosity so I'll accept the limitations.

In order to find out how many people with a given first and last name were on LinkedIn, I did a search in LinkedIn's public directory and then looked at the result count. I wrote `linkedinMe.py` to automate generating combinations of first and last names, searching them, and then finally scraping the result page to get the number of results.

## Results

The output from `linkedinMe.py`, showing the number of results per spelling and a final total, is below:

```
محمد موسى: 93
Mohamed Moussa: 561
Mohamed Mousa: 395
Mohamed Musa: 234
Mohammed Moussa: 103
Mohammed Mousa: 183
Mohammed Musa: 329
Mohamad Moussa: 60
Mohamad Mousa: 24
Mohamad Musa: 36
Mohammad Moussa: 46
Mohammad Mousa: 138
Mohammad Musa: 110
Muhamad Moussa: 1
Muhamad Mousa: 3
Muhamad Musa: 28
Muhammad Moussa: 19
Muhammad Mousa: 24
Muhammad Musa: 375
Muhamed Moussa: 2
Muhamed Mousa: 1
Muhamed Musa: 5
Muhammed Moussa: 8
Muhammed Mousa: 3
Muhammed Musa: 65
Moohammed Moussa: 0
Moohammed Mousa: 0
Moohammed Musa: 0
Mahmad Moussa: 0
Mahmad Mousa: 0
Mahmad Musa: 1
Mehmed Moussa: 0
Mehmed Mousa: 0
Mehmed Musa: 1
Mahamed Moussa: 0
Mahamed Mousa: 1
Mahamed Musa: 4
Mahammed Moussa: 0
Mahammed Mousa: 0
Mahammed Musa: 1
Muhamet Moussa: 0
Muhamet Mousa: 0
Muhamet Musa: 4
Muhammet Moussa: 0
Muhammet Mousa: 0
Muhammet Musa: 0
Mahammud Moussa: 0
Mahammud Mousa: 0
Mahammud Musa: 0
Mehmet Moussa: 0
Mehmet Mousa: 0
Mehmet Musa: 6
Mohd Moussa: 0
Mohd Mousa: 10
Mohd Musa: 196
Muh Moussa: 0
Muh Mousa: 0
Muh Musa: 3
Mahamid Moussa: 0
Mahamid Mousa: 0
Mahamid Musa: 0
Md Moussa: 2
Md Mousa: 1
Md Musa: 80

Total: 3156
```

According to these results, there are 3155 people that share my name on LinkedIn. The most popular spelling among those people is "Mohamed Moussa", which happens to be how my name is spelled.
