"""Turn per-frame tracks into compact text for LLM / analyst prompts."""

import pickle


def load_tracks_stub(path):
    with open(path, "rb") as f:
        return pickle.load(f)


def _ball_region(tracks, frame_idx, width, height):
    ball_frame = tracks["ball"][frame_idx]
    if not ball_frame:
        return "not detected"
    for _tid, info in ball_frame.items():
        bbox = info["bbox"]
        cx = ((bbox[0] + bbox[2]) / 2) / width
        cy = ((bbox[1] + bbox[3]) / 2) / height
        return f"visible (x≈{cx:.2f}, y≈{cy:.2f} of frame, 0–1)"
    return "not detected"


def tracks_to_timeline(tracks, frame_shape, fps=30.0, every_n_frames=15):
    """
    Build a sparse timeline: detection counts flicker with the model — the LLM should treat this as noisy signal.
    frame_shape: (H, W, C) from OpenCV frame.
    """
    height, width = frame_shape[0], frame_shape[1]
    n_frames = len(tracks["players"])
    duration = n_frames / fps if fps else 0.0
    lines = [
        f"Frames: {n_frames}, ~{fps} fps, duration ~{duration:.1f}s. Size {width}x{height}.",
        "Notes: counts are from a detector, not ground truth; brief drops may be occlusion or false negatives.",
    ]
    for i in range(0, n_frames, every_n_frames):
        n_players = len(tracks["players"][i])
        n_refs = len(tracks["referees"][i])
        ball = _ball_region(tracks, i, width, height)
        t = i / fps if fps else 0.0
        lines.append(
            f"t={t:.1f}s (f{i}): players={n_players}, referees={n_refs}, ball={ball}"
        )
    return "\n".join(lines)
