# Farmers Markets in the United States:
## Prediciting Markets by County

<img src='Images\benefits-of-farmers-markets.png' width = '65%' />

[Medium Blog Post](https://medium.com/@kekay0528/mod-3-blog-post-f14ff9f7c795)

[Presentation PDF](https://github.com/kailakay/dsc-mod-3-project-v2-1-onl01-dtsc-ft-041320/blob/master/Farmers%20Market%20Accessibility%20Presentation.pdf)

[Video Walkthrough]()

## Purpose
As a professional chef coming into Data Science; my main goal for my career is to fuse my two passions in order to aid in tackling food accessbility and sustanibilty. My first step towards that journey is with this Module 3 project. I've downloaded data that includes information on farmers markets in the United States as well as financial and population information for counties in the U.S. 

My goal with the project is to craft and hone into my own personal work flow; while also starting to get into the mind set that will allow me to succeed in moving on towards tackling deeper issues in this broad category of food sustainability. 

The original data set can be found on [Kaggle here](https://www.kaggle.com/madeleineferguson/farmers-markets-in-the-united-states).
<!------------------------------------------>
### Data Description

<details><summary style="font-size: 18px"> 
List of Files:</summary> 

```
| farmers_markets_from_usda.csv
| county_info.csv
```
</details>
<!------------------------------------------>

### Main Questions:

[Question 1 Notebook Link](https://github.com/kailakay/dsc-mod-3-project-v2-1-onl01-dtsc-ft-041320/blob/master/Q1.ipynb)
<details><summary style="font-size: 24px">
Question 1: {Does product variety correlate to alternative payment option?} </summary> 

#### Tables Used:

```
| farmers_markets_from_usda.csv
```
#### EDA

When cleaning this dataframe; in the interest of time I chose to drop zipcodes, social media, and seasonal information. 

While the distribution of product availbility appears relatively normal, I was curious as to whether or not that was an indicator that a market accepted assisted forms of payment outside of cash or credit. 

<img src='Images\Q1 Distribution of Product Count.png' witdth='50%'/>

After cleaning and visualizing, I found that typically a market with a higher product variety does tend to accept more forms of alternative payement. 

<img src='Images\Q1 Alternative Payment Methods by Produce Availability.png'/>

Most interestingly though; I found that the presence of a website was actually a better indicator of a market accepting alternative payment! 

<img src='Images\Q1 Alternative Payment Methods.png' />

#### Conclusion

After cleaning and exploring the data, I found that typically a market that offers a higher variety of products does have a higher tendency to accept alternative payment forms. 

</details>

<!------------------------------------------>
[Question 2 Notebook Link](https://github.com/kailakay/dsc-mod-3-project-v2-1-onl01-dtsc-ft-041320/blob/master/Q2.ipynb)

<details><summary style="font-size: 24px">
Question 2:  {What is the market availability by State?} </summary> 

### Tables Used:

```
| farmers_markets_from_usda.csv
| county_info.csv
```

### EDA

To start, I broke down all of the states by count of farmers market in descending order. 

<img src='Images\Q2 Farmers Markets County by State- Top 25.png' />

I then followed by doing the same method, except by mean product availbility by state:

<img src='Images\Mean Product Count by State map.jpg' />

### Conclusion

While New York and California have the highest number of Farmers Markets; Oregon, Washington, Florida, Vermont, and Arizona have the highest mean product count for their markets. 

</details>
<!------------------------------------------>

[Question 3 Notebook Link](https://github.com/kailakay/dsc-mod-3-project-v2-1-onl01-dtsc-ft-041320/blob/master/Q3.ipynb)

<details><summary style="font-size: 24px">
Question 3: {How do urban areas compare to rural areas in terms of accessbility (both to the product itself and to alternative payment methods)?} </summary> 

### Tables Used:

```
| farmers_markets_from_usda.csv
| county_info.csv
```

### EDA

It seems at first glance that higher populated states and urban areas have more access:

<img src='Images\Q3 Percentage of Markets accepting Alternative Payments by State.jpg'/>

However, I did not have enough time to fully develop the answers to this question and look forward to coming back in the future to finish up some of the more in-depth analysis.

### Conclusion

More future work needs to be done in order to appropriately determine the answer to this question. 

</details>
<!------------------------------------------>


# Wrap Up

<img src='Images\nfmw-infographic_stateofUSfarmers.jpg' width=80%/>

# Future Work
- Utilize Gradient Boosting
- Break information down into smaller areas and display in heat maps
- Look into grocery store versus convenience store availability
- Align political parties and counties to availability
- Investigate seasonal distribution and effect
- Start investigating the farmers side of the issue

