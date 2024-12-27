import os
import io
import base64
import wave
import openai
from io import BytesIO
from pydub import AudioSegment
from pytubefix import YouTube
import numpy as np
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

openai.api_key = key

def convert_audio_to_pcm_base64(audio_data, sample_rate, num_channels=1, sample_width=2):
    # Normalize float audio data to int16 if needed
    if audio_data.dtype in (np.float32, np.float64):
        audio_data = np.clip(audio_data, -1.0, 1.0)  # Cap float data
        audio_data = (audio_data * 32767).astype(np.int16)
    
    # Convert audio to WAV and encode in Base64
    with io.BytesIO() as wav_buffer:
        with wave.open(wav_buffer, 'wb') as wav_file:
            wav_file.setnchannels(num_channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(audio_data.tobytes())
        wav_base64 = base64.b64encode(wav_buffer.getvalue()).decode('utf-8')
    
    return wav_base64

def wav_to_numpy(audio_bytes):
    audio_seg = AudioSegment.from_file(BytesIO(audio_bytes), format="wav")
    samples = np.array(audio_seg.get_array_of_samples())
    if audio_seg.channels > 1:
        samples = samples.reshape((-1, audio_seg.channels))
    return audio_seg.frame_rate, samples

def extract_mp3(url):
    stream = YouTube(url).streams.get_audio_only()
    audio = BytesIO()
    stream.stream_to_buffer(audio)
    audio.seek(0)
    wav = BytesIO()
    AudioSegment.from_file(audio).export(wav, format='wav')
    return base64.b64encode(wav.getvalue()).decode('utf-8')

def realtime_response(systext, text, audio_data, voice):
    content = []
    history_response = []
    history_response.append({"role": "system", "content": [
        {
            "type": "text",
            "text": systext
        }
    ]})


    if audio_data:
        try:
            pcm_base64 = extract_mp3(audio_data)
            content.append({"type": "input_audio", "input_audio": {"data": pcm_base64, "format": "wav"}})
        except:
            sample_rate, audio_np = audio_data

            pcm_base64 = convert_audio_to_pcm_base64(audio_np, sample_rate)
            content.append({"type": "input_audio", "input_audio": {"data": pcm_base64, "format": "wav"}})

    if text:
        content.append({"type": "text", "text": text})

    history_response.append({"role": "user", "content": content})

    print(history_response)

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini-audio-preview-2024-12-17",
            modalities=["text", "audio"],
            audio={"voice": voice, "format": "wav"},
            messages=history_response
        )

        transcript = response.choices[0].message.audio.transcript
        
        try:
            wav_bytes = base64.b64decode(response.choices[0].message.audio.data)

            # audio_id = response.choices[0].message.audio.id

            pcm_base64 = wav_to_numpy(wav_bytes)

            return transcript, pcm_base64
        except:
            return transcript, None

    except Exception as e:
        print(f"Error during communication: {e}")
        return None, None

