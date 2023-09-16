# PyFileFlow

A python project/script to upload, download and list files from services such as Dropbox.

## Description

This Python script allows users to easily transfer files between their local system and cloud storage services like Dropbox. It uses the Inquirer library for collecting inputs via the command line interface (CLI) to keep things simple.

## Installation

### Windows

1.  Create a virtual environment:  
    `py -m venv venv`
2.  Activate the virtual environment:  
    `venv\Scripts\activate`
3.  Install dependencies from requirements.txt:  
    `pip install -r requirements.txt`

### macOS

1.  Create a virtual environment:  
    `python3 -m venv venv`
2.  Activate the virtual environment:  
   ` source venv/bin/activate`
3.  Install dependencies from requirements.txt:  
    `pip install -r requirements.txt`

### Linux

1.  Create a virtual environment:  
    `python3 -m venv venv`
2.  Activate the virtual environment:  
    `source venv/bin/activate`
3.  Install dependencies from requirements.txt:  
   ` pip install -r requirements.txt`

Currently, only code for Dropbox integration has been implemented.


## Configuration

To use PyFileFlow with Dropbox, follow these steps:

1. Create a `.env` file in the root of your project.

2. Add the following environment variables to the `.env` file:\
	`DROPBOX_APP_KEY=your_app_key`\
	`DROPBOX_APP_SECRET=your_app_secret`\
	`DROPBOX_ACCESS_TOKEN=your_access_token`
	




