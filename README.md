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
- Copy the following values:
  - **Workspace ID**
  - **Primary Key**

---

### ✅ Step 2: Configure Fluent Bit

In `fluent-bit/fluent-bit.conf`, replace the placeholders with your actual values:

```ini
[OUTPUT]
    Name            azure
    Match           *
    Customer_ID     YOUR_WORKSPACE_ID
    Shared_Key      YOUR_PRIMARY_KEY
    Log_Type        AppLog

✅ Step 3: Start the Pipeline
bash
Copy
Edit
docker-compose up --build
This command will:

Start the Node.js app

Start Fluent Bit

Ship container logs to Azure Monitor

✅ Step 4: View Logs in Azure
Go to Azure Portal → Log Analytics Workspace

Click on Logs

Run the following query:

kusto
Copy
Edit
AppLog_CL
| sort by TimeGenerated desc
You should start seeing your app logs in real time!

💼 Real-World Applications
👨‍💻 Portfolio-ready DevOps project — show off your skills with Azure & logging

📈 Centralized log analysis — useful in production-grade systems

☁️ Cloud-native observability — integrates Docker & Azure seamlessly

🙌 Author
Oluwahiyanu Akinlalu
GitHub: @oluwahiyanu
