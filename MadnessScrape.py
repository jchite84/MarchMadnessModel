# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:28:04 2019

@author: hitej
"""

import requests
from bs4 import BeautifulSoup
import csv

'''
teams = "abilene-christian", "air-force", "akron"
gamelog = requests.get("https://www.sports-reference.com/cbb/schools/{}/2019-gamelogs.html".format(teams))

'''

teams = "abilene-christian", "air-force", "akron", "alabama-am", "alabama-birmingham", "alabama-state", "alabama", \
"albany-ny", "alcorn-state", "american", "appalachian-state", "arizona-state", "arizona", "arkansas-little-rock", \
"arkansas-pine-bluff", "arkansas-state", "arkansas", "army", "auburn", "austin-peay", "ball-state", "baylor", "belmont", \
"bethune-cookman", "binghamton", "boise-state", "boston-college", "boston-university", "bowling-green-state", "bradley", \
"bringham-young", "brown", "bryant", "bucknell", "buffalo", "butler", "california", "california-davis", "california-irvine", \
"ucla", "cal-poly", "california-riverside", "california-santa-barbara", "cal-state-bakersfield", "fresno-state", "cal-state-fullerton", \
"long-beach-state", "cal-state-northridge", "sacramento-state", "campbell", "canisius", "central-arkansas", "central-connecticut-state", \
"central-florida", "central-michigan", "charleston-southern", "college-of-charleston", "chicago-state", "cincinnati", "citadel", "clemson", \
"cleveland-state", "coastal-carolina", "colgate", "colorado", "colorado-state", "columbia", "connecticut", "coppin-state", "cornell", \
"creighton", "dartmouth", "davidson", "dayton", "delaware-state", "delaware", "denver", "depaul", "detroit-mercy", "drake", "drexel", \
"duke", "duquesne", "east-carolina", "east-tennessee-state", "eastern-illinois", "eastern-kentucky", "eastern-michigan", "eastern-washington", \
"elon", "evansville", "fairfield", "fairleigh-dickinson", "florida-am", "florida-atlantic", "florida-gulf-coast", "florida-international", \
"florida-state", "florida", "fordham", "furman", "gardner-webb", "george-mason", "george-washington", "georgetown", "georgia-tech", \
"georgia-southern", "georgia-state", "georgia", "gonzaga", "grambling", "grand-canyon", "hampton", "hartford", "harvard", "hawaii", \
"high-point", "hofstra", "holy-cross", "houston-baptist", "houston", "howard", "idaho-state", "idaho", "illinois-chicago", "illinois-state", \
"illinois", "incarnate-word", "indiana-state", "indiana", "iupui", "iona", "iowa-state", "iowa", "jackson-state", "jacksonville-state", \
"jacksonville", "james-madison", "kansas-state", "kansas", "kennesaw-state", "kent-state", "kentucky", "la-salle", "lafayette", "lamar", \
"lehigh", "liberty", "lipscomb", "long-island-university", "longwood", "louisiana-lafayette", "louisiana-monroe", "louisiana-state", \
"louisiana-tech", "louisville", "loyola-marymount", "loyola-il", "loyola-md", "maine", "manhattan", "marist", "marquette", "marshall", \
"maryland-baltimore-county", "maryland", "maryland-eastern-shore", "massachusetts-amherst", "massachusetts-lowell", "mcneese-state", "memphis", \
"mercer", "miami-oh", "miami-fl", "michigan-state", "michigan", "middle-tennessee", "minnesota", "mississippi-state", "mississippi-valley-state", \
"mississippi", "missouri-kansas-city", "missouri-state", "missouri", "monmouth", "montana-state", "montana", "morehead-state", "morgan-state", \
"mount-st-marys", "murray-state", "navy", "nebraska-lincoln", "nebraska-omaha", "nevada-las-vegas", "nevada", "new-hampshire", "njit", \
"new-mexico-state", "new-mexico", "new-orleans", "niagara", "nicholls-state", "norfolk-state", "north-carolina-at", "north-carolina-asheville", \
"north-carolina-central", "north-carolina", "charlotte", "north-carolina-greensboro", "north-carolina-state", "north-carolina-willmington", \
"north-dakota-state", "north-dakota", "north-florida", "north-texas", "northeastern", "northern-arizona", "northern-colorado", "northern-illinois", \
"northern-iowa", "northern-kentucky", "northwestern-state", "northwestern", "notre-dame", "oakland", "ohio-state", "ohio", "oklahoma-state", \
"oklahoma", "old-dominion", "oral-roberts", "oregon-state", "oregon", "pacific", "penn-state", "pennsylvainia", "pepperdine", "pittsburgh", \
"portland-state", "portland", "prairie-view", "presbyterian", "princeton", "providence", "purdue", "ipfw", "quinnipiac", "radford", \
"rhode-island", "rice", "richmond", "rider", "robert-morris", "rutgers", "sacred-heart", "st-bonaventure", "st-francis-ny", \
"saint-francis-pa", "st-johns-ny", "saint-josephs", "saint-louis", "saint-marys-ca", "saint-peters", "sam-houston-state", "samford", \
"san-diego-state", "san-diego", "san-francisco", "san-jose-state", "santa-clara", "savannah-state", "seattle", "seton-hall", \
"siena", "south-alabama", "south-carolina-state", "south-carolina-upstate", "south-carolina", "south-dakota-state", "south-dakota", \
"south-florida", "southeast-missouri-state", "southeastern-louisiana", "southern-california", "southern-illinois", \
"southern-illinois-edwardsville", "southern-methodist", "southern-mississippi", "southern", "southern-utah", "stanford", \
"stephen-f-austin", "stetson", "stony-brook", "syracuse", "temple", "tennessee", "tennessee-martin", "tennessee-state", \
"tennessee-tech", "tennessee", "texas-am", "texas-am-corpus-christi", "texas-arlington", "texas", "texas-christian", \
"texas-el-paso", "texas-pan-american", "texas-san-antonio", "texas-southern", "texas-state", "texas-tech", "toledo", \
"towson", "troy", "tulane", "tulsa", "utah-state", "utah-valley", "utah", "valparaiso", "vanderbilt", "vermont", "villanova", \
"virginia-commonwealth", "virginia-military-institute", "virginia-tech", "virginia", "wagner", "wake-forest", "washington-state", \
"washington", "weber-state", "west-virginia", "western-carolina", "western-illinois", "western-kentucky", "western-michigan", \
"wichita-state", "william-mary", "winthrop", "green-bay", "wisconsin", "milwaukee", "wofford", "wright-state", "wyoming", \
"xavier", "yale", "youngstown-state"

teamStats = []

for i in range(len(teams)):
    teamYear = requests.get("https://www.sports-reference.com/cbb/schools/{}/2019-gamelogs.html".format(teams[i]))
    teamParse = BeautifulSoup(teamYear.text)
    teamRecord = {}
    for y in range(len(teamParse.find_all("td", {'data-stat': 'opp_id'}))):
        teamRecord["HomeTeam"] = teams[i]
        teamRecord["Opponent"] = teamParse.find_all("td", {'data-stat':'opp_id'})[y].text
        teamRecord["HT_Score"] = teamParse.find_all("td", {'data-stat':'pts'})[y].text
        teamRecord["Opp_Pts"] = teamParse.find_all("td", {'data-stat':'opp_pts'})[y].text
        teamRecord["FG"] = teamParse.find_all("td", {'data-stat':'fg'})[y].text
        teamRecord["FGA"] = teamParse.find_all("td", {'data-stat':'fga'})[y].text
        teamRecord["FG_Pct"] = teamParse.find_all("td", {'data-stat':'fg_pct'})[y].text
        teamRecord["ThreePt"] = teamParse.find_all("td", {'data-stat':'fg3'})[y].text
        teamRecord["ThreePt_Attempts"] = teamParse.find_all("td", {'data-stat':'fg3a'})[y].text
        teamRecord["ThreePt_Pct"] = teamParse.find_all("td", {'data-stat':'fg3_pct'})[y].text
        teamRecord["Free_Throws"] = teamParse.find_all("td", {'data-stat':'ft'})[y].text
        teamRecord["Free_Throw_Attempts"] = teamParse.find_all("td", {'data-stat':'fta'})[y].text
        teamRecord["Free_Throw_Pct"] = teamParse.find_all("td", {'data-stat':'ft_pct'})[y].text
        teamRecord["Offensive_Rebounds"] = teamParse.find_all("td", {'data-stat':'orb'})[y].text
        teamRecord["Total_Rebounds"] = teamParse.find_all("td", {'data-stat':'trb'})[y].text
        teamRecord["Assists"] = teamParse.find_all("td", {'data-stat':'ast'})[y].text
        teamRecord["Steals"] = teamParse.find_all("td", {'data-stat':'stl'})[y].text
        teamRecord["Blocks"] = teamParse.find_all("td", {'data-stat':'blk'})[y].text
        teamRecord["Turnovers"] = teamParse.find_all("td", {'data-stat':'tov'})[y].text
        teamRecord["Personal_Fouls"] = teamParse.find_all("td", {'data-stat':'pf'})[y].text
        teamStats.append(teamRecord)
        teamRecord = {}

header = "Home_Team", "Opponent", "HT_Pts", "Opp_Pts", "FG", "FGA", "FG_Pct", "Three_Pt", "Three_Pt_Attempts", "Three_Pt_Pct", "Free_Throws",\
"Free_Throw_Attempts", "Free_Throw_Pct", "Offensive_Rebounds", "Total_Rebounds", "Assists", "Steals", "Blocks", "Turnovers", "Personal_Fouls"

output = 'C:/Users/hitej/Documents/March Madness/MarchMadnessFullData.csv'

with open (output, "w") as file:
    filewriter = csv.writer(file, lineterminator = "\n")
    filewriter.writerow(header)
del(header)

with open (output, "a") as file:
    for i in range(len(teamStats)):
        row = teamStats[i]["HomeTeam"],teamStats[i]["Opponent"],teamStats[i]["HT_Score"],\
        teamStats[i]["Opp_Pts"],teamStats[i]["FG"],teamStats[i]["FGA"],teamStats[i]["FG_Pct"],\
        teamStats[i]["ThreePt"],teamStats[i]["ThreePt_Attempts"],teamStats[i]["ThreePt_Pct"],\
        teamStats[i]["Free_Throws"],teamStats[i]["Free_Throw_Attempts"],teamStats[i]["Free_Throw_Pct"],\
        teamStats[i]["Offensive_Rebounds"],teamStats[i]["Total_Rebounds"],teamStats[i]["Assists"],\
        teamStats[i]["Steals"],teamStats[i]["Blocks"],teamStats[i]["Turnovers"],teamStats[i]["Personal_Fouls"]
        filewriter = csv.writer(file, lineterminator = "\n")
        filewriter.writerow(row)


        
'''
Test Code

dukeLog = requests.get("https://www.sports-reference.com/cbb/schools/duke/2019-gamelogs.html")
dukeParse = BeautifulSoup(dukeLog.text)
len(dukeParse.find_all("td", {'data-stat':'opp_id'}))

for i in range(len(dukeParse.find_all("td", {'data-stat':'opp_id'}))):
    print("Duke", dukeParse.find_all("td", {'data-stat':'opp_id'})[i].text, dukeParse.find_all("td", {'data-stat':'pts'})[i].text, dukeParse.find_all("td", {'data-stat':'opp_pts'})[i].text)
'''