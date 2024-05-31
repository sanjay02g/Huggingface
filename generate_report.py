import requests
import json
import time
import os

# hugging model url
model_hub_url = os.environ['HUGGING_FACE_MODEL_HUB']
report_interval = int(os.environ['REPORT_INTERVAL'])
# number of top models
top_models = int(os.environ['TOP_MODELS'])
# fetch data from hugging model
def fetch_model_data():
    response = requests.get(model_hub_url + '/models')
    return json.loads(response.text)

# Function to generate the report
def generate_report():
    model_data = fetch_model_data()
    sorted_models = sorted(model_data, key=lambda x: x['downloads'], reverse=True)[:top_models]
    report = '\n'.join([f"{model['name']}: {model['downloads']}" for model in sorted_models])
    print(report)

# Main function
if __name__ == "__main__":
    while True:
        generate_report()
        time.sleep(report_interval)
    exit()
