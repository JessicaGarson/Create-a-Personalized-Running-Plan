# Create a personalized running plan with Elasticsearch and Agno

This repository contains a simple code sample, creating a four-week plan to run a faster 5k. The example uses Elasticsearch to store your fitness data and [Ango](https://github.com/agno-agi/agno) to generate a fitness plan. To monitor your progress, you can send your plan to Notion.

## Prerequsites

- The version of Python that is used is Python 3.12.1 but you can use any version of Python higher than 3.9.
- This demo uses Elasticsearch version 8.18, but you can use any version of Elasticsearch that is higher than 8.0.
- Install the required packages:

    ```
    pip install elasticsearch agno notion-client
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

- You will also need to clone this repository: 

    ```
    git clone https://github.com/JessicaGarson/Create-a-Personalized-Running-Plan.git
    cd Create-a-Personalized-Running-Plan
    ```

## Step 1: Get your data

### Apple Health data
This example uses an XML file that contains Apple Health data. You can obtain an XML file using the method described [in this article](https://support.apple.com/guide/iphone/share-your-health-data-iph5ede58c3d/ios).

### Andriod and Samsung health data
Similar data is available for [Android devices](https://developer.android.com/health-and-fitness/guides/health-connect) and [Samsung devices](https://developer.samsung.com/health/blog/en/accessing-samsung-health-data-through-health-connect), but additional processing may be needed here.

### Sample data
You can also find a sample data set in this repository as [sample_data.xml](sample_data.xml).


## Step 2: Getting your data into Elasticsearch
After you've obtained your dataset, you can run the Jupyter notebook [parse_data.ipynb](parse_data.ipynb).

## Step 3: Generating your running plan
You can generate a markdown file that contains a 4-week running plan by running the following command:

```
python plan.py
```

## Step 4: Sending your running plan to Notion
You can use the Jupyter notebook [Notion.ipynb](notion.ipynb) to send your running plan to Notion for activity tracking based on your plan. To learn more about working with the Notion API, be sure to check out their [documentation on the subject](https://developers.notion.com/reference/intro) as well as the [Python library](https://pypi.org/project/notion-client/) used in this example.