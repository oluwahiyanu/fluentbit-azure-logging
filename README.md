# 📦 Fluent Bit Logging Pipeline to Azure Monitor

This project sets up a containerized logging pipeline using **Fluent Bit** to collect logs from a **Node.js** application and ship them to **Azure Monitor (Log Analytics Workspace)**. It demonstrates modern observability practices with **Docker**, **Azure**, and **Bash scripting**.

---

## 📌 Features

- ✅ Real-time log collection from a Dockerized app
- 🔁 Centralized log forwarding to Azure Monitor
- 📊 Query logs in Azure Portal using **Kusto Query Language (KQL)**
- 🐳 Fully Dockerized for local development & deployment
- 💡 Fluent Bit config for parsing structured app logs

---

## 🔧 Tech Stack

- **Node.js** – sample log-emitting app  
- **Fluent Bit** – log collector & forwarder  
- **Azure Log Analytics** – centralized log sink  
- **Docker & Docker Compose** – container orchestration  
- **Bash scripting** – for automation/setup  

---

## 📁 Project Structure

.
├── app/
│ ├── index.js
│ ├── Dockerfile
│ └── package.json
├── fluent-bit/
│ ├── fluent-bit.conf
│ └── parsers.conf
├── docker-compose.yml
└── README.md

---

## 🚀 How It Works

1. The Node.js app writes logs to `stdout` in structured JSON.
2. Fluent Bit reads Docker container logs using the `docker` input plugin.
3. Logs are parsed and forwarded to Azure Monitor using the `azure` output plugin.
4. Logs become visible in your Azure Log Analytics workspace.

---

## 🛠 Setup Steps

### ✅ Step 1: Create Azure Resources

- Go to [Azure Portal](https://portal.azure.com)
- Create a **Log Analytics Workspace**
- Copy these from the workspace:
  - **Workspace ID**
  - **Primary Key**

---

### ✅ Step 2: Configure Fluent Bit

In `fluent-bit/fluent-bit.conf`, replace the placeholders:

```ini
[OUTPUT]
    Name            azure
    Match           *
    Customer_ID     YOUR_WORKSPACE_ID
    Shared_Key      YOUR_PRIMARY_KEY
    Log_Type        AppLog
✅ Step 3: Start the Pipeline
docker-compose up --build
Your app will start logging, and Fluent Bit will ship logs to Azure.

✅ Step 4: View Logs in Azure
Go to Azure Portal > Log Analytics Workspace

Click Logs

Run this query:

kusto
AppLog_CL
| sort by TimeGenerated desc

💼 Real-World Applications
👨‍💻 Portfolio-ready DevOps project

📈 Useful for centralized log analysis in production

☁️ Shows Azure integration & observability pipeline setup

🙌 Author
Oluwahiyanu Akinlalu
GitHub: @oluwahiyanu
