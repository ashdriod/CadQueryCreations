#!/bin/bash

# Set the path to your repository
REPO_DIR="$HOME/Documents/CadQueryCreations"

# Navigate to your repository's directory
cd $REPO_DIR

# Check for untracked files
if git status | grep 'Untracked files:' -A 1 | grep -q '.'; then
    echo "New files detected. Adding to GitHub..."

    # Add all new (untracked) files to the staging area
    git add .

    # Commit the new files with a specific message
    git commit -m "New cadqurty file got added"

    # Push the changes to your GitHub repository
    git push origin main

    echo "New files added and pushed to GitHub."
else
    echo "No new files to add."
fi

