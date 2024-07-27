# Anime Downloader Script

This Python script automates the process of downloading all episodes of an anime series. By providing the script with the link to the main page of the anime, it:

1. Scrapes the main page to identify and extract links to individual episodes.
2. Sequentially downloads each episode to a specified directory.
3. Handles potential interruptions and resumes downloads if needed.


## Features
Automatic scraping of episode links from the main page.
Sequential download of episodes.
Resumption of interrupted downloads.


## Requirements
Python 3.x
beautifulsoup4 for web scraping
requests for handling HTTP requests
youtube_dl or yt_dlp for downloading media content


## Installation

1. Clone the repository:
``` bash
git clone https://github.com/yourusername/anime-downloader.git
cd anime-downloader
```

2. Install the required packages:
``` bash
pip install -r requirements.txt
```

3. Usage
Update the config.py file with the main page link of the anime and the desired download directory.
Run the script:
``` bash
python downloader.py
```


## Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
