# GitHub User Activity CLI

This is a simple command-line tool that lets you check a GitHub user's recent activity right from your terminal. Perfect for quickly seeing what someone’s been up to on GitHub without opening a browser.

## Features

- Show the latest GitHub events of a user  
- Displays **Pushes**, **Issues**, **Stars**, and **Create events**  
- Timestamps included for each event  
- Gracefully handles users with no recent activity  

## How to Use

Run the script from your terminal and pass the GitHub username:

```bash
python github_activity.py <username>

```

Output will look like:

```bash
01/09/2025 03:02:23 <username> pushed on <username>/my-repo
01/09/2025 03:15:10 <username> opened an issue in <username>/my-repo
01/09/2025 03:20:00 <username> gave star to <username>/hello-world
01/09/2025 03:25:42 <username> created a new repository in <username>/new-project

```

If the user has no recent activity, it’ll just tell you:

```bash
 <username> has no recent activity.

```

## How It Works

- Fetches data using the GitHub API

- Parses the JSON events

- Formats the timestamps using Python’s datetime module

- Shows a clean, readable summary in the terminal

## Requirements

- Python 3.x

- No external libraries needed (uses argparse, urllib.request json, and datetime)

## Future Ideas

- Filter events by type (e.g., only show pushes)

- Show more events or all events

- Cache results to avoid hitting GitHub API limits
