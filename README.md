# Microsoft Movie Studios:
## Preliminary Case Study

<img src='images/Wonder_Woman_(2017_film).jpg' width = '%' />

[Medium Blog Post](https://medium.com/@kekay0528/my-first-data-science-project-94aa5b02709d)

[Presentation PDF](https://github.com/kailakay/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Microsoft%20Movie%20Studio%20Presentation.pdf)

[Video Walkthrough](https://voicethread.com/share/14445223/)

## Purpose
Microsoft has hired a team of green Data Scientists to evaluate various aspects of the movie industry in the hopes of finding their next big venture. Armed with a few starter data sets on box office information, we are tasked to perform preliminary analysis and interpret what types of movies Microsoft Studios should focus on creating. 
<!------------------------------------------>
### Data Description

<details><summary style="font-size: 18px"> 
List of Files:</summary> 

```
|-bom.movie_gross.csv.gz
|-imdb.name.basics.csv.gz
|-imdb.title.akas.csv.gz
|-imdb.title.basics.csv.gz
|-imdb.title.crew.csv.gz
|-imdb.title.principals.csv.gz
|-imdb.title.ratings.csv.gz
|-rt.movie_info.tsv.gz
|-rt.reviews.tsv.gz
|-tmdb.movies.csv.gz
|-tn.movie_budgets.csv.gz
```
</details>
<!------------------------------------------>

### Main Questions:

[Question 1 Notebook Link](https://github.com/kailakay/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Question%201%20L.ipynb)
<details><summary style="font-size: 24px">
Question 1: {What are the most popular genres?} </summary> 

```
In order to fully explore the popularity of genre, we wanted to answer three sub-questions:

- What genres are the most popular for consumers?
- Are more popular genres higher grossing?
- Does the production budget correlate to the popularity of a genre?
```

#### Tables Used:

```
|The Movie Database - tmdb.movies.csv.gz
```
#### EDA

Utilizing *The Movie Database* dataset, we were able to extract genre ID keys and pair them with genre names by utilizing an API key to pull in information from their website. *The Movie Database* has its own formula for calculating popularity that includes factors such as daily views and votes, the number of times a movie was favorited, and the release date - among others. 

We then used this quanititative popularity score per movie and extracted the respective genres. After grouping the data by genre, we then calculated the mean popularity of our correlated data set to create the table below. 

<img src='images/q1-genre-pop-all.png'/>

We filtered that data down to the top 9 genres, and compared them side by side in a boxen chart with a scattered bar chart. These two charts allowed us to visualize the data most comprehensively.

*On the left plot, the black lines show the median while the blue line shows the mean.*

<img src='images/q1-top-9-genre-pop.png'/>

Finally, we linked this data with our cleaned finance data, which allowed us to look directly at the finance information of the most popular genres.  

<img src='images/q1-genre-pop-fin.png' />

#### Conclusion

After cleaning and exploring the data, we found that **Action** was the most popular genre among consumers, followed by **Animation** and **Drama**. We also found that generally, popular genres were also lucrative financially - with a few outlying instances that showed higher rates of hit or miss such as Drama or the Thriller and Horror genres. 

#### Recommendation

While we do not recommend basing business decisions solely off of the popularity of a genre, the data indicates that we can generally assume popular genres are a safe investment. 

</details>

<!------------------------------------------>
[Question 2 Notebook Link](https://github.com/kailakay/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Question%202.ipynb)

<details><summary style="font-size: 24px">
Question 2:  {What are the top performing genres financially?} </summary> 

```
In order to fully explore the aspects of crew on film success, we wanted to answer two sub-questions:

- Does staffing the production with more writers or directors influence profit?
- Is there an optimal writer/director ratio for maximizing profitability?
```

### Tables Used:

```
|Internet Movie Database - imdb.title.basics.csv.gz
|Box Office Mojo - bom.movie_gross.csv.gz
|The Internet Movie Database - tn.movie_budgets.csv.gz
```

### EDA

We started by cleaning our data and combining the relevant information into one table. We then broke down all of the information by genre, and calculated the ROI per movie based off of the financial information that we were provided. 

<img src='images/q2-genre-fin-info.png' />

After charting the mean gross for each of the 19 genres that were in our database, we then graphed the top 7 grossing genres by mean - as seen below:

<img src='images/q2-top-7-genres.png' width='55%' height='50%' />

Next, we looked at the mean production budget by genre in order to investigate the correlation of the production budget to the gross. As you can see below, the 5 genres that had the highest production budget also showed up in the top 7 grossing genres. 

<img src='images/q2-genre-budget.png' width='50%' height='50%' />

Finally, we calculated the mean ROI per genre and graphed the top 6 grossing genres by ROI using a violin plot, shown below.

The width of the plot indicates the proportion of instances that lie within that range, the black line shows the distribution of the interquartile range, while the white dot shows the median of the data. 

<img src='images/q2-roi-violin.png' />

### Conclusion

We were interested to see that the **Science Fiction** genre was not relatively popular among consumers in our dataset, but that it showed as a positive financial prospect. I believe that in order to further interpret this data, we would need to broaded our datasets in regards to both finances and genre popularity.

However, we also noted that while **Action** was highly popular, it's likely that those high popularity ratings are inclinated towards high budget films. 

### Recommendation

While financial information does not showcase the entire picture in terms of success, our data shows that **Animation** has the most financial promise with an average ROI of 145%, while **Musicals** should be saved for niche audiences. 

</details>
<!------------------------------------------>

[Question 3 Notebook Link](https://github.com/kailakay/dsc-mod-1-project-v2-1-onl01-dtsc-ft-041320/blob/master/Question%203%20P.ipynb)

<details><summary style="font-size: 24px">
Question 3: {Does crew size have an impact on a films success?} </summary> 

```
In order to fully explore the financial aspects by genre, we wanted to answer three sub-questions:

- What are the mean production budgets and gross per genre?
- Does production budget impact overall gross?
- What is the Return of Investment(ROI) per genre?
```

### Tables Used:

```
|Internet Movie Database - imdb.title.basics.csv.gz
|Internet Movie Database - imdb.title.crew.csv.gz
```

### EDA

After joining the databases, we were able to match director and writer constructor codes to their respective movies by title name. We then filtered the database by genre as indicated in the table below. 

<img src='images/q3-dw-title.png' width='90%'/>

Following that, we broke down the directors and writers column values into strings, and then added respective columns that valued the count of directors and writers per movie. 

<img src='images/q3-dw-count.png' width='90%'/>

We then merged in the Basics dataframe to join the genres, and saw that films with only one director accounted for 90.9% of our data, and that combinations of 1-4 writers were also over 90% of our data.

<img src='images/q3-dw-count-graph.png' height='60%' width='70%'/>

Next, we wanted to know if that proportion changed by genre, so we broke that database down to find the total and average counts by genre for directors and writers.

If so, does that have an effect on the finances of our films?

<img src='images/q3-dw-fin-graph.png' height='60%'/>

### Conclusion

Overall, it doesn't seem that its very popular for films in general to have more than one or two directors. However, our data does show that staffing 3-4 writers has a tendency to produce a higher grossing film. 

With one fun exception, there is a documentary titled ***A Day in the Life*** that had a whopping 37 directors; which consisted of filming seemingly random people on the same random day. 

### Recommendation

<img src='images/q3-dw-fin-bar.png' height='60%'/>

While there seems to be a correlation between budget, gross, and staff count; we believe that staffing will be based upon genre and an individual films needs. Once a genre is chosen, further analysis will need to be done to provide insight as to what the optimal ratio could be.

</details>
<!------------------------------------------>


# Wrap Up

We recommend that Microsoft Studios focus on the **Action** genre due to its high popularity and ROI of 116%. With access to larger budgets, we believe that the studio will benefit from debuting with a literal bang.

<img src='images/final-violin.png'/>


The Action genre has a mean production budget of around 46.5 million dollars, with a mean gross of over 54 million dollars. A well developed film of this caliber will allow the studio to cover the costs of a second movie, perhaps in the Adventure or Animation genre, also due to their well-rounded attributes according to the data. 

We recommend that the debut Action film be limited to 1 director, with 2-3 writers.

<img src='images/final-dw.png'/>

# Future Work
- Create a larger dataset in order to gain more acurate insight
- Investigate if popularity is skewed by voter tendencies
- Look into release date and run-time on popularity and profitability 
- Whether or not high profile individuals have an effect on profit
- Compare studio competition to optimize niche markets

