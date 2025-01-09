# 📊 **AI Finance Agent: Analyst Recommendations & Financial News Fetcher**

![AI Agent Image](https://github.com/itsritzz/AI_Finance_agent/blob/main/Images/Autonomous-AI-Agents-for-Finance.png)

## 🚀 **Introduction**

This project implements an **AI Finance Agent** designed to fetch **analyst recommendations** and deliver **up-to-date financial news** using [Phidata Framework](https://docs.phidata.com/introduction). By leveraging **Groq's AI models**, **YFinanceTools**, and **GoogleSearch**, this application serves as a powerful tool for financial analysis and information retrieval. Could be used for any stocks data.

The system is modular, robust, and built to streamline financial data extraction, ensuring accurate insights and reliable updates.

---

## 📚 **Table of Contents**

- [🚀 Introduction](#-introduction)  
- [🛠️ Features](#--features)  
- [🏗️ Architecture](#architecture)  
- [🛠️ Tools and Technologies](#-tools-and-technologies)  
- [📦 Installation](#-installation)  
- [📝 License](#-license)  
- [🙌 Credits](#-credits)  
- [📲 Contact](#-contact)  

---

## 🛠️ **Features**

- ✅ **Web Data Retrieval:** Fetch real-time financial updates using `GoogleSearch`.  
- ✅ **Analyst Recommendations:** Retrieve key analyst insights via `YFinanceTools`.  
- ✅ **Structured Data Presentation:** Display results in clean and readable tables.  
- ✅ **Scalable Agent Team:** A collaborative agent architecture (`Agent Team`) combines insights from multiple agents.  
- ✅ **Dynamic Financial Summaries:** Generate clear, concise summaries with source URLs for transparency.  

---

## 🏗️ **Architecture**

The system employs a modular architecture with distinct roles for each agent:

### **1️⃣ Web Agent (GoogleSearch)**  
- Fetches relevant financial news.  
- Provides credible source URLs for transparency.  

### **2️⃣ Finance Agent (YFinanceTools)**  
- Retrieves stock prices, analyst recommendations, and company-specific insights.  
- Displays results in structured tables.  

### **3️⃣ Agent Team (Coordinator)**  
- Combines outputs from both agents into a unified response.  
- Ensures consistency and accuracy in the final summary.  

```plaintext
📦 AI Finance Agent  
├── 🤖 Web Agent (GoogleSearch)  
│   ├── Fetches live financial news  
│   ├── Includes source URLs  
│  
├── 💼 Finance Agent (YFinanceTools)  
│   ├── Fetches stock prices  
│   ├── Displays data in tables  
│  
└── 🧠 Agent Team  
    ├── Integrates agent outputs  
    ├── Delivers consolidated summaries ```plaintext
```

## 🛠️ **Tools and Technologies**

### ✅ **Programming Language**
- **Python:** Used for scripting, data handling, and agent orchestration.

### ✅ **Frameworks and Libraries**
- **Phidata:** Framework for creating AI agents and workflows.  

### ✅ **AI Models**
- **Groq LLaMA3 (70B):** Language model for generating insights and responses.

### ✅ **Agent Tools**
- **YFinanceTools:** Financial data retrieval (stock prices, analyst recommendations).  
- **GoogleSearch:** Real-time financial news from the web.

### ✅ **Environment Management**
- **Virtual Environment (venv):** Dependency isolation.  
- **Environment Variables (.env):** Secure API key management.

### ✅ **Data Sources**
- **Yahoo Finance API:** Real-time stock and financial data.  
- **Google Search API:** Fetch credible news updates.

### ✅ **Deployment**
- **Local Server (Python HTTP Server)**  
- **Cloud Hosting (Optional):**  
   - **GitHub Pages**  
   - **Vercel**  
   - **Netlify**  

## 📦 **Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-github-username/ai-finance-agent.git
cd ai-finance-agent
```
### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
.\env\Scripts\activate   # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
### **4️⃣ Set Environment Variables**
Create a .env file in the root folder:
```bash
GROQ_API_KEY=your_groq_api_key
```

## **License**

This project is licensed under the MIT License.

## **Credits**

- **Phidata Team:** For the framework and comprehensive documentation. [Phidata Documentation](https://docs.phidata.com/introduction)
- **Groq AI Models:** For superfast inference processing. [Groqcloud](https://console.groq.com/playground)
- **YFinanceTools:** For reliable financial data APIs.

## **Contact**

- **Author:** Ritesh Kumar Singh
- **Portfolio:** [itsritz.my.canva.site](https://itsritz.my.canva.site)
- **LinkedIn:** [Ritesh Kumar Singh](https://www.linkedin.com/in/ritesh001/)
- **GitHub:** [itsritzz](https://github.com/itsritzz)

---

2025 © Developed by Ritesh Kumar Singh. All rights reserved.
