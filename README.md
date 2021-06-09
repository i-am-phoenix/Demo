## PROJECT1<br>Impact of COVID on real estate market in Houston and beyond

#### Objective

These days Houston’s housing market is going through some major changes. It is not unheard of to see >10-20 offers bidding on the same property, leading to at times over-inflation of sale price beyond that of the listing. 

We also keep hearing about all those “New Yorkers and Silicone Valley folks” moving down to “cheaper” states, now that remote work in tech sector is much more common.

So....

Our objective was to understand what impact, if any, did COVID have on the real estate market in the US, in particular in Houston TX (vs other cities) and Harris county (vs other counties in TX)

#### Methodology & Data Sourcing

Our methodology was to seek data from 3 main sources of information:

1. Real Estate Data from [Zillow](https://www.zillow.com/research/data/) 
2. COVID data via [Johns Hopkins](https://coronavirus.jhu.edu/about/how-to-use-our-data)
3. Demographic data from [US Census](https://txcip.org/tac/census/) 

Separate Jupyter Notebooks were used to clean and pre-process real estate and demographic data:

* [zillow_data_cleaning_functions.ipynb](zillow_data_cleaning_functions.ipynb) (real estate)
* [Brainstorm_Rural Counties.ipynb](Brainstorm_Rural Counties.ipynb) (demographics)
* COVID data was pre-processed in Excel and summary *.csv file is located [here](data/jhcovid/COVID19_policies_cases_and_deaths_5_counties_TX.csv)

The above two Jupyter Notebooks are sourcing live data and need to be run first. Then a final [prj2_summary.ipynb](prj2_summary.ipynb) notebok needs to be run to perform merged data analysis and reporting.

We have chosen 5 cities within continental US and 5 counties within Texas to perform our comparisons on.

Chosen *cities* were: 

* Houston, TX
* San Francisco, CA
* Seattle, WA
* Chicago, IL
* New York, NY

Chosen counties within Texas were (selections were made with Harris county in mind, adding surrounding counties as well as Trinity as a more rural, less populated one):

* Harris County
* Fort Bend County
* Montgomery County
* Galveston County
* Trinity County

#### Observations

Our key observations as well as a more in-depth overview of methodology are presented in the set of [SLIDES](Project1_Group2_ReportOut.pdf) included with this repository. 



#### Authors





