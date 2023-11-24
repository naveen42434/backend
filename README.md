## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/naveen42434/backend.git
    ```
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Environment Variables:

    - **Linux/Mac:**

        ```bash
        export AZURE_SUBSCRIPTION_KEY=your_azure_subscription_id
        export AZURE_REGION=your_region
        export AZURE_RESOURCE_GROUP=your_resource_group
        ```

    - **Windows:**

        ```bash
        $env:AZURE_SUBSCRIPTION_ID=your_azure_subscription_id
        $env:AZURE_REGION=your_region
        $env:AZURE_RESOURCE_GROUP=your_resource_group
        ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload --workers 4 --port 1234
    ```

2. Open the API documentation in your browser:

    [http://127.0.0.1:1234/docs](http://127.0.0.1:1234/docs)


3. **Health Check:**

    Test the health of the application:

    ```bash
    curl --location 'http://127.0.0.1:1234/healthcheck'
    ```

4. **Create Speech Service:**

    Create a new Azure Speech Service:

    ```bash
    curl --location 'http://127.0.0.1:1234/create_speech_service/' \
    --form 'speech_service_name="your_service_name"'
    ```

5. **Transcribe Audio:**

    Test the `/transcribe/` endpoint by uploading an audio file:

    ```bash
    curl --location 'http://127.0.0.1:1234/transcribe/' \
    --header 'accept: application/json' \
    --form 'file=@"./path/to/your/audio/file/"'
    ```
   
6. **Convert Text to Speech:**

    Test the `/synthesize/` endpoint by uploading a Text, PDF, or DOCX file:

    ```bash
    curl --location 'http://127.0.0.1:1234/synthesize' \
    --form 'file=@path/to/your/file.pdf"' \
    --form 'rate="150"'
    ```
   
## Important Note

- Before using the `/transcribe/` endpoint, ensure that you have created a Speech Service using the `/create_speech_service/` endpoint. The Speech Service is required for transcribing audio files.

    ```bash
    curl --location 'http://127.0.0.1:1234/create_speech_service/' \
    --form 'speech_service_name="your_service_name"'
    ```

    After creating the Speech Service, you can use the `/transcribe/` endpoint to transcribe audio files.


- If you want to run the `/transcribe/` endpoint directly without creating a Speech Service through the API, you need to provide the Speech Resource Key using the following command:

    ```bash
    $env:AZURE_SUBSCRIPTION_KEY=your_speech_resource_key
    ```

    Make sure to replace `your_speech_resource_key` with the actual key.