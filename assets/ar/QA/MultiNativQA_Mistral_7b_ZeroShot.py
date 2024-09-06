import json

from llmebench.datasets import MultiNativQADataset
from llmebench.models import AzureModel
from llmebench.tasks import MultiNativQATask


def metadata():
    return {
        "author": "Arabic Language Technologies, QCRI, HBKU",
        "model": "Mistral 7b",
        "description": "Deployed on Azure.",
        "scores": {},
    }


def config():
    return {
        "dataset": MultiNativQADataset,
        "task": MultiNativQATask,
        "model": AzureModel,
    }


def prompt(input_sample):

    # Define the question prompt
    # Provide your response in the following JSON format and provide JSON output only. No additional text.
    question_prompt = f"""
    Please use your expertise to answer the following Arabic question. Answer in Arabic and rate your confidence level from 1 to 10.
    Provide your response in the following JSON format: {{"answer": "your answer", "score": your confidence score}}.
    Please provide JSON output only. No additional text. Answer should be limited to less or equal to {input_sample['length']} words.

    Question: {input_sample['question']}
    """

    # Define the assistant prompt
    assistant_prompt = """
    You are an Arabic AI assistant specialized in providing detailed and accurate answers across various fields.
    Your task is to deliver clear, concise, and relevant information. 
    """

    return [
        {
            "role": "user",
            "content": question_prompt,
        },
        # {
        #     "role": "assistant",
        #     "content": assistant_prompt,
        # },
    ]


def post_process(response):
    data = response["output"]
    if "\n\n" in data:
        data = data.split("\n\n")[0]
    response = json.loads(data)
    answer = response["answer"]
    return answer
