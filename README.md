# AI-Powered Deepfake Detection System

This project is a deep learning and image processing-based solution to detect AI-generated deepfakes in images and videos. With the increasing misuse of generative AI, such as spreading misinformation, identity theft, and fraud, it has become essential to develop reliable tools to identify manipulated media.

This system integrates a web interface with a backend deepfake detection engine to provide a user-friendly platform for users to test media files and receive visual analysis.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contact](#contact)

---

## Overview

The system leverages AI models to analyze images or videos and determine whether the media is genuine or synthetically altered. It uses frame analysis and facial behavior inconsistencies, among other indicators, to detect deepfakes.

This repository contains:
- A web front-end (`index.html`, `how_it_works.html`, etc.)
- Backend logic (`app.py`) for handling detection
- Custom styling (`styles.css`) for clean UI
  
---
## Features

- Deepfake detection using AI-based classification
- Web interface for uploading media and viewing results
- Detection history tracking
- User feedback submission
- Informational pages on deepfakes and system methodology

---

## Tech Stack

**Frontend:**
- HTML5
- CSS3
- Bootstrap (optional)
  
**Backend:**
- Python 3
- Flask (for web server)
- OpenCV
- TensorFlow / PyTorch (for detection model)

---

## Project Structure

├── app.py # Flask backend handling detection logic
├── index.html # Main landing page
├── how_it_works.html # Explanation of deepfake detection process
├── history.html # Shows previously analyzed media
├── feedback.html # User feedback form
├── styles.css # Styling for all HTML pages
├── static/ # (Optional) Images, uploads, models
├── templates/ # (Optional) Flask template directory
└── README.md # Project documentation

## Installation

1. Clone the repository:
git clone https://github.com/shubh-2601s/Ai-powered-deepfake-detection-system.git
cd Ai-powered-deepfake-detection-system

2. Install dependencies:
pip install -r requirements.txt

3.Run the Flask app:
python app.py

4.Open a browser and visit:
http://127.0.0.1:5000/

Usage
* Upload an image or video from the main interface.
* The system will process the media and display whether it is likely real or fake.
* Users can navigate to:
* How it Works to understand the detection logic
* History to see past results
* Feedback to share their thoughts

Future Improvements:
* Improve model accuracy using additional datasets (e.g., DFDC, Celeb-DF)
* Add support for video streaming (real-time detection)
* Display heatmaps to show manipulated areas
* user authentication for profile-based history
* Deploy on cloud platforms (e.g., Heroku, AWS)

License
This project is open-source and available under the MIT License.

Contact
Author: Shubham
Email: 10221shubham.s@gmail.com
GitHub: github.com/shubh-2601s



