import gradio as gr
from modules.get_openai_response import realtime_response
from modules.get_openai_response import realtime_chatresponse

with gr.Blocks(theme=gr.themes.Soft(), title="GPT-4o-audio-preview") as demo:
    gr.Markdown(f"<h1 style='text-align: center; display:block'>{'GPT-4o-audio-preview'}</h1>")

    # Audio Gen Tab
    with gr.Tab("Audio"):
        gr.Markdown(f"<p>{'Create Text-To-Speech or Speech-To-Speech'}</p>")

        with gr.Row():

            prompt = gr.Text(
                label="System Prompt",
                value="",
                interactive=True,
                render=False
            )

            audio = gr.Audio(
                label = "Audio Input",
                type="numpy",
                render = False
            )

            voice_dropdown = gr.Dropdown(
                ["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
                label = "Voice",
                value = "alloy",
                render = False
            )

        chat = gr.Interface(
            fn = realtime_response,
            inputs = [prompt, gr.Text(label="Input Prompts", value="Respond with audio."), audio],
            additional_inputs = [voice_dropdown],
            outputs=[gr.Text(label="Output Text"), gr.Audio(label="Output Audio", autoplay=True, format="wav", type="numpy")],
            flagging_mode="never"
        )

    # Audio Gen Tab
    with gr.Tab("YouTube"):
        gr.Markdown(f"<p>{'Summarize a YouTube Video'}</p>")

        with gr.Row():

            audio = gr.Text(
                label = "YouTube Link",
                value="https://www.youtube.com/watch?v=yJrDOlncFzI",
                render = False
            )

            voice_dropdown = gr.Dropdown(
                ["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
                label = "Voice",
                value = "alloy",
                render = False
            )

        chat = gr.Interface(
            fn = realtime_response,
            inputs = [gr.Text(label="Input Prompt", value="Review this clip and try to make your own original version of it."), audio],
            additional_inputs = [voice_dropdown],
            outputs=[gr.Text(label="Output Text"), gr.Audio(label="Output Audio", autoplay=True, format="wav", type="numpy")],
            flagging_mode="never"
        )

    # Chat Window Tab
    with gr.Tab("Chat"):
        gr.Markdown(f"<p>{'Chat window with the AI'}</p>")

        with gr.Row():

            prompt = gr.Text(
                label="System Prompt",
                value="",
                interactive=True,
                render=False
            )

            audio = gr.Audio(
                label = "Audio Input",
                type="numpy",
                render = False
            )

            voice_dropdown = gr.Dropdown(
                ["alloy", "echo", "fable", "onyx", "nova", "shimmer"],
                label = "Voice",
                value = "alloy",
                render = False
            )

        chat = gr.Interface(
            fn = realtime_chatresponse,
            inputs = [prompt, gr.Text(label="Input Prompts", value="Respond with audio."), audio],
            additional_inputs = [voice_dropdown],
            outputs=[gr.Text(label="Chat Window"), gr.Audio(label="Output Audio", autoplay=True, format="wav", type="numpy")],
            flagging_mode="never",
        )

if __name__ == "__main__":
    demo.queue()
    # # Toggle this on if you want to share your app, change the username and password
    # demo.launch(server_port=7862, share=True, auth=("admin", "password"))

    # Toggle this on if you want to only run local
    demo.launch()

