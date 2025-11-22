 # AI Text Summarizer – SummarIQ

A full-stack web application that summarizes any text using AI. Built with **React**, **FastAPI**, and deployed online using **Vercel** and **Render**.

---

## Features

- Summarizes text efficiently using the **Groq Llama-3.1-8b-instant** AI model.
- Dark/Light mode toggle for better user experience.
- Loading indicators while summarization is in progress.
- Clear input and output with a single click.
- Fully deployed: backend on **Render**, frontend on **Vercel**.

---

## Tech Stack

- **Frontend:** React, Vite, CSS  
- **Backend:** FastAPI, Groq API  
- **Deployment:** Vercel (frontend), Render (backend)

---

## Getting Started

### Prerequisites

- Node.js
- Python 3.10+
- Git

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
export GROQ_API_KEY=your_api_key   # or use .env file
uvicorn main:app --reload
