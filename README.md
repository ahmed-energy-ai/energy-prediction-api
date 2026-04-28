\# ⚡ Energy Consumption Prediction API



This project is a Machine Learning-based API that predicts energy consumption (kWh) based on temperature and time.



\---



\## 📌 Overview



Predict electricity usage using:



\* Temperature 🌡️

\* Hour ⏰



\---



\## 🚀 API



\### Endpoint:



POST /predict



\### Example Request:



{

"temperature": 35,

"hour": 14

}



\### Example Response:



{

"predicted\_kwh": 120.29

}



\---



\## 🛠️ Tech Stack



\* Python

\* FastAPI

\* Scikit-learn



\---



\## ▶️ Run



pip install fastapi uvicorn scikit-learn



uvicorn app:app --reload



\---



\## 👨‍💻 Author



Ahmed Samy



