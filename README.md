# Watson AI Emotion Detector

This project is a web application that utilizes IBM Watson AI (via the Watson Emotion service) to perform emotion detection in text. The application is built with Flask and exposes a simple API endpoint that accepts a text input and returns the detected emotion scores along with the dominant emotion.

## Features

- **Emotion Analysis:** Sends user-provided text to Watson Emotion API and retrieves emotion statistics.
- **Error Handling:** Manages blank or invalid text inputs and returns appropriate error messages.
- **Web Interface:** Simple Flask-based server that renders an HTML page and provides an API endpoint for emotion detection.
- **Testing:** Unit tests are provided to verify the functionality of the emotion detection function.

## Project Structure
```
├── EmotionDetection
│   ├── emotion_detection.py
│   ├── __init__.py
│   └── __pycache__
│       ├── emotion_detection.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── LICENSE
├── __pycache__
│   └── emotion_detection.cpython-310.pyc
├── README.md
├── server.py
├── static
│   └── mywebscript.js
├── templates
│   └── index.html
├── test_emotion_detection.py
└── venv
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── Activate.ps1
    │   ├── flask
    │   ├── get_gprof
    │   ├── get_objgraph
    │   ├── isort
    │   ├── isort-identify-imports
    │   ├── normalizer
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.10
    │   ├── pylint
    │   ├── pylint-config
    │   ├── pyreverse
    │   ├── python -> python3
    │   ├── python3 -> /usr/bin/python3
    │   ├── python3.10 -> python3
    │   ├── symilar
    │   └── undill
    ├── include
    ├── lib
    │   └── python3.10
    │       └── site-packages
    ├── lib64 -> lib
    └── pyvenv.cfg
```  

## License

This project is licensed under the terms of the Apache License. Big shoutout to ibm-developer-skills-network/oaqjp-final-project-emb-ai from which the project was originally forked from!

## Acknowledgements

This project was built as a part of an assignment to demonstrate the integration of Watson AI for emotion detection within a Flask web application.

## Summarization

This README.md file summarizes the project, its structure, and usage instructions, and includes the required screenshots and testing guidelines as specified by the assignment.
