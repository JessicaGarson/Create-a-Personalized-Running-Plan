# Create a personalized running plan with Elasticsearch and Agno

This repository contains a simple code sample, creating a four-week plan to run a faster 5k. The example uses Elasticsearch to store your fitness data and [Ango](https://github.com/agno-agi/agno) to generate a fitness plan.  

## Prerequsites

- The version of Python that is used is Python 3.12.1 but you can use any version of Python higher than 3.9.
- This demo uses Elasticsearch version 8.18, but you can use any version of Elasticsearch that is higher than 8.0.
- Install the required packages:

    ```
    pip install elasticsearch agno
    ```
- You will want to configure an environment variable for your OpenAI API Key, which you can find on the API keys page in [OpenAI's developer portal](https://platform.openai.com/api-keys).

    On Mac: 

    ```
    export OPENAI_API_KEY="your_api_key"
    ```

    
    On Windows:

    ```
    setx OPENAI_API_KEY "your_api_key"
    ```

## Step 1: Get your data

## Step 2: Getting your data into Elasticsearch

## Step 3: Generating your running plan

