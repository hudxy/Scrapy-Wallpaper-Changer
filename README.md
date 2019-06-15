# Scrapy-Wallpaper-Changer
Side project to change desktop wallpapers using images scraped from web using python3.7 &amp; scrapy

Uses Scrapy Framework to download high-resolution wallpapers from the internet

socwall file uses spider to download from https://www.socwall.com 
redwall file uses spider to download from https://www.reddit.com/r/wallpaper 


### ONLY WORKS ON WINDOWS OS ###

### To Run ###
1. Download Anaconda3 and run the command to get scrapy and all dependancies: conda install -c conda-forge scrapy 
2. Add the path to Anaconda3 into Windows environment variables PATH
3. From Anaconda Prompt, go to directory were files are stored (inside socwall or redwall)
4. Run command: python wallmypy.py
5. Click Fetch Wallpapers button to run spider and retrieve wallpapers
6. Upon success, wallpapers will be saved into the 'papers/full' directory
7. Click Change Wallpaper button to randomly select one of the downloaded images to be the desktop background
8. Exit the GUI to exit
