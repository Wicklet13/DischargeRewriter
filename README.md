
# 🏥 DischargeRewriter

**DischargeRewriter** is a Streamlit-based web application that uses  LLMs via Groq 
to convert complex hospital discharge instructions into plain, easy-to-understand language.

**Hosted at:** https://discharge-summary.streamlit.app/

---

## 🚀 Project Goals

- Simplify real-world discharge summaries using an LLM.
- Provide a clean, readable web interface for healthcare users.
- Estimate word count and reading level of rewritten text.

---

## 🛠️ Technologies Used

- **Streamlit** – for building the web interface.
- **Groq** – for fast LLM API requests when local performance is limited.
- **Python** – core backend logic.
- **Hugging Face synthetic notes** – as a data source for test cases.

---

## 📁 Folder Structure

```
DischargeRewriter/
├── main.py           # Model generation and handling
├── stream.py         # Application user interface
├── refine.py         # Factor test data
├── data.csv          # Raw test data
├── refined.csv       # Refined test data
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
```

---

## ⚙️ How to Run Locally

1. **Clone the repo**

   ```bash
   git clone https://github.com/Wicklet13/DischargeRewriter.git
   cd DischargeRewriter
   ```

2. **Set up a virtual environment (optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the app**

   ```bash
   streamlit run stream.py
   ```

---

## 📊 Features

- 🔄 Rewrites complex discharge instructions in plain English.
- ✂️ Keeps all sentences short and simple.
- 📏 Calculates word count and grade level.
- 🌐 Clean, friendly web UI with customizable settings.
- 🔒 Local processing using Ollama and Groq.

---

## 🙋‍♀️ Project By

**Prateek Kalusani**  
Mentor: Dr. Neelima  

This project was developed as part of a research initiative to explore language models 
in patient education and accessibility.
