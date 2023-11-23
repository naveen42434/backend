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
        export AZURE_SUBSCRIPTION_KEY=your_subscription_key
        export AZURE_REGION=your_region
        ```

    - **Windows:**

        ```bash
        $env:AZURE_SUBSCRIPTION_KEY=your_subscription_key
        $env:AZURE_REGION=your_region
        ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload --workers 4 --port 1234
    ```

2. Open the API documentation in your browser:

    [http://127.0.0.1:1234/docs](http://127.0.0.1:1234/docs)


3. Test the `/transcribe/` endpoint by uploading an audio file:
    ```bash
    curl --location 'http://127.0.0.1:1234/transcribe/' \
    --header 'accept: application/json' \
    --form 'file=@"./path/to/your/audio/file/"'
    ```