# Grabcut Tutorial

This repo is the code supporting the Meetup talk "Foreground Extraction with GrabCut".

It aims at presenting different ways to extract exterior contours in an image with
 the following characteristics:
- one main object on a united background
- the object of interest is always at the same place on the image
- not many data available

This tutorial is a notebook, with the following image used to try out different
techniques:

![Example Cat Image](./images/white_cat_on_white_background.jpeg)

## Installation

- Clone the repo
- Create a virtualenv and activate it:
```
virtualenv -p python3 venv
source venv/bin/activate
```
- Install the requirements:
```
pip install requirements.txt
```

You can now run the `grabcut_notebook.py` notebook to start extracting cat contours!

## Try it out with another image

To try out the code with another image, drop your image of interest in the `images/` 
folder and replace the image name in the first cell of the notebook.
