#Import All the Required Libraries
import os

from utils import read_video, save_video
from utils.track_narrative import load_tracks_stub, tracks_to_timeline
from trackers import Tracker

INPUT_VIDEO = "input_videos/video.mp4"
OUTPUT_VIDEO = "output_videos/output.mp4"
STUB_PATH = "tracker_stubs/player_detection.pkl"


def _align_tracks_to_video(tracks, num_video_frames):
    m = min(num_video_frames, len(tracks["players"]))
    if m != len(tracks["players"]) or m != num_video_frames:
        print(
            f"Note: aligning timeline ({len(tracks['players'])} stub frames) "
            f"to video ({num_video_frames} frames); using {m}."
        )
    return {
        "players": tracks["players"][:m],
        "referees": tracks["referees"][:m],
        "ball": tracks["ball"][:m],
    }


def _run_gemini_on_frames(api_key, video_frames, tracks):
    from insights import analyze_clip

    if tracks is not None:
        tracks = _align_tracks_to_video(tracks, len(video_frames))
        timeline = tracks_to_timeline(tracks, video_frames[0].shape, fps=30.0)
    else:
        timeline = (
            "No track stub found. Still frames are from the annotated output video "
            "(on-screen player/referee/ball markings if present)."
        )
    n = len(video_frames)
    sample_idx = sorted({0, n // 2, max(0, n - 1)})
    key_frames = [video_frames[i] for i in sample_idx]
    insight = analyze_clip(timeline, key_frames, api_key=api_key)
    insight_path = "output_videos/gemini_insight.txt"
    with open(insight_path, "w", encoding="utf-8") as f:
        f.write(insight)
    print(f"\n--- Gemini insight (saved {insight_path}) ---\n{insight}\n")


def main():
    api_key = ""

    if api_key and os.path.isfile(OUTPUT_VIDEO):
        print(f"{OUTPUT_VIDEO} found — skipping tracking; running Gemini only.")
        video_frames = read_video(OUTPUT_VIDEO)
        tracks = None
        if os.path.isfile(STUB_PATH):
            tracks = load_tracks_stub(STUB_PATH)
        else:
            print(f"No {STUB_PATH}; insight will be vision-only (no count timeline).")
        _run_gemini_on_frames(api_key, video_frames, tracks)
        return

    video_frames = read_video(INPUT_VIDEO)

    tracker = Tracker("models/best.pt")
    tracks = tracker.get_object_tracks(
        video_frames, read_from_stub=False, stub_path=STUB_PATH
    )

    output_video_frames = tracker.draw_annotations(video_frames, tracks)
    save_video(output_video_frames, OUTPUT_VIDEO)

    if api_key:
        _run_gemini_on_frames(api_key, output_video_frames, tracks)


if __name__ == "__main__":
    main()