# Gistyfy - AI Text Summarizer
[![Vercel](https://img.shields.io/badge/Frontend-Vercel-blue)](https://vercel.com)
[![Render](https://img.shields.io/badge/Backend-Render-green)](https://render.com)

SummarIQ is a web application that uses AI to summarize long texts into concise, readable summaries. It's perfect for quickly understanding articles, documents, or notes. The project combines a **React** frontend with a **FastAPI** backend powered by **Groq AI API**.

---

## Features

- Summarize any text quickly
- Dark/Light mode toggle for comfortable reading
- Responsive and modern UI
- Easy deployment on **Render** (backend) and **Vercel** (frontend)

---

## Demo

- **Backend:** [https://gistify-new.onrender.com](https://gistify-new.onrender.com)  
- **Frontend:** [https://gistify.vercel.app](https://gistify.vercel.app)

---

## Tech Stack

- **Frontend:** React, Vite, CSS  
- **Backend:** Python, FastAPI, Groq AI API  
- **Deployment:** Render (backend), Vercel (frontend)

---

## Backend Setup

1. Clone the repository and navigate to the backend folder:

```bash
git clone https://github.com/RivoKhara/SummerIQ.git
cd SummerIQ/backend
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the backend folder and add your Groq API key:

ini
Copy code
GROQ_API_KEY=your_api_key_here
Run the FastAPI server:

bash
Copy code
uvicorn main:app --reload
Open the server in your browser:

text
Copy code
http://127.0.0.1:8000
Frontend Setup
Navigate to the frontend folder:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
Update the API URL in App.jsx if needed:

javascript
Copy code
const res = await fetch("https://gistify-new.onrender.com", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text }),
});
Start the frontend development server:

bash
Copy code
npm run dev
Open the local URL displayed in the terminal (usually http://localhost:5173).

