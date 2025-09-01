#!/usr/bin/env python3

import argparse
import urllib.request
import json
import sys

def main():
    # Read the username from the terminal
    parser = argparse.ArgumentParser(description='Show a GitHub user\'s activity')
    parser.add_argument('username', help='GitHub username')
    args = parser.parse_args()

    username = args.username
    print(f'User to consult: {username}')

    # Build the GitHub API URL with that username
    url = f"https://api.github.com/users/{username}/events"

    try: 
        with urllib.request.urlopen(url) as response: # Make the HTTP request
            data = response.read().decode('utf-8') #  Convert JSON to a Python object
            events = json.loads(data)
    except Exception as e:
        print(f' Error when querying the API: {e}')
        sys.exit(1)
    
# Display the last 5 events on screen
    for event in events[:5]:
        event_type = event.get('type', 'UnknownEvent')
        repo_name = event['repo']['name']
        print(f'{username} did {event_type} in {repo_name}')
        """
        if event_type == 'PushEvent':
            print(f'{username} pushed on {repo_name}')
        elif event_type == 'IssuesEvent':
            print(f'{username} opened an issue in {repo_name}')
        elif event_type == 'WatchEvent':
            print(f'gave star to {repo_name}')
        else:
            print(f'{username} did {event_type} in {repo_name}')
        """
if __name__ == "__main__":
    main()