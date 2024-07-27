# Anime Downloader Script

This Python script automates the process of downloading all episodes of an anime series. It is for WINDOWS, but it can be easly adpted for linux as well, it need to be changed the chromedriver used by selenium.

1. Scrapes the main page to identify and extract links to individual episodes.
2. Sequentially downloads each episode to a specified directory.
3. Handles potential interruptions and resumes downloads if needed.


## Features
Automatic scraping of episode links from the main page.
Sequential download of episodes.
Resumption of interrupted downloads.


## Requirements
"Read the requirments.txt file"


## Installation

1. Clone the repository:
``` bash
git clone git clone https://github.com/rick0101/anime_bot_unity.git
cd anime_bot_unity
```

2. Install the required packages (ONE LINE PER COMMAND):
``` bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

3. Usage
Run the script:
``` bash
python anime_scraping_unity.py
```

## WARNING

If it does stop working try to download the newer version of chromedriver based on your OS.
Link to chromedriver: https://googlechromelabs.github.io/chrome-for-testing/
Go to Stable, and from line 6 to line 10, you have the links for downloading chromedriver based on you OS.


## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
