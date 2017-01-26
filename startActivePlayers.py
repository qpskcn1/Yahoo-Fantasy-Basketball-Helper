import sys
import fantasy_login as login
import fantasy_team as tm
from urlparse import urljoin

from datetime import datetime, date, timedelta

def usage():
    """
    Print usage and exit
    """
    msg_lines = [' username and password is empty ']
    sys.exit('\n\n'.join(msg_lines))

def output_team_info(session, league_id, team_id):
    """
    Output team name and league
    """
    response = session.get(tm.url('nba', league_id, team_id))
    league = tm.league(response.text)
    team = tm.team(response.text)
    print("Success!")
    print('League Name: %s \nTeam Name: %s\n' % (league, team))

def start_active_players(session, league_id, team_id, start_date=None):
    """
    Start active players and output results
    """
    # Load team page
    team_url = tm.url('nba', league_id, team_id, start_date)
    response = session.get(team_url)

    # Press "Start Active Players" button
    start_path = tm.start_active_players_path(response.text)
    start_url = urljoin(response.url, start_path)
    response = session.get(start_url)

    # If unsuccessful, report failure
    formatted_date = tm.date(response.text)
    if not (200 <= response.status_code < 300):
        print('- %s: Failed to start active players' % formatted_date)

    # Report success and highlight available bench players
    print('- %s: Started active players' % formatted_date)
    alternates = tm.alternates(response.text)
    for player in alternates:
        print('    - Alternate: %s (%s) [%s]' % (
            player['name'],
            player['details'],
            player['opponent']))

def main():
	username = ''
	password = ''
	league_id = 15712
	team_id = 4
	if username is None or password is None:
		usage()

	try:
		print("Loading...Please wait...")
		session = login.authenticated_session(username, password)
		output_team_info(session, league_id, team_id)
	except:
		sys.exit("Login Failed")

	start_date = date.today()
	num_days = 2
	try:
		for _ in range(num_days):
			start_active_players(session, league_id, team_id, start_date)
			start_date = start_date + timedelta(days=1)
	except:
		sys.exit("Faild To Start Players")


if __name__ == '__main__':
    main()