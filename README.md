# This repository stores helpful scripts that have been used by the Solution Architects at Mattermost

The workflow to add new scripts follows the same rules as always:

1. Clone the repository
2. Create a branch
3. Commit your changes
4. Create a pull request and add minimum 1 reviewer
5. Delete your branch after the merge

|folder|purpose|language|author|
|---|---|---|---|
|ad-scripts |Powershell script to translate AD attributes into JSONL for bulkimport. Usage video: https://www.youtube.com/watch?v=4AsGu0qacvI |PowerShell |Christian Johannsen |
|get-data |Scripts to gather data from Mattermost (Channels, Posts, Users etc.) |python |Christian Johannsen |
|live-importer |Script to import data from another Mattermost server (Test to Prod etc.) |python |Christian Johannsen |
|set-user-attributes |Script to set user attributes from a central location |python |Christian Johannsen |
|upload-files |Script to upload files to Mattermost |python |Christian Johannsen |
|websocket-listener  |Script to check for websocket events to develop reactions (Sharepoint site, Message popup, alarm etc.) |python |Christian Johannsen |
|account-settings  |User input script to set specific Account menu settings (Sidebar) for all users. The script will read all active users and give the option for the administrator to set the sidebar settings for Unreads, Favorites, and Recency/Alphabetical. It will change the settings for each user every time it is run  |python |Christian Johannsen |
