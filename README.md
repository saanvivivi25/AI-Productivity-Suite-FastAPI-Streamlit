# AI Productivity Suite using FastAPI & Streamlit

## Overview

The AI Productivity Suite is a full-stack AI-powered web application built using **FastAPI** for the backend and **Streamlit** for the frontend. The application integrates Google's Gemini AI to automate various productivity tasks through REST APIs and an interactive web interface.

The project demonstrates a clean FastAPI architecture with routers, services, models, dependency injection, logging, exception handling, configuration management using `.env`, and SQLite database integration.

---

## Features

- AI Resume Screening
- AI Feedback Analyzer
- AI Meeting Notes Generator
- AI Email Generator
- AI Text Summarizer
- Dashboard with Analytics
- Search History
- Delete Individual History
- Delete All History
- Export Reports
- SQLite Database Integration
- FastAPI REST APIs
- Streamlit Web Interface
- Logging
- Exception Handling
- Dependency Injection
- Environment Variable Configuration

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini API
- SQLite
- Pandas
- Pydantic
- Pydantic Settings
- Requests
- Python-docx
- OpenPyXL
- Uvicorn
- Python-dotenv

---

## Project Structure

```
AI-Productivity-Suite/
│
├── app.py                  # Streamlit Frontend
├── main.py                 # FastAPI Backend
├── .env                    # Environment Variables
├── requirements.txt
├── history.db
├── README.md
```

---

## FastAPI Concepts Implemented

- FastAPI Project Structure
- REST APIs
- POST APIs
- GET APIs
- DELETE APIs
- Dependency Injection
- Configuration using .env
- Logging
- Exception Handling
- Pydantic Models
- Business Service Layer
- SQLite Database Integration

---

## Streamlit Features

- Interactive Dashboard
- Text Input Forms
- File Upload
- API Integration using Requests
- Report Download
- History Management
- Search Functionality
- Responsive User Interface

---

## API Endpoints

### Resume Screening

- POST `/resume/analyze`
- POST `/resume/analyze-bulk`

### Feedback Analyzer

- POST `/feedback/analyze`
- POST `/feedback/analyze-bulk`

### Meeting Notes Generator

- POST `/meeting-notes/generate`

### Email Generator

- POST `/email/generate`

### Text Summarizer

- POST `/summarize`

### History

- GET `/history`
- GET `/history/export`
- DELETE `/history/{id}`
- DELETE `/history`

### Dashboard

- GET `/dashboard`

---



Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
DATABASE_PATH=history.db
```

---

## Running the Backend

```bash
python -m uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
python -m streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

## Workflow

1. User enters data in the Streamlit application.
2. Streamlit sends HTTP requests to FastAPI using the Requests library.
3. FastAPI validates the input using Pydantic models.
4. Business logic is processed through the Service layer.
5. Gemini AI generates the response.
6. Results are stored in the SQLite database.
7. FastAPI returns the response as JSON.
8. Streamlit displays the output to the user.

---

## Database

SQLite stores:

- Module Name
- User Input
- AI Output
- Additional Information
- Timestamp

---

## Learning Outcomes

- FastAPI Project Structure
- API Development
- POST, GET and DELETE APIs
- Dependency Injection
- Environment Configuration
- Exception Handling
- Logging
- Service Layer Architecture
- Streamlit Frontend Development
- SQLite Database Operations
- AI Integration using Gemini API
- REST API Communication
- File Handling
- Report Generation

---

