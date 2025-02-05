import os
from datetime import datetime, timedelta
from random import randint as ri

# Configure the number of days back and the frequency of commits
start_year = 2018  # Start from 2018
end_date = datetime.now()  # Current date
total_days = (end_date - datetime(start_year, 1, 1)).days  # Total number of days from 2018 to now
commit_freq = 10  # Number of commits per day
variability = True  # Set True if you want variable commit frequency

# Set your repository link
repo_link = "https://www.github.com/ravuga/ravuga.git"

# Initialize variables
pointer = 0
ctr = 1
now = datetime.now()

# Start a new git repository
os.system("git init")

# Open a file to record commit dates
with open("commit.txt", "w") as f:
    # Generate commits from 2018 to the current date
    while total_days > 0:
        # Determine the number of commits for today
        ct = ri(1, commit_freq + 1) if variability else commit_freq
        
        # For each commit of the day, generate a commit with the date
        while ct > 0:
            commit_date = now - timedelta(days=pointer)
            formatted_date = commit_date.strftime("%Y-%m-%d")
            
            # Write commit info to file
            f.write(f"commit ke {ctr}: {formatted_date}\n")
            
            # Add file changes and commit
            os.system("git add .")
            os.system(f'git commit --date="{formatted_date} 12:15:10" -m "commit ke {ctr}"')
            print(f"commit ke {ctr}: {formatted_date}")
            
            ct -= 1
            ctr += 1

        # Move to the next day
        pointer += 1
        total_days -= 1

# Set the remote repository and push to GitHub
os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")
