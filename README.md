# chatGPT_sentiment_analysis

## Project Overview

This project is a Python-based sentiment analysis tool that allows you to analyze the sentiment of text data using OpenAI's ChatGPT model (engine of choice was "text-davinci-003"). It takes a CSV file as input, processes each text entry in the file, and assigns a sentiment label to each entry (negative, neutral, or positive) in a new column called "sentiment". While the script is initially designed to work seamlessly with CSV files, it can be easily adapted to handle various file formats, granting you the flexibility to use it with the data sources of your preference.

To begin using this script effectively, you will need to provide your own API key from OpenAI. It is important to mention that to avoid exceeding the rate limit usage, a sleeper function has been thoughtfully incorporated into line 92 of the script. The default setting is to wait for 1 second between each API call. This should be modified according to your specific needs and means.

## Features

-   Sentiment analysis of text data: The tool utilizes OpenAI's ChatGPT model to analyze the sentiment of text entries.
-   Customizable sentiment labels: You can define your own sentiment labels to suit your specific use case.
-   Command-line interface: The tool provides a command-line interface for easy interaction and usage with progress bar included.
    Output visualization: The analyzed dataset is saved as a CSV file with an additional column for sentiment labels.

## Customization

Sentiment labels: You can customize the sentiment labels by modifying the sentiment_labels list in the perform_sentiment_analysis function of the sa_script.py file.

## Data

The data used was generated for testing pourposes. For a quick trial, I provide a small file and a big one, both with the respective results of the analysis performed. If you want to run the the scrip yourself, you can use the 'sample.csv' file. 

-   data.csv
-   mini_data.csv
-   sample.csv

## Setup and Dependencies
To run the code in this project, you'll need the following dependencies:

Python (version 3.11.3)
libraries:  pandas, openai, time, ssl, tqdm 

## Acknowledgments

The sentiment analysis tool utilizes OpenAI's ChatGPT model. Special thanks to OpenAI for providing access to their powerful language model.

