# Yahoo Fantasy Basketball Helper

## Current Features

* Start active players for the next few days

## Dependencies

* Python 2.7
* BeautifulSoup4
```bash
pip install beautifulsoup4
```
* yahooscraper 0.3.0 (https://github.com/jbrudvik/yahooscraper)
I modified this package into `fantasy_login.py` and `fantasy_team.py`

## Run the program

First, you need to set up the authentication and your fantasy team info in the `config.ini` file.
To find the League ID and Team ID, you need to go to your fantasy page and click MyTeam,
then you can find the league ID and team ID at the end of the URL.

To run the program

```
python startActivePlayers.py
```

You will be prompted to enter the number of days you want this script to help you start active players.