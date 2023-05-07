import asyncio
import aiohttp
from codetiming import Timer
from lib2to3.pgen2 import driver
from time import sleep, time
import html
from urllib import response
from h11 import Response
import scrapy
from selenium import webdriver
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import TextResponse
from multiprocessing import Pool


async def task(name, work_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    async with aiohttp.ClientSession() as session:

        while not work_queue.empty():
            url = await work_queue.get()
            driver = webdriver.Chrome("D:\Project\scarpy-selenium\chromedriver.exe")
            driver.get(url)
            print(f"Task {name} getting URL: {url}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()

async def main():
    """
    This is the main entry point for the program
    """
    # Create the queue of work
    #used to store over work load
    work_queue = asyncio.Queue()
    print(work_queue)
    # Put some work in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
    ]:
        # await work_queue.put(url)
        print(await work_queue.put(url))
    # Run the tasks
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        
         #( asyncio.create_task) used to submit the coroutines to run in background
        await asyncio.gather(
            asyncio.create_task(task("One", work_queue)),   
            asyncio.create_task(task("Two", work_queue)),
        )

if __name__ == "__main__":
    asyncio.run(main())
