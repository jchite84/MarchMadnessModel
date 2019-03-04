# MarchMadnessModel
Scraper and Predictive Model Built for March Madness Bracket

## Data

Data has been scraped from Sports-Reference.com using the python script MadnessScrape.py. The following fields were scraped for each game of each Division I team through February 26th, 2019.
- Home Team
- Opponent
- HT_Score
- Opp_Pts
- FG
- FG_Attempts
- FG_Pct
- ThreePt
- ThreePt_Attempts
- ThreePt_Pct
- Free_Throws
- Free_Throw_Attempts
- Free_Throw_Pct
- Offensive_Rebounds
- Total_Rebounds
- Assists
- Steals
- Blocks
- Turnovers
- Fouls

Opponent data was scraped with THAT team listed as "Home Team". This avoided duplicated data, and made it easier to generate game scenarios that did not actually happen in the year. 

### Data Cleaning
Data was pulled into R for cleaning. Games were matched on Home_Team and Opponent Team name and Home_Team_Pts with Opp_Pts. Matching games were then indexed with the same Game_Index number. This process was imperfect, but it removed games against Division II teams. Games that could not be indexed were removed. This reduced the total number of games in the training data to 3,388 unique games (of ~4500 total games for the season).

This long data format was exported into Excel where "Wide" data was created. Indexed games were matched and new columns generated with home team stats and opponent stats in one row. Two data sets were created. Each contain all games but with the reciporical teams listed as "Home Team" and "Opponent". This wide data was then reimported into R. 

## Methods
A Support Vector Machine (SVM) model was used  with a linear kernel in R using the Rattle package. Data was partitioned into training, validation, and training sets (70/15/15). HT_Score and Opp_Pts were ignored in the model. Game Index, Home Team, and Opponent were used as identifiers. Trained model tested at 95% accuracy. This was deemed an acceptable level for this project. 

Two prediction functions were created with the resulting model. The first takes 2 teams as input. It randomly samples 20 games from each team and binds the data to create a 20 random scenario games with data from the 2018-2019 season. This data is run through the SVM and the number of games that Team 1 wins is returned. The second function runs the first function 200 times and returns the overall percentage of games that Team 1 is expected to win as well as the odds probability of winning. 

## Follow Up Questions and Concerns
The main limitation of the model appears to be that it does not weight for conference quality. Placing teams that are far apart in quality (Gonzaga vs Chicago State for instance) creates a clearly demarcated winner, but not at the percentages expected. Teams that are more evenly matched, or teams that are more closely ranked within their respective conferences produces fuzzier results. Even in instances where the outcome would be more clear in the event that those teams actually played one another. 

Switching the order of the teams does not always provide reciporical results, which is expected. This is especially noticable when teams are ranked similiarly in their conferences, but the overall conference quality is markedly different. 

## Using the data
MadnessScrape.py can be used to recreate the raw data from Sports-Reference.com. Those using the Anacondas python release with Spyder IDE can also use MarchMadnessData.spydata to get the snapshot from February, 26th and write the data. DataModel (Teams Tab) was primarily used to clean the data and standardize the team name to the URL standard. This was instrumental in matching games. DataModel also contains geographical information for each team, should users want to include travel considerations into future models. 

Those choosing to work with the raw data can use the R Script (MadnessAnalysis.R) to index and match games, but this method had limited success. I am open to improved code for this portion of the cleaning. The conversion from Long to Wide data formats was done in Excel, and therefore was not scripted. However, it was acheived primarily using VLookup. Results were also categorized in Excel. DivI_Wide_1 and DivI_Wide_2 were generated through this process and reimported into R.

Those choosing to work with the data as I have created it can import the MadnessAnalysisData Workspace. The primary function is modelTeams(). It takes 2 string parameters as input. These are the URL standard team names. These can be found in the Data Model excel sheet. Example: modelGames("michigan", "michigan-state"). The output is the probability of winning out of 4000 scenarios and the odds probability of winning out of 4000 games. 
