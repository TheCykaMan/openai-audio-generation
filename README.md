# GPT-4o Audio Preview Application

This project is a web application leveraging Gradio 5 and OpenAI's API to generate text-to-speech or speech-to-speech responses and interact with YouTube videos. This application acts as an interface for generating audio responses using OpenAI's GPT-4o model with audio capabilities.

## Features

- **Audio Tab**: Convert text prompts to speech or transform input audio using selected voice tones.
- **YouTube Tab**: Summarize YouTube videos and optionally recreate the video's audio content with your own unique version.

## Requirements

Ensure you have Python 3.7 or higher installed. 

## Quick Start with `startup.bat`

To simplify the installation and startup process on Windows, use the `startup.bat` script. This script will handle the creation of a virtual environment, install the necessary dependencies, and start the application for you.

### Steps:

1. **Download the Repository:**

    Navigate to the directory where you want this project to reside. Clone or download the repository files.

2. **Configure Environment:**

    Ensure you have a `.env` file in the root of your project with the following content:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

    Replace `your_openai_api_key_here` with your actual OpenAI API key.

3. **Run `startup.bat`:**

    Locate the `startup.bat` file in your project directory. Double-click the file or execute it through the command line:

    ```bash
    startup.bat
    ```

    This script performs the following:
    - Checks if a virtual environment exists. If not, it creates one.
    - Activates the virtual environment.
    - Installs the required Python packages from the `requirements.txt`.
    - Launches the Gradio application.

4. **Access the Application:**

    Once the script executes successfully, the application will launch, usually accessible at `http://localhost:7862`.

## Manual Setup and Execution

If you prefer manual setup:

1. **Manual Environment Setup:**

    - Install all dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application:**

    Use the following command to start the Gradio application:

    ```bash
    python main.py
    ```

    Alternatively, you can continue using the `startup.bat` as described.

## Usage

### Audio Tab

1. **Input Prompt**: Enter the text prompt you wish to convert into speech.
2. **Audio Input**: Optionally upload an audio file for speech-to-speech transformation.
3. **Select Voice**: Choose a voice tone from options like Alloy, Echo, Fable, etc.
4. **Output**: The application will display the transcribed text and generate corresponding audio.

### YouTube Tab

1. **Enter YouTube Link**: Provide the URL of a YouTube video to summarize.
2. **Select Voice**: Choose a voice tone.
3. **Output**: The application summarizes the video, providing both text and audio output.

## Code Explanation

### `main.py`

This script sets up the UI using Gradio, defining inputs and outputs for both the &quot;Audio&quot; and &quot;YouTube&quot; tabs. It uses a custom component `realtime_response` from `get_openai_response.py` to generate responses.

### `get_openai_response.py`

Key Functions:
- **`convert_audio_to_pcm_base64`**: Converts numpy audio data to base64-encoded PCM WAV format.
- **`wav_to_numpy`**: Converts WAV audio bytes to a numpy array.
- **`extract_mp3`**: Downloads audio from a YouTube link and converts it to a base64-encoded WAV format.
- **`realtime_response`**: Communicates with OpenAI's API to generate text and audio responses based on inputs.

## Troubleshooting

- Ensure your API key is correctly set in the `.env` file.
- Verify all dependencies are installed.
- Check that the correct ports are open and accessible if running the app over a network.

## Contribution

Feel free to fork the repository and submit pull requests. Any contributions to improve functionality or add new features are welcome!
