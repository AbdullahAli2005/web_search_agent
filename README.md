# 🌐 Web Search Agent

A simple **AI-powered Web Search Agent** built with **LangChain** and **Tavily Search API**. This project demonstrates how to integrate an LLM with an external search tool to answer real-world queries directly from the web.

---

## 🚀 Features

* Uses **LangChain ReAct Agent** to handle reasoning and actions.
* Integrates with **Tavily Search API** for live web search results.
* Runs inside a **virtual environment (venv)** for dependency isolation.
* API keys are securely stored in a **.env file**.

---

## 📂 Project Structure

```
web_search_agent/
│── .env                  # Stores API keys
│── requirements.txt      # Python dependencies
│── web_agent.py          # Main agent script
│── README.md             # Project documentation
```

---

## 🔑 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/web_search_agent.git
cd web_search_agent
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate   # On Windows
source .venv/bin/activate  # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a **.env** file in the root directory:

```env
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

> ⚠️ **Note**: API keys are required. You can get them by signing up on [Tavily](https://app.tavily.com/) and [OpenAI](https://platform.openai.com/).

### 5. Run the Agent

```bash
python web_agent.py
```

---

## 🧪 Example Usage

After running, you can input queries like:

```
>>> What is the latest news about artificial intelligence?
```

The agent will:

1. Think about the query.
2. Use Tavily Search.
3. Return an AI-generated summary.

---

## 📦 Requirements

* Python 3.8+
* LangChain
* Tavily Search API
* OpenAI API
* python-dotenv

---

## ⚡ Troubleshooting

* **Missing API keys** → Check `.env` file.
* **Import errors** → Run `pip install -r requirements.txt` again.
* **Virtual environment issues** → Ensure `.venv` is activated before running scripts.

---

## 📜 License

This project is open-source and free to use under the MIT License.
