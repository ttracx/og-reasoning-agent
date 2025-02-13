# 🛢️ OG Reasoning Agent

🚀 **OG Reasoning Agent** is an AI-powered reasoning system for the **oil and gas industry**, integrating **LLMs, structured reasoning (Mind Maps), vector search (Pinecone), and real-time engineering calculations** to assist professionals in drilling, wellbore stability, and regulatory compliance.

---

## 🌍 **Project Overview**
This repository implements **Agentic Reasoning** for oil and gas applications by:
- 🧠 **Mind Map Agent** → Structuring knowledge using a **graph-based reasoning memory**.
- 🔍 **Retrieval Agent (RAG)** → Querying **Pinecone** for drilling manuals, reports, and API standards.
- 📊 **Computation Agent** → Performing **real-time calculations** for mud weight, well control, and casing design.
- 🤖 **LLM Agent** → Using **DeepSeek R1 / OpenAI** for expert-level explanations.

---

## 📂 **Project Structure**
```
og-reasoning-agent/
│── backend/
│   ├── main.py                # FastAPI entry point
│   ├── agents/
│   │   ├── mind_map.py        # Knowledge graph agent
│   │   ├── retrieval.py       # Web & document retrieval agent
│   │   ├── computation.py     # Engineering calculations agent
│   ├── models/
│   │   ├── embedding.py       # Pinecone vector search
│   │   ├── llm.py             # LLM agent with DeepSeek R1
│   ├── utils/
│   │   ├── config.py          # API keys and settings
│   │   ├── logger.py          # Logging setup
│   ├── requirements.txt       # Python dependencies
│── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/
│   │   ├── App.js             # React UI
│   ├── package.json           # Frontend dependencies
│── data/
│   ├── oil_gas_docs/          # Sample documents
│   ├── embeddings/            # Vectorized knowledge base
│── README.md                  # Documentation
│── .gitignore                  # Ignore unnecessary files
│── docker-compose.yml          # Deployment setup
│── Dockerfile                  # Containerization
```

---

## ⚡ **Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ttracx/og-reasoning-agent.git
cd og-reasoning-agent
```

### **2️⃣ Set Up Backend**
Install dependencies:
```bash
pip install -r backend/requirements.txt
```
Run FastAPI server:
```bash
uvicorn backend.main:app --reload
```

### **3️⃣ Set Up Frontend**
Navigate to frontend and install:
```bash
cd frontend
npm install
npm start
```

---

## 🛠 **Features**
### ✅ **AI-Powered Reasoning**
- Uses **DeepSeek R1** for stepwise reasoning and logical deduction.
- Implements **Mind Maps** to structure reasoning context.

### ✅ **Retrieval-Augmented Generation (RAG)**
- Searches **Pinecone Vector DB** for oil and gas drilling documents.
- Integrates **API standards, well logs, and real-time knowledge**.

### ✅ **Engineering Calculations**
- Computes **mud weight, pore pressure, casing design** using **SymPy**.
- Supports **Python-based real-time calculations**.

### ✅ **Multi-Agent Collaboration**
- **Mind Map Agent** → Structures logical reasoning.
- **Retrieval Agent** → Queries documents and API standards.
- **Computation Agent** → Executes real-time well calculations.

---

## 🔧 **API Endpoints**
### 🚀 **Query AI Model**
**Endpoint:** `POST /query/`  
**Request:**
```json
{
  "question": "What’s the recommended mud weight for a well at 12,000 ft TVD with a pore pressure of 0.48 psi/ft?"
}
```
**Response:**
```json
{
  "answer": "Recommended Mud Weight: 7.69 ppg"
}
```

---

## 🌍 **Deployment**
### **1️⃣ Docker Setup**
Build and run containers:
```bash
docker-compose up --build
```

### **2️⃣ Environment Variables (`.env`)**
Create a `.env` file and add:
```
PINECONE_API_KEY=your_pinecone_key
OPENAI_API_KEY=your_openai_key
```

---

## 📚 **References**
- **DeepSeek R1**: [https://deepseek.com](https://deepseek.com)
- **Pinecone Vector DB**: [https://www.pinecone.io](https://www.pinecone.io)
- **Oil & Gas Industry Standards**: [https://www.api.org](https://www.api.org)

---

## 🚀 **Contributing**
1. Fork the repository.
2. Create a new branch (`feature/my-new-feature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/my-new-feature`).
5. Open a **Pull Request**.

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 💡 **Future Enhancements**
✅ **Hybrid Retrieval (Vector + Keyword Search)**  
✅ **Multi-Agent Collaboration**  
🔲 **Support for Real-Time Drilling Data Feeds**  
🔲 **AI-Driven Regulatory Compliance Audits**  

---

