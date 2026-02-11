# Automatic Handwritten Answer Sheet Evaluation System using Deep Learning

> **Final Year Major Project**
> *AI-Assisted Evaluation | Ethical AI | Explainable Grading*

---

## 1. Abstract
In the traditional education system, manual evaluation of handwritten answer sheets is time-consuming, prone to human fatigue, and potentially inconsistent. This project presents an **AI-Assisted Evaluation System** that automates the preliminary grading of descriptive handwritten answers. By leveraging Optical Character Recognition (OCR) and Transformer-based Deep Learning models, the system assesses answers based on semantic meaning rather than mere keyword matching. It provides a page-wise detailed analysis, similarity scores, and explainable insights, assisting educators in grading more efficiently while maintaining transparency.

## 2. Problem Statement
Manual grading of thousands of handwritten scripts often leads to:
- **Inconsistency:** Different markers may grade differently.
- **Latency:** Results take weeks or months to declare.
- **Fatigue:** Human evaluators may miss key points after hours of grading.

**Objectives:**
- To convert handwritten answer sheets (PDF) into digital text.
- To compare student answers semantically with a model answer key.
- To provide a transparent, explainable scoring mechanism.
- To highlight "Low Confidence" evaluations for mandatory human review.

## 3. System Architecture
The system follows a modular client-server architecture:

1.  **Frontend (React.js):**
    - Takes PDF upload from the user.
    - Accepts the "Model Answer" text.
    - Displays detailed analytics (Marks, Similarity, Missing Concepts).

2.  **Backend (FastAPI & Python):**
    - **PDF Processor:** Splits the PDF into individual page images.
    - **OCR Module (Tesseract):** Extracts handwritten text from images.
    - **Semantic Grader (Sentence-BERT):** Converts text into high-dimensional vectors and verifies cosine similarity.
    - **Response Generator:** Aggregates marks and flags low-confidence pages.

## 4. Technologies Used
- **Frontend:** React.js, Tailwind CSS, Axios, Vite.
- **Backend:** Python 3.9+, FastAPI, Uvicorn.
- **AI/ML:**
    - **OCR:** Tesseract-OCR (Google).
    - **NLP:** Sentence Transformers (`all-MiniLM-L6-v2`).
    - **Libraries:** PyTorch, Scikit-learn, NumPy, PDF2Image, Pillow.

## 5. Key Features
- **Page-wise Evaluation:** Each page is processed independently for granular grading.
- **Semantic Understanding:** Grades based on meaning, not just exact words.
- **Explainable AI (XAI):** Shows "Missing Concepts" and match percentages.
- **Confidence Flagging:** Automatically flags ambiguous handwriting/answers for human verification.
- **Ethical Design:** Explicitly labeled as an *assistant* tool, not a replacement for teachers.

## 6. How to Run the Project

### Prerequisites
1.  **Python 3.9+** installed.
2.  **Node.js 16+** installed.
3.  **Tesseract OCR** installed on your system.
    - Windows: Download installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
    - Add Tesseract to your System PATH.
4.  **Poppler** (for PDF conversion) installed and added to PATH.

### Steps
1.  **Backend Setup:**
    ```bash
    cd backend
    python -m venv venv
    # Activate venv: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux)
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    *Note: The first run will download the AI model (~80MB).*

2.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

3.  **Usage:**
    - Open `http://localhost:3000`.
    - Upload a PDF file containing handwritten answers.
    - Paste a Model Answer in the text box.
    - Click "Evaluate".

## 7. Limitations & Constraints
- **Handwriting Legibility:** Extremely messy handwriting may result in poor OCR accuracy.
- **Language Support:** Currently optimized for English script only.
- **Diagrams:** The system evaluates *text* only; diagrams/graphs are not currently graded.
- **Human Oversight:** This tool is designed to *assist* teachers, not replace them. Final verification is recommended.

## 8. Future Enhancements
- Fine-tuning OCR (CNN-LSTM) on specific handwriting datasets.
- Adding specific support for mathematical equations and diagram grading.
- User authentication and database integration for storing student records.
