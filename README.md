# 🏢 Real Estate Smart Predictor

This project is a user-friendly web application built with **Streamlit** that predicts real estate property prices based on user-defined parameters. It leverages a **Random Forest Regressor** and includes modular code design with logging and error handling.

---

## 🚀 Features

- 🔍 Predict property price based on interactive form inputs
- 🧠 Machine learning model: Random Forest Regressor
- 🧼 Data preprocessing with encoding and feature engineering
- 📦 Modular Python codebase
- 📋 Real-time logging with file-based logs
- ☁️ Easily deployable to Streamlit Cloud

---

## ⚙️ How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/Ken-Jacob/Real-Estate-App.git
cd Real-Estate-App
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run app.py
```

---

## 🏗️ Input Features

| Feature         | Description                          |
|----------------|--------------------------------------|
| Bedrooms        | Number of bedrooms                   |
| Bathrooms       | Number of bathrooms                  |
| Square Ft.      | Total square footage                 |
| Year Built      | Year the property was constructed    |
| Year Sold       | Year the property was sold           |
| Lot Size        | Lot size in acres                    |
| Basement        | Presence of a basement (Yes/No)      |
| Popular Area    | Is the location considered popular?  |
| Recession       | Was it sold during a recession?      |
| Property Type   | Bungalow / Condo / Other             |

---

## 📈 Model Details

- **Algorithm**: Random Forest Regressor
- **Training/Test Split**: 80/20
- **Target Variable**: `price`
- **Feature Engineering**: `property_age`, one-hot encoding for categorical features

---

## 🪵 Logs

Logs are saved to `logs/app.log` and include runtime info, warnings, and errors for debugging purposes.

---

## ☁️ Deployment

You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) by pushing this project to a public GitHub repository and linking it through the Streamlit dashboard.

---

## 🧑‍💻 Author

**Ken Biju Jacob**  
Business Intelligence System Infrastructure  
Algonquin College 

---

## 📄 License

This project is licensed for academic use.
