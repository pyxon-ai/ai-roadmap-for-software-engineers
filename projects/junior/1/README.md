# Junior — Project 1: Applied ML & NLP (classic portfolio)

## Inspiration

This mirrors the **“get your hands dirty”** phase many developers follow when moving into AI: small **supervised learning** projects before LLMs—like building a **movie recommender**, **image classifier (CNN)**, or **sentiment analysis** on text—then **shipping a live demo** (e.g. **Streamlit**) so recruiters can click and run it.

## Goal

Show that you can **train or fine-tune a model**, **evaluate** it sensibly, and **deploy** a simple UI—not only call APIs.

## Pick one core build (or combine lightly)

| Direction | Example | Skills you show |
|-----------|---------|-----------------|
| **Recommendation** | Collaborative filtering on a public dataset (e.g. MovieLens, Kaggle) | Tabular ML, metrics, cold-start trade-offs |
| **Vision** | Image classification with a **CNN** on CIFAR-10 or similar | PyTorch/TF, train/val split, overfitting awareness |
| **NLP** | **Sentiment** or topic classification using **Hugging Face** transformers on tweets or reviews | Tokenization, metrics, small-scale fine-tuning |

## Requirements

- **Python** stack you can defend: NumPy/Pandas, scikit-learn and/or **PyTorch** (or TensorFlow if you prefer—say why).  
- **Evaluation:** not only accuracy—mention at least one of: precision/recall, confusion matrix, or baseline comparison.  
- **Deploy:** **Streamlit** (or similar) with a **public demo link** or clear local run + screenshots.  
- **`prompts/`** per [submission rules](../../README.md#2-prompts-folder-required).

## Honest scope

You do **not** need PhD-level math—focus on **clear decisions** (why this model, how you split data, what you’d monitor in production). Interviewers often ask **bias–variance**, **tabular vs deep nets**, **imbalanced data**—note any of that you considered in the README.

## PR checklist

- [ ] One primary ML/NLP task with a trained or fine-tuned model  
- [ ] Evaluation section in README (metrics + short interpretation)  
- [ ] Streamlit (or equivalent) demo + **demo link** or run instructions  
- [ ] `README.md` + `prompts/`  
- [ ] State in PR: **Junior — Project 1**
