# Jaga Mental - Machine Learning Prediction API 🧠

This repository contains the FastAPI server that handles machine learning predictions for the **Jaga Mental** project. This server is designed to provide mood analysis and emotional state predictions based on user input. It works alongside a mobile application to deliver personalized feedback and recommendations for mental health improvement.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview 📖

**Jaga Mental** is a mental health application aimed at helping Gen Z in Indonesia track and improve their mental well-being. This FastAPI server powers the machine learning prediction functionality, enabling the analysis of user moods based on journaling entries.

## Features ✨

- **Predict User Emotions:** Use a trained TensorFlow model to predict emotions from text input.
- **FastAPI Framework:** High-performance and easy-to-use backend framework.
- **Integration Ready:** Designed to integrate seamlessly with the Jaga Mental mobile application.

## Tech Stack 🛠️

- **Backend Framework:** FastAPI
- **Machine Learning:** TensorFlow
- **Language:** Python 3.11+
- **Deployment:** Google Cloud Platform (GCP)

## Getting Started  🚀

### Prerequisites 📋

- Python 3.11 or later
- `pip` (Python package manager)

### Installation 💾

1. Clone the repository:

   ```bash
   git clone https://github.com/Jaga-Mental-Dev/backend-python.git
   cd backend-python
   ```
3. Create environment variable
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Create .env

   ```.env
   PORT=
   GROQ_API_KEY=
   ```

5. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Server ▶️

Start the FastAPI :

 ```bash
  python run.py
 ```

## API Endpoints 🔗

### Get Emotion from Image

**Endpoint:**  
`POST /image/api/imageclassification/`

**Description:**  
Predicts the user's emotion based on an uploaded image.

**Request Format:**  
- **Content-Type:** `multipart/form-data`
- **Body:**
  - `file`: (required) The image file to analyze.

**Example Request:**  
```bash
curl -X POST http://0.0.0.0:8080/image/api/imageclassification/ \
-F "file=@FAlling in reverse.jpg"
```

**Example Response**

```json
{
    "filename": "FAlling in reverse.jpg",
    "result": {
        "label": "sedih",
        "probability": 0.5948500633239746
    }
}
```

### Get Emotion from text

**Endpoint**
`POST /text/api/emotion/`

**Description**
Predicts the user's emotion based on a text input.

**Request Format:**  
- **Content-Type:** `multipart/form-data`
- **Body:**
  - `text`: (required) The text input for emotion analysis.

**Example Requext**

```bash
curl -X POST http://0.0.0.0:8080/text/api/emotion/ \
-F "text=Aku Sedih Banget huhu T-T"
```

**Example Response**

```json
{
    "text": "Aku sedih banget huhu T-T",
    "label": "sedih"
}
```

### Get Feedback

**Endpoint**
`POST /text/api/feedback/`

**Description**
Provides feedback based on the user's emotional state and text input.

**Request Format:**  
- **Content-Type:** `multipart/form-data`
- **Body:**
  - `text`: (required) The text input for emotion analysis.

**Example Requext**

```bash
curl -X POST http://127.0.0.1:8000/text/api/feedback/ \
-F "emotion=sedih" \
-F "text=Aku sedih banget Huhuhuh T-T."
```

**Example Response**

```json
{
    "text": "Aku sedih banget Huhuhuh T-T",
    "feedback": "\"Aku di sini untukmu, sedih banget pasti sangat berat untukmu. Kamu tidak sendirian, aku ada di sini untuk mendengarkan dan menemanimu. Jangan ragu untuk berbagi apa yang sedang kamu rasakan, aku siap mendengarkan dengan hati terbuka.\""
}
```

## Contributing 🤝
Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.

## License 📜
Proyek ini menggunakan lisensi MIT. Silakan lihat [LICENSE](./LICENSE) untuk informasi lebih lanjut.

