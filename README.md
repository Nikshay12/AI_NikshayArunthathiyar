# AI-Powered Knowledge Graph to Manim Animation Automation

## Overview
This project automates educational video creation:
Book text → Knowledge Graph → AI Script Generator → Slide Formatter → Manim Animation → Video Output

## Steps to Run
1. Install dependencies: `pip install --user fastapi uvicorn neo4j python-dotenv jinja2 spacy`  
2. Run backend: `python3 -m uvicorn backend.app.main:app --reload`  
3. Run KG ingestion: `python3 kg/ingestion/ingest.py`  

> Manim scripts are included as placeholders; running them requires additional system libraries.
