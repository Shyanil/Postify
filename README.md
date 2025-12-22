# Postify 🚀
🚀 **Live Testing Link:**  - https://postify-app.streamlit.app/


Postify is an AI-powered tool designed to generate engaging social media posts. Leveraging Large Language Models (LLMs) and few-shot learning techniques, it helps users create high-quality content tailored to their specific style and needs.

## 📂 Project Structure

Here's an overview of the key files in the repository:

- **`main.py`**: The entry point of the application (likely the Streamlit dashboard).
- **`llm_helper.py`**: Handles interactions with the Large Language Model (e.g., OpenAI, Groq, Llama).
- **`post_generator.py`**: Contains the core logic for generating post content based on inputs.
- **`few_short.py`**: Implements "few-shot" prompting to provide the LLM with examples for better context and style matching.
- **`preprocess.py`**: Utility script for cleaning and formatting input data.
- **`data/`**: Directory containing dataset files or example inputs.
- **`requirements.txt`**: List of Python dependencies required to run the project.

## ✨ Features

- **AI Content Generation**: Automatically generate posts for platforms like LinkedIn, Twitter, or Instagram.
- **Few-Shot Learning**: Uses examples to understand and mimic a specific writing style.
- **Customizable Topics**: Generate content based on user-selected tags, topics, and length.
- **Easy-to-Use Interface**: Simple interaction to generate results quickly.

## 🛠️ Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/Shyanil/Postify.git](https://github.com/Shyanil/Postify.git)
cd Postify
