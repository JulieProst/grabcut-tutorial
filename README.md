# Grabcut Tutorial

This repo is the code supporting the Meetup talk "Foreground Extraction with GrabCut".

It aims at presenting different ways to extract exterior contours in an image with
 the following characteristics:
- one main object on a united background
- the object of interest is always at the same place on the image
- not many data available

By following this notebook tutorial, you'll see how to segment the input spoon image
 as follows: 

![Example Cat Image](./doc/sample_segmentation.png)

## Installation

- Clone the repo
- Create a virtualenv and activate it. You can use [pyenv](https://github.com/pyenv/pyenv) to manage different Python 
versions and create a virtual environment: 
```bash
pyenv install 3.8.2
pyenv virtualenv 3.8.2 <ENV_NAME>
cd <WORKIND_DIR>
pyenv local <ENV_NAME>
```

- Install the requirements:
```
pip install -r requirements.txt
```

You can now run the `grabcut_notebook.py` notebook to start extracting cat contours!

## Try it out with another image

To try out the code with another image, drop your image of interest in the `images/` 
folder and replace the image name in the first cell of the notebook.
