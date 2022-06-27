# Ranking Tennis Player's Based on Career Stats

## Data Collection  
I scraped different statistics for the top 80 male tennis players on tour at the moment off of [the ATP tour website](https://www.atptour.com/). The data contains a player's serving statistics, such as the amount of service games they have won in their career, and returning statistics (when a player is returning a serve) such as the amount of return games they have won in their career.

## Developing Ranking
I started by averaging values that weren't percentages, such as total return games won per year. A player with a 20 year long career will definetly appear better than a player with only 6 years on tour without averaging. Some other transformations were done as well.
### Best Servers
The best server score I developed was a combination of several metrics, which were normalized to fit in a range of 0 to 1.
![Best Serve](/visuals/serve.png)

### Best Returners of Serve
The best return score I developed was a combination of several metrics, which were normalized to fit in a range of 0 to 1.
![Best Return](/visuals/return.png)

### Best Players according to my Metrics
I simply averaged the return and serve score to get the best players.
![Best Player](/visuals/best.png)
