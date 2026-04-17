import os

import cv2
from PIL import Image


def analyze_clip(
    timeline_text,
    key_frames_bgr,
    *,
    api_key=None,
    model_name="gemini-3-flash-preview",
):
    """
    Send a text timeline plus a few BGR (OpenCV) frames to Gemini and return narrative text.
    Requires: pip install google-generativeai
    API key: pass api_key=... or set environment variable GEMINI_API_KEY.
    """
    try:
        import google.generativeai as genai
    except ImportError as e:
        raise ImportError(
            "Install the Gemini SDK: python -m pip install google-generativeai"
        ) from e

    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        raise ValueError(
            "Missing Gemini API key. Set GEMINI_API_KEY or pass api_key=..."
        )

    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_name)

    images = []
    for arr in key_frames_bgr:
        rgb = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
        images.append(Image.fromarray(rgb))

    prompt = """You are a football (soccer) analyst assistant.

You are given:
1) A timeline built from an object-detection + tracking pipeline (counts of players, referees, ball visibility and rough ball position in the frame). These numbers are noisy — occlusion, motion blur, and model errors cause flicker.
2) A few still images sampled from the same clip (beginning, middle, end).

Tasks:
- Summarize what likely happens in the clip in plain language (possession hints, crowded zones, transitions) while separating facts visible in the stills from guesses from the timeline.
- Call out where you are uncertain.
- Ignore "two balls" style contradictions in the timeline unless clearly visible in images — treat those as detector noise unless images support it.

Use short sections: Summary, What the stills show, Timeline interpretation, Uncertainties.

Timeline:
"""
    prompt = prompt + "\n" + timeline_text

    response = model.generate_content([prompt, *images])
    if not response.parts:
        raise RuntimeError(
            getattr(response, "prompt_feedback", None) or "Empty response from Gemini"
        )
    return response.text
