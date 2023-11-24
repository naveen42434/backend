import time

from fastapi import APIRouter, Query
from app.core.config import settings
import subprocess
import json

router = APIRouter()

def create_speech_service(speech_service_name: str):
    subscription_id = settings.AZURE_SUBSCRIPTION_ID
    resource_group = settings.AZURE_RESOURCE_GROUP
    azure_region = settings.AZURE_REGION

    create_command = f"az cognitiveservices account create --name {speech_service_name} --resource-group {resource_group} --kind SpeechServices --sku S0 --location {azure_region} --subscription {subscription_id}"

    try:
        subprocess.run(create_command, shell=True, check=True)
        get_keys_command = f"az cognitiveservices account keys list --name {speech_service_name} --resource-group {resource_group} --subscription {subscription_id}"
        result = subprocess.run(get_keys_command, shell=True, capture_output=True, text=True, check=True)
        keys_info = json.loads(result.stdout)
        key1 = keys_info['key1']
        settings.AZURE_SUBSCRIPTION_KEY = key1
        time.sleep(300)

        if settings.AZURE_SUBSCRIPTION_KEY:
            return {"status": "Speech service created successfully"}
        else:
            return {"status": "Error setting subscription key", "error_message": "Subscription key not set correctly"}

    except subprocess.CalledProcessError as e:
        return {"status": "Error executing command", "error_message": str(e)}
    except json.JSONDecodeError as e:
        return {"status": "Error decoding JSON", "error_message": str(e)}


@router.post("/")
async def create_speech_service_endpoint(speech_service_name: str = Query(...)):
    return create_speech_service(speech_service_name)