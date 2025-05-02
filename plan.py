from elasticsearch import Elasticsearch
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from getpass import getpass


class SimpleWorkoutKnowledge:
    def __init__(self, es_client, index_name):
        self.es = es_client
        self.index_name = index_name

    def load(self):
        pass

    def query(self, query_text):
        query_body = {
            "_source": ["workout_type", "start_time", "distance_km"],
            "query": {
                "match_all": {}
            },
            "size": 500
        }
        results = self.es.search(index=self.index_name, body=query_body)
        return [hit["_source"] for hit in results["hits"]["hits"]]
    

es = Elasticsearch(
    getpass("Host: "),
    api_key=getpass("API Key: "),
)


agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description="Personal Running Coach",
    instructions=[
        "Review the user's past running workouts.",
        "Create a running plan based on past distances and frequency.",
        "If there are gaps or missed days, add easier re-entry runs.",
    ],
    knowledge=SimpleWorkoutKnowledge(es, index_name="apple-health-workouts"),
    markdown=True
)

recent_workouts = agent.knowledge.query("recent workouts")

workouts_text = "\n".join([
    f"Workout on {w['start_time']}: {w['distance_km']} km ({w['workout_type']})"
    for w in recent_workouts
])

final_prompt = (
    f"Here are my recent workouts:\n\n{workouts_text}\n\n"
    "Based on this, create a personalized 4-week running plan for me to run faster."
)

run_response = agent.run(final_prompt, stream=True)
full_text = "".join([chunk.content for chunk in run_response])

with open("running_plan.md", "w") as f:
    f.write(full_text)