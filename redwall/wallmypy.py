#!c:/Python/python.exe
import ctypes
import tkinter
import random
import os
import urllib.request

#imports for scrapy to be called
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def wallpaperCrawl():
    #create process for crawler with wallpaper bot settings
    process = CrawlerProcess(get_project_settings())
    # 'wallpaper' is the name of one of the spiders bot.
    process.crawl('wallpaper')
    process.start() # the script will block here until the crawling is finished


def changeWallpaper():
    SPI_SETDESKWALLPAPER = 20
    #random to test different wallpapers
    wallpaper = random.choice(os.listdir(os.getcwd() + "\\paper\\full"))
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.getcwd() + "\\paper\\full\\" + wallpaper , 0)

#GUI
gui = tkinter.Tk()
# Code to add widgets will go here...
#change title of GUI
gui.title('Scrapy Wallpaper Changer')
#create button to change Wallpaper
chgPaperButton = tkinter.Button(gui, text ="Change Wallpaper", command = changeWallpaper)
#create button to change send spider to get wallpapers
getPaperButton = tkinter.Button(gui, text ="Fetch Wallpapers", command = wallpaperCrawl)
#pack and run GUI
chgPaperButton.pack()
getPaperButton.pack()
gui.mainloop()
