from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

def get_vit_synthesizer(path: str = "/Users/jt-lab/opt/anaconda3/envs/redenv/lib/python3.10/site-packages/TTS/.models.json"):
    """Get a synthesizer for the VIT model."""

    model_manager = ModelManager(path)
    model_path, config_path, model_item = model_manager.download_model("tts_models/en/vctk/vits")


    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
    )

    return syn

def gen_and_save_audio(syn: Synthesizer ,text: str, output_path: str, speaker_name: str = "p243"):
    """Generate audio from text using the VIT model and saves the audio to the output path."""

    # this will only work for the VIT model
    # other models may not need the speaker_name argument
    outputs = syn.tts(text, speaker_name=speaker_name)
    syn.save_wav(outputs, output_path)

def print_models():
    path = "/Users/jt-lab/opt/anaconda3/envs/redenv/lib/python3.10/site-packages/TTS/.models.json"

    model_manager = ModelManager(path)
    model_manager.list_models()