#Peer-graded Assignment submission: Predicting the Winning College Basketball Team
#Level 2 headings may be created by course providers in the future.
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a href=\"https://www.bigdatauniversity.com\"><img src=\"https://ibm.box.com/shared/static/cw2c7r3o20w9zn8gkecaeyjhgw3xdgbj.png\" width=\"400\" align=\"center\"></a>\n",
    "\n",
    "<h1 align=\"center\"><font size=\"5\">Classification with Python</font></h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "In this notebook we try to practice all the classification algorithms that we learned in this course.\n",
    "\n",
    "We load a dataset using Pandas library, and apply the following algorithms, and find the best one for this specific dataset by accuracy evaluation methods.\n",
    "\n",
    "Lets first load required libraries:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "import itertools\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from matplotlib.ticker import NullFormatter\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.ticker as ticker\n",
    "from sklearn import preprocessing\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### About dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "This dataset is about the performance of basketball teams. The __cbb.csv__ data set includes performance data about five seasons of 354 basketball teams. It includes following fields:\n",
    "\n",
    "| Field          | Description                                                                           |\n",
    "|----------------|---------------------------------------------------------------------------------------|\n",
    "|TEAM |\tThe Division I college basketball school|\n",
    "|CONF|\tThe Athletic Conference in which the school participates in (A10 = Atlantic 10, ACC = Atlantic Coast Conference, AE = America East, Amer = American, ASun = ASUN, B10 = Big Ten, B12 = Big 12, BE = Big East, BSky = Big Sky, BSth = Big South, BW = Big West, CAA = Colonial Athletic Association, CUSA = Conference USA, Horz = Horizon League, Ivy = Ivy League, MAAC = Metro Atlantic Athletic Conference, MAC = Mid-American Conference, MEAC = Mid-Eastern Athletic Conference, MVC = Missouri Valley Conference, MWC = Mountain West, NEC = Northeast Conference, OVC = Ohio Valley Conference, P12 = Pac-12, Pat = Patriot League, SB = Sun Belt, SC = Southern Conference, SEC = South Eastern Conference, Slnd = Southland Conference, Sum = Summit League, SWAC = Southwestern Athletic Conference, WAC = Western Athletic Conference, WCC = West Coast Conference)|\n",
    "|G|\tNumber of games played|\n",
    "|W|\tNumber of games won|\n",
    "|ADJOE|\tAdjusted Offensive Efficiency (An estimate of the offensive efficiency (points scored per 100 possessions) a team would have against the average Division I defense)|\n",
    "|ADJDE|\tAdjusted Defensive Efficiency (An estimate of the defensive efficiency (points allowed per 100 possessions) a team would have against the average Division I offense)|\n",
    "|BARTHAG|\tPower Rating (Chance of beating an average Division I team)|\n",
    "|EFG_O|\tEffective Field Goal Percentage Shot|\n",
    "|EFG_D|\tEffective Field Goal Percentage Allowed|\n",
    "|TOR|\tTurnover Percentage Allowed (Turnover Rate)|\n",
    "|TORD|\tTurnover Percentage Committed (Steal Rate)|\n",
    "|ORB|\tOffensive Rebound Percentage|\n",
    "|DRB|\tDefensive Rebound Percentage|\n",
    "|FTR|\tFree Throw Rate (How often the given team shoots Free Throws)|\n",
    "|FTRD|\tFree Throw Rate Allowed|\n",
    "|2P_O|\tTwo-Point Shooting Percentage|\n",
    "|2P_D|\tTwo-Point Shooting Percentage Allowed|\n",
    "|3P_O|\tThree-Point Shooting Percentage|\n",
    "|3P_D|\tThree-Point Shooting Percentage Allowed|\n",
    "|ADJ_T|\tAdjusted Tempo (An estimate of the tempo (possessions per 40 minutes) a team would have against the team that wants to play at an average Division I tempo)|\n",
    "|WAB|\tWins Above Bubble (The bubble refers to the cut off between making the NCAA March Madness Tournament and not making it)|\n",
    "|POSTSEASON|\tRound where the given team was eliminated or where their season ended (R68 = First Four, R64 = Round of 64, R32 = Round of 32, S16 = Sweet Sixteen, E8 = Elite Eight, F4 = Final Four, 2ND = Runner-up, Champion = Winner of the NCAA March Madness Tournament for that given year)|\n",
    "|SEED|\tSeed in the NCAA March Madness Tournament|\n",
    "|YEAR|\tSeason"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Load Data From CSV File  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Let's load the dataset [NB Need to provide link to csv file]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TEAM</th>\n",
       "      <th>CONF</th>\n",
       "      <th>G</th>\n",
       "      <th>W</th>\n",
       "      <th>ADJOE</th>\n",
       "      <th>ADJDE</th>\n",
       "      <th>BARTHAG</th>\n",
       "      <th>EFG_O</th>\n",
       "      <th>EFG_D</th>\n",
       "      <th>TOR</th>\n",
       "      <th>...</th>\n",
       "      <th>FTRD</th>\n",
       "      <th>2P_O</th>\n",
       "      <th>2P_D</th>\n",
       "      <th>3P_O</th>\n",
       "      <th>3P_D</th>\n",
       "      <th>ADJ_T</th>\n",
       "      <th>WAB</th>\n",
       "      <th>POSTSEASON</th>\n",
       "      <th>SEED</th>\n",
       "      <th>YEAR</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>North Carolina</td>\n",
       "      <td>ACC</td>\n",
       "      <td>40</td>\n",
       "      <td>33</td>\n",
       "      <td>123.3</td>\n",
       "      <td>94.9</td>\n",
       "      <td>0.9531</td>\n",
       "      <td>52.6</td>\n",
       "      <td>48.1</td>\n",
       "      <td>15.4</td>\n",
       "      <td>...</td>\n",
       "      <td>30.4</td>\n",
       "      <td>53.9</td>\n",
       "      <td>44.6</td>\n",
       "      <td>32.7</td>\n",
       "      <td>36.2</td>\n",
       "      <td>71.7</td>\n",
       "      <td>8.6</td>\n",
       "      <td>2ND</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Villanova</td>\n",
       "      <td>BE</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>123.1</td>\n",
       "      <td>90.9</td>\n",
       "      <td>0.9703</td>\n",
       "      <td>56.1</td>\n",
       "      <td>46.7</td>\n",
       "      <td>16.3</td>\n",
       "      <td>...</td>\n",
       "      <td>30.0</td>\n",
       "      <td>57.4</td>\n",
       "      <td>44.1</td>\n",
       "      <td>36.2</td>\n",
       "      <td>33.9</td>\n",
       "      <td>66.7</td>\n",
       "      <td>8.9</td>\n",
       "      <td>Champions</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notre Dame</td>\n",
       "      <td>ACC</td>\n",
       "      <td>36</td>\n",
       "      <td>24</td>\n",
       "      <td>118.3</td>\n",
       "      <td>103.3</td>\n",
       "      <td>0.8269</td>\n",
       "      <td>54.0</td>\n",
       "      <td>49.5</td>\n",
       "      <td>15.3</td>\n",
       "      <td>...</td>\n",
       "      <td>26.0</td>\n",
       "      <td>52.9</td>\n",
       "      <td>46.5</td>\n",
       "      <td>37.4</td>\n",
       "      <td>36.9</td>\n",
       "      <td>65.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>E8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Virginia</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>29</td>\n",
       "      <td>119.9</td>\n",
       "      <td>91.0</td>\n",
       "      <td>0.9600</td>\n",
       "      <td>54.8</td>\n",
       "      <td>48.4</td>\n",
       "      <td>15.1</td>\n",
       "      <td>...</td>\n",
       "      <td>33.4</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.3</td>\n",
       "      <td>40.3</td>\n",
       "      <td>34.7</td>\n",
       "      <td>61.9</td>\n",
       "      <td>8.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kansas</td>\n",
       "      <td>B12</td>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>120.9</td>\n",
       "      <td>90.4</td>\n",
       "      <td>0.9662</td>\n",
       "      <td>55.7</td>\n",
       "      <td>45.1</td>\n",
       "      <td>17.8</td>\n",
       "      <td>...</td>\n",
       "      <td>37.3</td>\n",
       "      <td>52.7</td>\n",
       "      <td>43.4</td>\n",
       "      <td>41.3</td>\n",
       "      <td>32.5</td>\n",
       "      <td>70.1</td>\n",
       "      <td>11.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             TEAM CONF   G   W  ADJOE  ADJDE  BARTHAG  EFG_O  EFG_D   TOR  \\\n",
       "0  North Carolina  ACC  40  33  123.3   94.9   0.9531   52.6   48.1  15.4   \n",
       "1       Villanova   BE  40  35  123.1   90.9   0.9703   56.1   46.7  16.3   \n",
       "2      Notre Dame  ACC  36  24  118.3  103.3   0.8269   54.0   49.5  15.3   \n",
       "3        Virginia  ACC  37  29  119.9   91.0   0.9600   54.8   48.4  15.1   \n",
       "4          Kansas  B12  37  32  120.9   90.4   0.9662   55.7   45.1  17.8   \n",
       "\n",
       "   ...  FTRD  2P_O  2P_D  3P_O  3P_D  ADJ_T   WAB  POSTSEASON  SEED  YEAR  \n",
       "0  ...  30.4  53.9  44.6  32.7  36.2   71.7   8.6         2ND   1.0  2016  \n",
       "1  ...  30.0  57.4  44.1  36.2  33.9   66.7   8.9   Champions   2.0  2016  \n",
       "2  ...  26.0  52.9  46.5  37.4  36.9   65.5   2.3          E8   6.0  2016  \n",
       "3  ...  33.4  52.6  46.3  40.3  34.7   61.9   8.6          E8   1.0  2016  \n",
       "4  ...  37.3  52.7  43.4  41.3  32.5   70.1  11.6          E8   1.0  2016  \n",
       "\n",
       "[5 rows x 24 columns]"
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0120ENv3/Dataset/ML0101EN_EDX_skill_up/cbb.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1406, 24)"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Add Column\n",
    "Next we'll add a column that will contain \"true\" if the wins above bubble are over 7 and \"false\" if not. We'll call this column Win Index or \"windex\" for short. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['windex'] = np.where(df.WAB > 7, 'True', 'False')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "# Data visualization and pre-processing\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Next we'll filter the data set to the teams that made the Sweet Sixteen, the Elite Eight, and the Final Four in the post season. We'll also create a new dataframe that will hold the values with the new column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TEAM</th>\n",
       "      <th>CONF</th>\n",
       "      <th>G</th>\n",
       "      <th>W</th>\n",
       "      <th>ADJOE</th>\n",
       "      <th>ADJDE</th>\n",
       "      <th>BARTHAG</th>\n",
       "      <th>EFG_O</th>\n",
       "      <th>EFG_D</th>\n",
       "      <th>TOR</th>\n",
       "      <th>...</th>\n",
       "      <th>2P_O</th>\n",
       "      <th>2P_D</th>\n",
       "      <th>3P_O</th>\n",
       "      <th>3P_D</th>\n",
       "      <th>ADJ_T</th>\n",
       "      <th>WAB</th>\n",
       "      <th>POSTSEASON</th>\n",
       "      <th>SEED</th>\n",
       "      <th>YEAR</th>\n",
       "      <th>windex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notre Dame</td>\n",
       "      <td>ACC</td>\n",
       "      <td>36</td>\n",
       "      <td>24</td>\n",
       "      <td>118.3</td>\n",
       "      <td>103.3</td>\n",
       "      <td>0.8269</td>\n",
       "      <td>54.0</td>\n",
       "      <td>49.5</td>\n",
       "      <td>15.3</td>\n",
       "      <td>...</td>\n",
       "      <td>52.9</td>\n",
       "      <td>46.5</td>\n",
       "      <td>37.4</td>\n",
       "      <td>36.9</td>\n",
       "      <td>65.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>E8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Virginia</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>29</td>\n",
       "      <td>119.9</td>\n",
       "      <td>91.0</td>\n",
       "      <td>0.9600</td>\n",
       "      <td>54.8</td>\n",
       "      <td>48.4</td>\n",
       "      <td>15.1</td>\n",
       "      <td>...</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.3</td>\n",
       "      <td>40.3</td>\n",
       "      <td>34.7</td>\n",
       "      <td>61.9</td>\n",
       "      <td>8.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kansas</td>\n",
       "      <td>B12</td>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>120.9</td>\n",
       "      <td>90.4</td>\n",
       "      <td>0.9662</td>\n",
       "      <td>55.7</td>\n",
       "      <td>45.1</td>\n",
       "      <td>17.8</td>\n",
       "      <td>...</td>\n",
       "      <td>52.7</td>\n",
       "      <td>43.4</td>\n",
       "      <td>41.3</td>\n",
       "      <td>32.5</td>\n",
       "      <td>70.1</td>\n",
       "      <td>11.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Oregon</td>\n",
       "      <td>P12</td>\n",
       "      <td>37</td>\n",
       "      <td>30</td>\n",
       "      <td>118.4</td>\n",
       "      <td>96.2</td>\n",
       "      <td>0.9163</td>\n",
       "      <td>52.3</td>\n",
       "      <td>48.9</td>\n",
       "      <td>16.1</td>\n",
       "      <td>...</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.1</td>\n",
       "      <td>34.4</td>\n",
       "      <td>36.2</td>\n",
       "      <td>69.0</td>\n",
       "      <td>6.7</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Syracuse</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>23</td>\n",
       "      <td>111.9</td>\n",
       "      <td>93.6</td>\n",
       "      <td>0.8857</td>\n",
       "      <td>50.0</td>\n",
       "      <td>47.3</td>\n",
       "      <td>18.1</td>\n",
       "      <td>...</td>\n",
       "      <td>47.2</td>\n",
       "      <td>48.1</td>\n",
       "      <td>36.0</td>\n",
       "      <td>30.7</td>\n",
       "      <td>65.5</td>\n",
       "      <td>-0.3</td>\n",
       "      <td>F4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         TEAM CONF   G   W  ADJOE  ADJDE  BARTHAG  EFG_O  EFG_D   TOR  ...  \\\n",
       "2  Notre Dame  ACC  36  24  118.3  103.3   0.8269   54.0   49.5  15.3  ...   \n",
       "3    Virginia  ACC  37  29  119.9   91.0   0.9600   54.8   48.4  15.1  ...   \n",
       "4      Kansas  B12  37  32  120.9   90.4   0.9662   55.7   45.1  17.8  ...   \n",
       "5      Oregon  P12  37  30  118.4   96.2   0.9163   52.3   48.9  16.1  ...   \n",
       "6    Syracuse  ACC  37  23  111.9   93.6   0.8857   50.0   47.3  18.1  ...   \n",
       "\n",
       "   2P_O  2P_D  3P_O  3P_D  ADJ_T   WAB  POSTSEASON  SEED  YEAR  windex  \n",
       "2  52.9  46.5  37.4  36.9   65.5   2.3          E8   6.0  2016   False  \n",
       "3  52.6  46.3  40.3  34.7   61.9   8.6          E8   1.0  2016    True  \n",
       "4  52.7  43.4  41.3  32.5   70.1  11.6          E8   1.0  2016    True  \n",
       "5  52.6  46.1  34.4  36.2   69.0   6.7          E8   1.0  2016   False  \n",
       "6  47.2  48.1  36.0  30.7   65.5  -0.3          F4  10.0  2016   False  \n",
       "\n",
       "[5 rows x 25 columns]"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = df.loc[df['POSTSEASON'].str.contains('F4|S16|E8', na=False)]\n",
    "df1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "S16    32\n",
       "E8     16\n",
       "F4      8\n",
       "Name: POSTSEASON, dtype: int64"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['POSTSEASON'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "32 teams made it into the Sweet Sixteen, 16 into the Elite Eight, and 8 made it into the Final Four over 5 seasons. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets plot some columns to underestand data better:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1296x216 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "bins = np.linspace(df1.BARTHAG.min(), df1.BARTHAG.max(), 10)\n",
    "g = sns.FacetGrid(df1, col=\"windex\", hue=\"POSTSEASON\", palette=\"Set1\", col_wrap=6)\n",
    "g.map(plt.hist, 'BARTHAG', bins=bins, ec=\"k\")\n",
    "\n",
    "g.axes[-1].legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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kggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSeg0o29fYfsH2soEoCAAAqbwzqGsldfZzHQAAvEWvARUR90v64wDUAgDADkPy2pDt6ZKmS1JbW9su27a0tah7VXdeu85NXUOdbFe6DNSIvvSZlOXZn5tHNev5lc/nsq2Uf8+0dnclt60U5RZQETFb0mxJ6ujoiF217V7VrWNunpLLfm+bOjeX7UjSti3bkqwL1akvfSZlqfbnVOvK+/dMiseYF67iAwAkiYACACSpnMvMfy7pQUkfsN1l+5T+LwsAUOt6/RtURJw4EIUAAFCMIT4AQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSCCgAQJIIKABAkggoAECSygoo2522n7T9tO1v93dRAAD0GlC26yVdKekoSQdKOtH2gf1dGACgtpVzBvVhSU9HxDMR8YakGyUd279lAQBqnSNi1w3sz0nqjIhTs/tfljQpIs7Yqd10SdOzux+Q9GT+5Q6IEZLWVbqId6gajkEaHMexLiI6d+eJVdRnpMHxWvWGYxg4ZfWbIWVsyCXWvS3VImK2pNllbC9pth+JiI5K1/FOVMMxSNVzHD2plj4jVcdrxTGkp5whvi5Jo4rut0rq7p9yAAAoKCegfifp/bbH2N5D0gmSftW/ZQEAal2vQ3wRsdX2GZLulFQv6ZqIeLzfK6ucahhyqYZjkKrnOGpBNbxWHENier1IAgCASmAmCQBAkggoAECSai6gbF9j+wXby4rWfd7247a32e7Yqf252RRPT9r+9MBX/HZ9OQbbo21vtr0kW35UmarfqodjuNT2720/Zvtm23sXPZbc61BL6Df0m4qIiJpaJB0h6VBJy4rWjVPhg5LzJHUUrT9Q0lJJQyWNkfQHSfWD7BhGF7dLZenhGI6UNCS7fbGki1N+HWppod+ksdRav6m5M6iIuF/SH3datzwiSn2K/1hJN0bE6xHxrKSnVZj6qaL6eAxJ6uEY7oqIrdndh1T4zJ2U6OtQS+g3aai1flNzAdVHLZJWFd3vytYNNmNsP2r7Ptsfr3QxZfpbSb/JblfL61ArquX1ot9UWDlTHdWysqZ5StxqSW0Rsd72REm32B4fES9VurCe2D5P0lZJN2xfVaLZYHsdakk1vF70mwRwBrVrg36ap+z0fn12e5EK49BjK1tVz2z/jaSjJZ0U2UC6quB1qDGD/vWi36SBgNq1X0k6wfZQ22MkvV/SwxWuqU9svyv7Ti/Z3l+FY3imslWVZrtT0rckfSYiXi16aNC/DjVm0L9e9JtEVPoqjYFeJP1chdP3LSq8wzhF0tTs9uuS/k/SnUXtz1Ph3dOTko6qdP19PQZJx0t6XIWreRZLOqbS9e/iGJ5WYcx8Sbb8KOXXoZYW+g39phILUx0BAJLEEB8AIEkEFAAgSQQUACBJBBQAIEkEFAAgSQRUgmxPtR22P5jd3z6z8qO2l9t+OPtg3vb2J9u+ouj+9Gx2499nbQ8vemxeNrPx9lmabxrYowPyR5+pTkx1lKYTJT0g6QRJF2Tr/hARh0g7Pjj4S9t1EfGT4ifaPlrSVyUdHhHrbB+qwjQtH46INVmzkyLikYE4EGCA0GeqEGdQibHdJOljKnwA74RSbSLiGUlnS5pR4uFvSZoZEeuytoslXSfpa/1SMFBh9JnqRUCl57OS7oiIFZL+mL2bK2WxpA+WWD9e0qKd1j2Srd/uhqLhikvfccVAZdFnqhRDfOk5UdL3sts3ZvevLNGu1EzFPbHeOosxwxWoJvSZKkVAJcT2vpI+Kekg2yGpXoVOclWJ5odIWl5i/ROSJkr6bdG6Q7P1QFWhz1Q3hvjS8jlJ10fEfhExOiJGSXpWf/qGTEmFK5QkXSbpByW2cYmki7OOK9vtkk5W6Q4LDHb0mSrGGVRaTpQ0a6d1v5D0j5LeZ/tRSY2SXpb0g6KrkYaoMBuzIuJXtlskLcjeUb4s6UsRsbpomzfY3pzdXhcRn+qfwwH6HX2mijGbeRWwfbmkpyKCd3xAGegzgwMBNcjZ/o2kPSQdFxEbK10PkDr6zOBBQAEAksRFEgCAJBFQAIAkEVAAgCQRUACAJBFQAIAk/T9mzBRRZdMnhAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x216 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bins = np.linspace(df1.ADJOE.min(), df1.ADJOE.max(), 10)\n",
    "g = sns.FacetGrid(df1, col=\"windex\", hue=\"POSTSEASON\", palette=\"Set1\", col_wrap=2)\n",
    "g.map(plt.hist, 'ADJOE', bins=bins, ec=\"k\")\n",
    "\n",
    "g.axes[-1].legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "# Pre-processing:  Feature selection/extraction"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Lets look at how Adjusted Defense Efficiency plots"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x216 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "bins = np.linspace(df1.ADJDE.min(), df1.ADJDE.max(), 10)\n",
    "g = sns.FacetGrid(df1, col=\"windex\", hue=\"POSTSEASON\", palette=\"Set1\", col_wrap=2)\n",
    "g.map(plt.hist, 'ADJDE', bins=bins, ec=\"k\")\n",
    "g.axes[-1].legend()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "We see that this data point doesn't impact the ability of a team to get into the Final Four. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## Convert Categorical features to numerical values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Lets look at the postseason:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "windex  POSTSEASON\n",
       "False   S16           0.605263\n",
       "        E8            0.263158\n",
       "        F4            0.131579\n",
       "True    S16           0.500000\n",
       "        E8            0.333333\n",
       "        F4            0.166667\n",
       "Name: POSTSEASON, dtype: float64"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1.groupby(['windex'])['POSTSEASON'].value_counts(normalize=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "13% of teams with 6 or less wins above bubble make it into the final four while 17% of teams with 7 or more do.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Lets convert wins above bubble (winindex) under 7 to 0 and over 7 to 1:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:6586: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  self._update_inplace(new_data)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TEAM</th>\n",
       "      <th>CONF</th>\n",
       "      <th>G</th>\n",
       "      <th>W</th>\n",
       "      <th>ADJOE</th>\n",
       "      <th>ADJDE</th>\n",
       "      <th>BARTHAG</th>\n",
       "      <th>EFG_O</th>\n",
       "      <th>EFG_D</th>\n",
       "      <th>TOR</th>\n",
       "      <th>...</th>\n",
       "      <th>2P_O</th>\n",
       "      <th>2P_D</th>\n",
       "      <th>3P_O</th>\n",
       "      <th>3P_D</th>\n",
       "      <th>ADJ_T</th>\n",
       "      <th>WAB</th>\n",
       "      <th>POSTSEASON</th>\n",
       "      <th>SEED</th>\n",
       "      <th>YEAR</th>\n",
       "      <th>windex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notre Dame</td>\n",
       "      <td>ACC</td>\n",
       "      <td>36</td>\n",
       "      <td>24</td>\n",
       "      <td>118.3</td>\n",
       "      <td>103.3</td>\n",
       "      <td>0.8269</td>\n",
       "      <td>54.0</td>\n",
       "      <td>49.5</td>\n",
       "      <td>15.3</td>\n",
       "      <td>...</td>\n",
       "      <td>52.9</td>\n",
       "      <td>46.5</td>\n",
       "      <td>37.4</td>\n",
       "      <td>36.9</td>\n",
       "      <td>65.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>E8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Virginia</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>29</td>\n",
       "      <td>119.9</td>\n",
       "      <td>91.0</td>\n",
       "      <td>0.9600</td>\n",
       "      <td>54.8</td>\n",
       "      <td>48.4</td>\n",
       "      <td>15.1</td>\n",
       "      <td>...</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.3</td>\n",
       "      <td>40.3</td>\n",
       "      <td>34.7</td>\n",
       "      <td>61.9</td>\n",
       "      <td>8.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kansas</td>\n",
       "      <td>B12</td>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>120.9</td>\n",
       "      <td>90.4</td>\n",
       "      <td>0.9662</td>\n",
       "      <td>55.7</td>\n",
       "      <td>45.1</td>\n",
       "      <td>17.8</td>\n",
       "      <td>...</td>\n",
       "      <td>52.7</td>\n",
       "      <td>43.4</td>\n",
       "      <td>41.3</td>\n",
       "      <td>32.5</td>\n",
       "      <td>70.1</td>\n",
       "      <td>11.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Oregon</td>\n",
       "      <td>P12</td>\n",
       "      <td>37</td>\n",
       "      <td>30</td>\n",
       "      <td>118.4</td>\n",
       "      <td>96.2</td>\n",
       "      <td>0.9163</td>\n",
       "      <td>52.3</td>\n",
       "      <td>48.9</td>\n",
       "      <td>16.1</td>\n",
       "      <td>...</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.1</td>\n",
       "      <td>34.4</td>\n",
       "      <td>36.2</td>\n",
       "      <td>69.0</td>\n",
       "      <td>6.7</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Syracuse</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>23</td>\n",
       "      <td>111.9</td>\n",
       "      <td>93.6</td>\n",
       "      <td>0.8857</td>\n",
       "      <td>50.0</td>\n",
       "      <td>47.3</td>\n",
       "      <td>18.1</td>\n",
       "      <td>...</td>\n",
       "      <td>47.2</td>\n",
       "      <td>48.1</td>\n",
       "      <td>36.0</td>\n",
       "      <td>30.7</td>\n",
       "      <td>65.5</td>\n",
       "      <td>-0.3</td>\n",
       "      <td>F4</td>\n",
       "      <td>10.0</td>\n",
       "      <td>2016</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 25 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         TEAM CONF   G   W  ADJOE  ADJDE  BARTHAG  EFG_O  EFG_D   TOR  ...  \\\n",
       "2  Notre Dame  ACC  36  24  118.3  103.3   0.8269   54.0   49.5  15.3  ...   \n",
       "3    Virginia  ACC  37  29  119.9   91.0   0.9600   54.8   48.4  15.1  ...   \n",
       "4      Kansas  B12  37  32  120.9   90.4   0.9662   55.7   45.1  17.8  ...   \n",
       "5      Oregon  P12  37  30  118.4   96.2   0.9163   52.3   48.9  16.1  ...   \n",
       "6    Syracuse  ACC  37  23  111.9   93.6   0.8857   50.0   47.3  18.1  ...   \n",
       "\n",
       "   2P_O  2P_D  3P_O  3P_D  ADJ_T   WAB  POSTSEASON  SEED  YEAR  windex  \n",
       "2  52.9  46.5  37.4  36.9   65.5   2.3          E8   6.0  2016       0  \n",
       "3  52.6  46.3  40.3  34.7   61.9   8.6          E8   1.0  2016       1  \n",
       "4  52.7  43.4  41.3  32.5   70.1  11.6          E8   1.0  2016       1  \n",
       "5  52.6  46.1  34.4  36.2   69.0   6.7          E8   1.0  2016       0  \n",
       "6  47.2  48.1  36.0  30.7   65.5  -0.3          F4  10.0  2016       0  \n",
       "\n",
       "[5 rows x 25 columns]"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1['windex'].replace(to_replace=['False','True'], value=[0,1],inplace=True)\n",
    "df1.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Feature selection"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Lets defind feature sets, X:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>G</th>\n",
       "      <th>W</th>\n",
       "      <th>ADJOE</th>\n",
       "      <th>ADJDE</th>\n",
       "      <th>BARTHAG</th>\n",
       "      <th>EFG_O</th>\n",
       "      <th>EFG_D</th>\n",
       "      <th>TOR</th>\n",
       "      <th>TORD</th>\n",
       "      <th>ORB</th>\n",
       "      <th>...</th>\n",
       "      <th>FTR</th>\n",
       "      <th>FTRD</th>\n",
       "      <th>2P_O</th>\n",
       "      <th>2P_D</th>\n",
       "      <th>3P_O</th>\n",
       "      <th>3P_D</th>\n",
       "      <th>ADJ_T</th>\n",
       "      <th>WAB</th>\n",
       "      <th>SEED</th>\n",
       "      <th>windex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>36</td>\n",
       "      <td>24</td>\n",
       "      <td>118.3</td>\n",
       "      <td>103.3</td>\n",
       "      <td>0.8269</td>\n",
       "      <td>54.0</td>\n",
       "      <td>49.5</td>\n",
       "      <td>15.3</td>\n",
       "      <td>14.8</td>\n",
       "      <td>32.7</td>\n",
       "      <td>...</td>\n",
       "      <td>32.9</td>\n",
       "      <td>26.0</td>\n",
       "      <td>52.9</td>\n",
       "      <td>46.5</td>\n",
       "      <td>37.4</td>\n",
       "      <td>36.9</td>\n",
       "      <td>65.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>6.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>37</td>\n",
       "      <td>29</td>\n",
       "      <td>119.9</td>\n",
       "      <td>91.0</td>\n",
       "      <td>0.9600</td>\n",
       "      <td>54.8</td>\n",
       "      <td>48.4</td>\n",
       "      <td>15.1</td>\n",
       "      <td>18.8</td>\n",
       "      <td>29.9</td>\n",
       "      <td>...</td>\n",
       "      <td>32.1</td>\n",
       "      <td>33.4</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.3</td>\n",
       "      <td>40.3</td>\n",
       "      <td>34.7</td>\n",
       "      <td>61.9</td>\n",
       "      <td>8.6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>120.9</td>\n",
       "      <td>90.4</td>\n",
       "      <td>0.9662</td>\n",
       "      <td>55.7</td>\n",
       "      <td>45.1</td>\n",
       "      <td>17.8</td>\n",
       "      <td>18.5</td>\n",
       "      <td>32.2</td>\n",
       "      <td>...</td>\n",
       "      <td>38.6</td>\n",
       "      <td>37.3</td>\n",
       "      <td>52.7</td>\n",
       "      <td>43.4</td>\n",
       "      <td>41.3</td>\n",
       "      <td>32.5</td>\n",
       "      <td>70.1</td>\n",
       "      <td>11.6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>37</td>\n",
       "      <td>30</td>\n",
       "      <td>118.4</td>\n",
       "      <td>96.2</td>\n",
       "      <td>0.9163</td>\n",
       "      <td>52.3</td>\n",
       "      <td>48.9</td>\n",
       "      <td>16.1</td>\n",
       "      <td>20.2</td>\n",
       "      <td>34.1</td>\n",
       "      <td>...</td>\n",
       "      <td>40.3</td>\n",
       "      <td>32.0</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.1</td>\n",
       "      <td>34.4</td>\n",
       "      <td>36.2</td>\n",
       "      <td>69.0</td>\n",
       "      <td>6.7</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>37</td>\n",
       "      <td>23</td>\n",
       "      <td>111.9</td>\n",
       "      <td>93.6</td>\n",
       "      <td>0.8857</td>\n",
       "      <td>50.0</td>\n",
       "      <td>47.3</td>\n",
       "      <td>18.1</td>\n",
       "      <td>20.4</td>\n",
       "      <td>33.5</td>\n",
       "      <td>...</td>\n",
       "      <td>35.4</td>\n",
       "      <td>28.0</td>\n",
       "      <td>47.2</td>\n",
       "      <td>48.1</td>\n",
       "      <td>36.0</td>\n",
       "      <td>30.7</td>\n",
       "      <td>65.5</td>\n",
       "      <td>-0.3</td>\n",
       "      <td>10.0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    G   W  ADJOE  ADJDE  BARTHAG  EFG_O  EFG_D   TOR  TORD   ORB  ...   FTR  \\\n",
       "2  36  24  118.3  103.3   0.8269   54.0   49.5  15.3  14.8  32.7  ...  32.9   \n",
       "3  37  29  119.9   91.0   0.9600   54.8   48.4  15.1  18.8  29.9  ...  32.1   \n",
       "4  37  32  120.9   90.4   0.9662   55.7   45.1  17.8  18.5  32.2  ...  38.6   \n",
       "5  37  30  118.4   96.2   0.9163   52.3   48.9  16.1  20.2  34.1  ...  40.3   \n",
       "6  37  23  111.9   93.6   0.8857   50.0   47.3  18.1  20.4  33.5  ...  35.4   \n",
       "\n",
       "   FTRD  2P_O  2P_D  3P_O  3P_D  ADJ_T   WAB  SEED  windex  \n",
       "2  26.0  52.9  46.5  37.4  36.9   65.5   2.3   6.0       0  \n",
       "3  33.4  52.6  46.3  40.3  34.7   61.9   8.6   1.0       1  \n",
       "4  37.3  52.7  43.4  41.3  32.5   70.1  11.6   1.0       1  \n",
       "5  32.0  52.6  46.1  34.4  36.2   69.0   6.7   1.0       0  \n",
       "6  28.0  47.2  48.1  36.0  30.7   65.5  -0.3  10.0       0  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = df1[['G', 'W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D',\n",
    "       'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O',\n",
    "       '3P_D', 'ADJ_T', 'WAB', 'SEED', 'windex']]\n",
    "X[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "What are our lables? Round where the given team was eliminated or where their season ended (R68 = First Four, R64 = Round of 64, R32 = Round of 32, S16 = Sweet Sixteen, E8 = Elite Eight, F4 = Final Four, 2ND = Runner-up, Champion = Winner of the NCAA March Madness Tournament for that given year)|"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['E8', 'E8', 'E8', 'E8', 'F4'], dtype=object)"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y = df1['POSTSEASON'].values\n",
    "y[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## Normalize Data "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Data Standardization give data zero mean and unit variance (technically should be done after train test split )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\preprocessing\\data.py:645: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  return self.partial_fit(X, y)\n",
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:1: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[-0.43331874, -1.26140173,  0.28034482,  2.74329908, -2.45717765,\n",
       "         0.10027963,  0.94171924, -1.16188145, -1.71391372,  0.12750511,\n",
       "         1.33368704, -0.4942211 , -0.87998988,  0.02784185,  0.00307239,\n",
       "         0.22576157,  1.59744386, -1.12106011, -1.0448016 ,  0.49716104,\n",
       "        -0.6882472 ],\n",
       "       [ 0.40343468,  0.35874728,  0.64758014, -0.90102957,  1.127076  ,\n",
       "         0.39390887,  0.38123706, -1.29466791, -0.03522254, -0.62979797,\n",
       "        -1.31585883, -0.68542235,  0.55458056, -0.07167795, -0.0829545 ,\n",
       "         1.32677295,  0.65081046, -2.369021  ,  0.98050611, -1.14054592,\n",
       "         1.45296631],\n",
       "       [ 0.40343468,  1.33083669,  0.87710222, -1.0788017 ,  1.29403598,\n",
       "         0.72424177, -1.30020946,  0.49794919, -0.16112438, -0.00772758,\n",
       "        -0.27908001,  0.86808783,  1.31063795, -0.03850468, -1.33034432,\n",
       "         1.70643205, -0.29582294,  0.47355659,  1.94493836, -1.14054592,\n",
       "         1.45296631],\n",
       "       [ 0.40343468,  0.68277708,  0.30329703,  0.63966222, -0.04972253,\n",
       "        -0.52368251,  0.63600169, -0.63073565,  0.55231938,  0.50615665,\n",
       "         0.71929959,  1.2743905 ,  0.28317534, -0.07167795, -0.16898138,\n",
       "        -0.91321572,  1.29624232,  0.0922352 ,  0.36969903, -1.14054592,\n",
       "        -0.6882472 ],\n",
       "       [ 0.40343468, -1.58543153, -1.18859646, -0.13068368, -0.87375079,\n",
       "        -1.36786658, -0.17924511,  0.69712887,  0.63625394,  0.34387742,\n",
       "         2.56246194,  0.10328282, -0.49226814, -1.8630343 ,  0.69128747,\n",
       "        -0.30576117, -1.07034117, -1.12106011, -1.88064288,  1.80732661,\n",
       "        -0.6882472 ]])"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X= preprocessing.StandardScaler().fit(X).transform(X)\n",
    "X[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## Training and Validation "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Split the data into Training and Validation data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train set: (44, 21) (44,)\n",
      "Validation set: (12, 21) (12,)\n"
     ]
    }
   ],
   "source": [
    "# We split the X into train and test to find the best k\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=4)\n",
    "print ('Train set:', X_train.shape,  y_train.shape)\n",
    "print ('Validation set:', X_val.shape,  y_val.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "# Classification "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Now, it is your turn, use the training set to build an accurate model. Then use the validation set  to report the accuracy of the model\n",
    "You should use the following algorithm:\n",
    "- K Nearest Neighbor(KNN)\n",
    "- Decision Tree\n",
    "- Support Vector Machine\n",
    "- Logistic Regression\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# K Nearest Neighbor(KNN)\n",
    "\n",
    "<b>Question  1 </b> Build a KNN model using a value of k equals five, find the accuracy on the validation data (X_val and y_val)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can use <code> accuracy_score</cdoe>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train set Accuracy:  0.6363636363636364\n",
      "Test set Accuracy:  0.6666666666666666\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "\n",
    "k = 5\n",
    "#Train Model and Predict  \n",
    "knn_model = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)\n",
    "\n",
    "yhat = knn_model.predict(X_val)\n",
    "yhat[0:5]\n",
    "\n",
    "from sklearn import metrics\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, knn_model.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Question  2</b> Determine and print the accuracy for the first 15 values of k the on the validation data:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.33333333 0.33333333 0.5        0.58333333 0.66666667 0.58333333\n",
      " 0.58333333 0.66666667 0.58333333 0.58333333 0.58333333 0.5\n",
      " 0.58333333 0.58333333 0.58333333]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Ks = 16\n",
    "mean_acc = np.zeros((Ks-1))\n",
    "std_acc = np.zeros((Ks-1))\n",
    "ConfustionMx = [];\n",
    "for n in range(1,Ks):\n",
    "    \n",
    "    #Train Model and Predict  \n",
    "    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)\n",
    "    yhat=neigh.predict(X_val)\n",
    "    mean_acc[n-1] = metrics.accuracy_score(y_val, yhat)\n",
    "\n",
    "    \n",
    "    std_acc[n-1]=np.std(yhat==y_val)/np.sqrt(yhat.shape[0])\n",
    "\n",
    "print(mean_acc)\n",
    "\n",
    "plt.plot(range(1,Ks),mean_acc,'g')\n",
    "plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)\n",
    "plt.legend(('Accuracy ', '+/- 3xstd'))\n",
    "plt.ylabel('Accuracy ')\n",
    "plt.xlabel('Number of Neighbors (K)')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Decision Tree"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The following lines of code fit a <code>DecisionTreeClassifier</code>:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=2,\n",
       "            max_features=None, max_leaf_nodes=None,\n",
       "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
       "            min_samples_leaf=1, min_samples_split=2,\n",
       "            min_weight_fraction_leaf=0.0, presort=False, random_state=None,\n",
       "            splitter='best')"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "DT_model = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 2)\n",
    "DT_model.fit(X_train,y_train)\n",
    "DT_model"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Question  3</b> Determine the minumum   value for the parameter <code>max_depth</code> that improves results "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.66666667 0.66666667 0.5        0.33333333 0.5        0.41666667\n",
      " 0.5        0.41666667 0.41666667]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Ks = 10\n",
    "mean_acc = np.zeros((Ks-1))\n",
    "std_acc = np.zeros((Ks-1))\n",
    "ConfustionMx = [];\n",
    "for n in range(1,Ks):\n",
    "    \n",
    "    #Train Model and Predict  \n",
    "    dt = DecisionTreeClassifier(criterion=\"entropy\", max_depth = n).fit(X_train,y_train)\n",
    "    yhat=dt.predict(X_val)\n",
    "    mean_acc[n-1] = metrics.accuracy_score(y_val, yhat)\n",
    "\n",
    "    \n",
    "    std_acc[n-1]=np.std(yhat==y_val)/np.sqrt(yhat.shape[0])\n",
    "\n",
    "print(mean_acc)\n",
    "\n",
    "plt.plot(range(1,Ks),mean_acc,'g')\n",
    "plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)\n",
    "plt.legend(('Accuracy ', '+/- 3xstd'))\n",
    "plt.ylabel('Accuracy ')\n",
    "plt.xlabel('max_depth')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train set Accuracy:  0.6818181818181818\n",
      "Test set Accuracy:  0.6666666666666666\n"
     ]
    }
   ],
   "source": [
    "from sklearn.tree import DecisionTreeClassifier\n",
    "DT_model = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 2)\n",
    "DT_model.fit(X_train,y_train)\n",
    "DT_model\n",
    "\n",
    "yhat = DT_model.predict(X_val)\n",
    "yhat\n",
    "\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, DT_model.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Therefore minimum max_depth value = 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Question  4\n",
    "\n",
    "</b>Train the support  vector machine model and determine the accuracy on the validation data for each kernel. Find the kernel (linear, poly, rbf, sigmoid) that provides the best score on the validation data and train a SVM using it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import svm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Train set Accuracy:  0.9318181818181818\n",
      "Test set Accuracy:  0.25\n",
      "Train set Accuracy:  0.6363636363636364\n",
      "Test set Accuracy:  0.5\n",
      "Train set Accuracy:  0.8409090909090909\n",
      "Test set Accuracy:  0.5833333333333334\n",
      "Train set Accuracy:  0.75\n",
      "Test set Accuracy:  0.6666666666666666\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\base.py:196: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.\n",
      "  \"avoid this warning.\", FutureWarning)\n",
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\base.py:196: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.\n",
      "  \"avoid this warning.\", FutureWarning)\n",
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\base.py:196: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.\n",
      "  \"avoid this warning.\", FutureWarning)\n"
     ]
    }
   ],
   "source": [
    "svmodel = svm.SVC(kernel = 'linear')\n",
    "svmodel.fit(X_train, y_train)\n",
    "yhat = svmodel.predict(X_val)\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, svmodel.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))\n",
    "\n",
    "svmodel = svm.SVC(kernel = 'sigmoid')\n",
    "svmodel.fit(X_train, y_train)\n",
    "yhat = svmodel.predict(X_val)\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, svmodel.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))\n",
    "\n",
    "svmodel = svm.SVC(kernel = 'rbf')\n",
    "svmodel.fit(X_train, y_train)\n",
    "yhat = svmodel.predict(X_val)\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, svmodel.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))\n",
    "\n",
    "svmodel = svm.SVC(kernel = 'poly')\n",
    "svmodel.fit(X_train, y_train)\n",
    "yhat = svmodel.predict(X_val)\n",
    "print(\"Train set Accuracy: \", metrics.accuracy_score(y_train, svmodel.predict(X_train)))\n",
    "print(\"Test set Accuracy: \", metrics.accuracy_score(y_val, yhat))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 0 0]\n",
      " [0 4 4]\n",
      " [0 1 1]]\n",
      "Confusion matrix, without normalization\n",
      "[[2 0 0]\n",
      " [0 4 4]\n",
      " [0 1 1]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "import itertools\n",
    "def plot_confusion_matrix(cm, classes,\n",
    "                          normalize=False,\n",
    "                          title='Confusion matrix',\n",
    "                          cmap=plt.cm.Blues):\n",
    "    \"\"\"\n",
    "    This function prints and plots the confusion matrix.\n",
    "    Normalization can be applied by setting `normalize=True`.\n",
    "    \"\"\"\n",
    "    if normalize:\n",
    "        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]\n",
    "        print(\"Normalized confusion matrix\")\n",
    "    else:\n",
    "        print('Confusion matrix, without normalization')\n",
    "\n",
    "    print(cm)\n",
    "\n",
    "    plt.imshow(cm, interpolation='nearest', cmap=cmap)\n",
    "    plt.title(title)\n",
    "    plt.colorbar()\n",
    "    tick_marks = np.arange(len(classes))\n",
    "    plt.xticks(tick_marks, classes, rotation=45)\n",
    "    plt.yticks(tick_marks, classes)\n",
    "\n",
    "    fmt = '.2f' if normalize else 'd'\n",
    "    thresh = cm.max() / 2.\n",
    "    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):\n",
    "        plt.text(j, i, format(cm[i, j], fmt),\n",
    "                 horizontalalignment=\"center\",\n",
    "                 color=\"white\" if cm[i, j] > thresh else \"black\")\n",
    "\n",
    "    plt.tight_layout()\n",
    "    plt.ylabel('True label')\n",
    "    plt.xlabel('Predicted label')\n",
    "print(confusion_matrix(y_val, yhat, labels=['F4', 'S16', 'E8']))\n",
    "\n",
    "# Compute confusion matrix\n",
    "cnf_matrix = confusion_matrix(y_val, yhat, labels=['F4', 'S16', 'E8'])\n",
    "np.set_printoptions(precision=2)\n",
    "\n",
    "\n",
    "# Plot non-normalized confusion matrix\n",
    "plt.figure()\n",
    "plot_confusion_matrix(cnf_matrix, classes=['1','0','-1'],normalize= False,  title='Confusion matrix')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Logistic Regression"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Question 5</b> Train a logistic regression model and determine the accuracy of the validation data (set C=0.01)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:460: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=0.01, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
       "          n_jobs=None, penalty='l2', random_state=None, solver='liblinear',\n",
       "          tol=0.0001, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "LR = LogisticRegression(C=0.01, solver='liblinear').fit(X_train,y_train)\n",
    "LR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['F4', 'S16', 'E8', 'E8', 'E8', 'E8', 'S16', 'F4', 'E8', 'S16',\n",
       "       'S16', 'S16'], dtype=object)"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yhat = LR.predict(X_val)\n",
    "yhat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.31, 0.36, 0.33],\n",
       "       [0.33, 0.33, 0.35],\n",
       "       [0.36, 0.31, 0.33],\n",
       "       [0.39, 0.35, 0.26],\n",
       "       [0.35, 0.33, 0.32],\n",
       "       [0.34, 0.32, 0.34],\n",
       "       [0.32, 0.34, 0.34],\n",
       "       [0.33, 0.35, 0.33],\n",
       "       [0.35, 0.32, 0.33],\n",
       "       [0.32, 0.31, 0.37],\n",
       "       [0.34, 0.3 , 0.35],\n",
       "       [0.33, 0.29, 0.37]])"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "yhat_prob = LR.predict_proba(X_val)\n",
    "yhat_prob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2 0 0]\n",
      " [0 4 4]\n",
      " [0 1 1]]\n"
     ]
    }
   ],
   "source": [
    "from sklearn.metrics import classification_report, confusion_matrix\n",
    "import itertools\n",
    "def plot_confusion_matrix(cm, classes,\n",
    "                          normalize=False,\n",
    "                          title='Confusion matrix',\n",
    "                          cmap=plt.cm.Blues):\n",
    "    \"\"\"\n",
    "    This function prints and plots the confusion matrix.\n",
    "    Normalization can be applied by setting `normalize=True`.\n",
    "    \"\"\"\n",
    "    if normalize:\n",
    "        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]\n",
    "        print(\"Normalized confusion matrix\")\n",
    "    else:\n",
    "        print('Confusion matrix, without normalization')\n",
    "\n",
    "    print(cm)\n",
    "\n",
    "    plt.imshow(cm, interpolation='nearest', cmap=cmap)\n",
    "    plt.title(title)\n",
    "    plt.colorbar()\n",
    "    tick_marks = np.arange(len(classes))\n",
    "    plt.xticks(tick_marks, classes, rotation=45)\n",
    "    plt.yticks(tick_marks, classes)\n",
    "\n",
    "    fmt = '.2f' if normalize else 'd'\n",
    "    thresh = cm.max() / 2.\n",
    "    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):\n",
    "        plt.text(j, i, format(cm[i, j], fmt),\n",
    "                 horizontalalignment=\"center\",\n",
    "                 color=\"white\" if cm[i, j] > thresh else \"black\")\n",
    "\n",
    "    plt.tight_layout()\n",
    "    plt.ylabel('True label')\n",
    "    plt.xlabel('Predicted label')\n",
    "print(confusion_matrix(y_val, yhat, labels=['F4', 'S16', 'E8']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Confusion matrix, without normalization\n",
      "[[2 0 0]\n",
      " [0 4 4]\n",
      " [0 1 1]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Compute confusion matrix\n",
    "cnf_matrix = confusion_matrix(y_val, yhat, labels=['F4', 'S16', 'E8'])\n",
    "np.set_printoptions(precision=2)\n",
    "\n",
    "\n",
    "# Plot non-normalized confusion matrix\n",
    "plt.figure()\n",
    "plot_confusion_matrix(cnf_matrix, classes=['1','0','-1'],normalize= False,  title='Confusion matrix')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Model Evaluation using Test set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import f1_score\n",
    "# for f1_score please set the average parameter to 'micro'\n",
    "from sklearn.metrics import log_loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
   "source": [
    "def jaccard_index(predictions, true):\n",
    "    if (len(predictions) == len(true)):\n",
    "        intersect = 0;\n",
    "        for x,y in zip(predictions, true):\n",
    "            if (x == y):\n",
    "                intersect += 1\n",
    "        return intersect / (len(predictions) + len(true) - intersect)\n",
    "    else:\n",
    "        return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<b>Question  5</b> Calculate the  F1 score and Jaccard Similarity score for each model from above. Use the Hyperparameter that performed best on the validation data. **For f1_score please set the average parameter to 'micro'.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Load Test set for evaluation "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>TEAM</th>\n",
       "      <th>CONF</th>\n",
       "      <th>G</th>\n",
       "      <th>W</th>\n",
       "      <th>ADJOE</th>\n",
       "      <th>ADJDE</th>\n",
       "      <th>BARTHAG</th>\n",
       "      <th>EFG_O</th>\n",
       "      <th>EFG_D</th>\n",
       "      <th>TOR</th>\n",
       "      <th>...</th>\n",
       "      <th>FTRD</th>\n",
       "      <th>2P_O</th>\n",
       "      <th>2P_D</th>\n",
       "      <th>3P_O</th>\n",
       "      <th>3P_D</th>\n",
       "      <th>ADJ_T</th>\n",
       "      <th>WAB</th>\n",
       "      <th>POSTSEASON</th>\n",
       "      <th>SEED</th>\n",
       "      <th>YEAR</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>North Carolina</td>\n",
       "      <td>ACC</td>\n",
       "      <td>40</td>\n",
       "      <td>33</td>\n",
       "      <td>123.3</td>\n",
       "      <td>94.9</td>\n",
       "      <td>0.9531</td>\n",
       "      <td>52.6</td>\n",
       "      <td>48.1</td>\n",
       "      <td>15.4</td>\n",
       "      <td>...</td>\n",
       "      <td>30.4</td>\n",
       "      <td>53.9</td>\n",
       "      <td>44.6</td>\n",
       "      <td>32.7</td>\n",
       "      <td>36.2</td>\n",
       "      <td>71.7</td>\n",
       "      <td>8.6</td>\n",
       "      <td>2ND</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Villanova</td>\n",
       "      <td>BE</td>\n",
       "      <td>40</td>\n",
       "      <td>35</td>\n",
       "      <td>123.1</td>\n",
       "      <td>90.9</td>\n",
       "      <td>0.9703</td>\n",
       "      <td>56.1</td>\n",
       "      <td>46.7</td>\n",
       "      <td>16.3</td>\n",
       "      <td>...</td>\n",
       "      <td>30.0</td>\n",
       "      <td>57.4</td>\n",
       "      <td>44.1</td>\n",
       "      <td>36.2</td>\n",
       "      <td>33.9</td>\n",
       "      <td>66.7</td>\n",
       "      <td>8.9</td>\n",
       "      <td>Champions</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Notre Dame</td>\n",
       "      <td>ACC</td>\n",
       "      <td>36</td>\n",
       "      <td>24</td>\n",
       "      <td>118.3</td>\n",
       "      <td>103.3</td>\n",
       "      <td>0.8269</td>\n",
       "      <td>54.0</td>\n",
       "      <td>49.5</td>\n",
       "      <td>15.3</td>\n",
       "      <td>...</td>\n",
       "      <td>26.0</td>\n",
       "      <td>52.9</td>\n",
       "      <td>46.5</td>\n",
       "      <td>37.4</td>\n",
       "      <td>36.9</td>\n",
       "      <td>65.5</td>\n",
       "      <td>2.3</td>\n",
       "      <td>E8</td>\n",
       "      <td>6.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Virginia</td>\n",
       "      <td>ACC</td>\n",
       "      <td>37</td>\n",
       "      <td>29</td>\n",
       "      <td>119.9</td>\n",
       "      <td>91.0</td>\n",
       "      <td>0.9600</td>\n",
       "      <td>54.8</td>\n",
       "      <td>48.4</td>\n",
       "      <td>15.1</td>\n",
       "      <td>...</td>\n",
       "      <td>33.4</td>\n",
       "      <td>52.6</td>\n",
       "      <td>46.3</td>\n",
       "      <td>40.3</td>\n",
       "      <td>34.7</td>\n",
       "      <td>61.9</td>\n",
       "      <td>8.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kansas</td>\n",
       "      <td>B12</td>\n",
       "      <td>37</td>\n",
       "      <td>32</td>\n",
       "      <td>120.9</td>\n",
       "      <td>90.4</td>\n",
       "      <td>0.9662</td>\n",
       "      <td>55.7</td>\n",
       "      <td>45.1</td>\n",
       "      <td>17.8</td>\n",
       "      <td>...</td>\n",
       "      <td>37.3</td>\n",
       "      <td>52.7</td>\n",
       "      <td>43.4</td>\n",
       "      <td>41.3</td>\n",
       "      <td>32.5</td>\n",
       "      <td>70.1</td>\n",
       "      <td>11.6</td>\n",
       "      <td>E8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2016</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 24 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "             TEAM CONF   G   W  ADJOE  ADJDE  BARTHAG  EFG_O  EFG_D   TOR  \\\n",
       "0  North Carolina  ACC  40  33  123.3   94.9   0.9531   52.6   48.1  15.4   \n",
       "1       Villanova   BE  40  35  123.1   90.9   0.9703   56.1   46.7  16.3   \n",
       "2      Notre Dame  ACC  36  24  118.3  103.3   0.8269   54.0   49.5  15.3   \n",
       "3        Virginia  ACC  37  29  119.9   91.0   0.9600   54.8   48.4  15.1   \n",
       "4          Kansas  B12  37  32  120.9   90.4   0.9662   55.7   45.1  17.8   \n",
       "\n",
       "   ...  FTRD  2P_O  2P_D  3P_O  3P_D  ADJ_T   WAB  POSTSEASON  SEED  YEAR  \n",
       "0  ...  30.4  53.9  44.6  32.7  36.2   71.7   8.6         2ND   1.0  2016  \n",
       "1  ...  30.0  57.4  44.1  36.2  33.9   66.7   8.9   Champions   2.0  2016  \n",
       "2  ...  26.0  52.9  46.5  37.4  36.9   65.5   2.3          E8   6.0  2016  \n",
       "3  ...  33.4  52.6  46.3  40.3  34.7   61.9   8.6          E8   1.0  2016  \n",
       "4  ...  37.3  52.7  43.4  41.3  32.5   70.1  11.6          E8   1.0  2016  \n",
       "\n",
       "[5 rows x 24 columns]"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_df = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0120ENv3/Dataset/ML0101EN_EDX_skill_up/basketball_train.csv',error_bad_lines=False)\n",
    "test_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\pandas\\core\\generic.py:6586: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy\n",
      "  self._update_inplace(new_data)\n",
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\preprocessing\\data.py:645: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  return self.partial_fit(X, y)\n",
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py:8: DataConversionWarning: Data with input dtype int64, float64 were all converted to float64 by StandardScaler.\n",
      "  \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[-4.08e-01, -1.10e+00,  3.37e-01,  2.66e+00, -2.47e+00,  2.14e-01,\n",
       "         9.44e-01, -1.19e+00, -1.64e+00,  1.45e-02,  1.30e+00, -6.24e-01,\n",
       "        -9.32e-01,  1.43e-01,  1.69e-01,  2.85e-01,  1.63e+00, -8.37e-01,\n",
       "        -9.99e-01,  4.84e-01, -6.77e-01],\n",
       "       [ 3.64e-01,  3.26e-01,  7.03e-01, -7.14e-01,  1.07e+00,  4.83e-01,\n",
       "         4.77e-01, -1.33e+00, -6.86e-02, -7.35e-01, -1.35e+00, -8.07e-01,\n",
       "         3.42e-01,  4.97e-02,  9.41e-02,  1.37e+00,  6.94e-01, -2.01e+00,\n",
       "         9.81e-01, -1.19e+00,  1.48e+00],\n",
       "       [ 3.64e-01,  1.18e+00,  9.32e-01, -8.79e-01,  1.24e+00,  7.85e-01,\n",
       "        -9.22e-01,  5.28e-01, -1.87e-01, -1.19e-01, -3.18e-01,  6.82e-01,\n",
       "         1.01e+00,  8.07e-02, -9.91e-01,  1.75e+00, -2.39e-01,  6.61e-01,\n",
       "         1.92e+00, -1.19e+00,  1.48e+00],\n",
       "       [ 3.64e-01,  6.12e-01,  3.60e-01,  7.15e-01, -8.92e-02, -3.58e-01,\n",
       "         6.90e-01, -6.42e-01,  4.83e-01,  3.90e-01,  6.81e-01,  1.07e+00,\n",
       "         1.01e-01,  4.97e-02,  1.92e-02, -8.41e-01,  1.33e+00,  3.03e-01,\n",
       "         3.84e-01, -1.19e+00, -6.77e-01],\n",
       "       [ 3.64e-01, -1.39e+00, -1.13e+00,  3.92e-04, -9.04e-01, -1.13e+00,\n",
       "         1.09e-02,  7.34e-01,  5.61e-01,  2.29e-01,  2.52e+00, -5.07e-02,\n",
       "        -5.88e-01, -1.63e+00,  7.67e-01, -2.41e-01, -1.00e+00, -8.37e-01,\n",
       "        -1.82e+00,  1.83e+00, -6.77e-01]])"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_df['windex'] = np.where(test_df.WAB > 7, 'True', 'False')\n",
    "test_df1 = test_df[test_df['POSTSEASON'].str.contains('F4|S16|E8', na=False)]\n",
    "test_Feature = test_df1[['G', 'W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D',\n",
    "       'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O',\n",
    "       '3P_D', 'ADJ_T', 'WAB', 'SEED', 'windex']]\n",
    "test_Feature['windex'].replace(to_replace=['False','True'], value=[0,1],inplace=True)\n",
    "test_X=test_Feature\n",
    "test_X= preprocessing.StandardScaler().fit(test_X).transform(test_X)\n",
    "test_X[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['E8', 'E8', 'E8', 'E8', 'F4'], dtype=object)"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test_y = test_df1['POSTSEASON'].values\n",
    "test_y[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "KNN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN Jaccard index: 0.46\n",
      "KNN F1-score: 0.62\n"
     ]
    }
   ],
   "source": [
    "knn_yhat = knn_model.predict(test_X)\n",
    "print(\"KNN Jaccard index: %.2f\" % jaccard_index(test_y, knn_yhat))\n",
    "print(\"KNN F1-score: %.2f\" % f1_score(test_y, knn_yhat, average='weighted') )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Decision Tree"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN Jaccard index: 0.49\n",
      "KNN F1-score: 0.57\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\PRADYUM\\Anaconda3\\lib\\site-packages\\sklearn\\metrics\\classification.py:1143: UndefinedMetricWarning: F-score is ill-defined and being set to 0.0 in labels with no predicted samples.\n",
      "  'precision', 'predicted', average, warn_for)\n"
     ]
    }
   ],
   "source": [
    "DT_model = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 2)\n",
    "DT_model.fit(X_train,y_train)\n",
    "dt_yhat = DT_model.predict(test_X)\n",
    "print(\"KNN Jaccard index: %.2f\" % jaccard_index(test_y, dt_yhat))\n",
    "print(\"KNN F1-score: %.2f\" % f1_score(test_y, dt_yhat, average='weighted') )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "SVM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN Jaccard index: 0.52\n",
      "KNN F1-score: 0.64\n"
     ]
    }
   ],
   "source": [
    "sv_yhat = svmodel.predict(test_X)\n",
    "print(\"KNN Jaccard index: %.2f\" % jaccard_index(test_y, sv_yhat))\n",
    "print(\"KNN F1-score: %.2f\" % f1_score(test_y, sv_yhat, average='weighted') )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Logistic Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KNN Jaccard index: 0.52\n",
      "KNN F1-score: 0.69\n"
     ]
    }
   ],
   "source": [
    "LR_yhat = LR.predict(test_X)\n",
    "print(\"KNN Jaccard index: %.2f\" % jaccard_index(test_y, LR_yhat))\n",
    "print(\"KNN F1-score: %.2f\" % f1_score(test_y, LR_yhat, average='weighted') )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Report\n",
    "You should be able to report the accuracy of the built model using different evaluation metrics:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "| Algorithm          | Accuracy | Jaccard  | F1-score  | LogLoss |\n",
    "|--------------------|----------|----------|-----------|---------|\n",
    "| KNN                |0.628571  | 0.458333 | 0.628571  | NA      |\n",
    "| Decision Tree      |0.642857  | 0.473684 | 0.642857  | NA      |\n",
    "| SVM                |0.685714  | 0.521739 | 0.685714  | NA      |\n",
    "| LogisticRegression |0.685714  | 0.521739 | 0.685714  | 1.03719 |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Something to keep in mind when creating models to predict the results of basketball tournaments or sports in general is that is quite hard due to so many factors influencing the game. Even in sports betting an accuracy of 55% and over is considered good as it indicates profits."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<h2>Want to learn more?</h2>\n",
    "\n",
    "IBM SPSS Modeler is a comprehensive analytics platform that has many machine learning algorithms. It has been designed to bring predictive intelligence to decisions made by individuals, by groups, by systems – by your enterprise as a whole. A free trial is available through this course, available here: <a href=\"http://cocl.us/ML0101EN-SPSSModeler\">SPSS Modeler</a>\n",
    "\n",
    "Also, you can use Watson Studio to run these notebooks faster with bigger datasets. Watson Studio is IBM's leading cloud solution for data scientists, built by data scientists. With Jupyter notebooks, RStudio, Apache Spark and popular libraries pre-packaged in the cloud, Watson Studio enables data scientists to collaborate on their projects without having to install anything. Join the fast-growing community of Watson Studio users today with a free account at <a href=\"https://cocl.us/ML0101EN_DSX\">Watson Studio</a>\n",
    "\n",
    "<h3>Thanks for completing this lesson!</h3>\n",
    "\n",
    "<h4>Authors: <a href=\"https://www.linkedin.com/in/azim-hirjani-691a07179/\">Azim Hirjani</a> and <a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a></h4>\n",
    "\n",
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n",
    "\n",
    "\n",
    "\n",
    "<hr>\n",
    "\n",
    "<p>Copyright &copy; 2018 <a href=\"https://cocl.us/DX0108EN_CC\">Cognitive Class</a>. This notebook and its source code are released under the terms of the <a href=\"https://bigdatauniversity.com/mit-license/\">MIT License</a>.</p>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
