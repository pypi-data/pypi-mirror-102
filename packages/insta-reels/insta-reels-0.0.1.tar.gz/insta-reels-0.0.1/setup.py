from  setuptools import setup
setup(name="insta-reels",
version="0.0.1",description="This can download instagram reels",author="@tanay_mishra",packages=['reels-downloader'],
author_email="tanaymishra2204@gmail.com",install_requires=['requests-HTML','requests'],
long_description="""This module can download Instagram reels video 
to download import download function from module and call with parameters 
like that download('link','videos/video.mp4')..
"""
)