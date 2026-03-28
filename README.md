# 💳 Customer Retention Intelligence System

An end-to-end machine learning application that predicts customer churn and provides actionable retention strategies through an interactive web interface.

---

## 🚀 Overview

Customer churn is a critical business problem. This project builds a complete ML pipeline to:

* Predict whether a customer is likely to churn
* Estimate churn probability
* Provide business-driven retention strategies
* Deliver predictions through a user-friendly web app

---

## 🧠 Problem Statement

Businesses lose significant revenue when customers leave.
The goal of this project is to:

> Identify high-risk customers early and take preventive actions.

---

## 🛠 Tech Stack

* Python
* Scikit-learn
* Streamlit
* Pandas & NumPy

---

## 📊 Model Development

Two models were developed and compared:

### 🔹 1. XGBoost

* Accuracy: ~87%
* Better recall for churn class (~50%)
* More powerful for tabular data

### 🔹 2. Random Forest (Selected)

* Accuracy: ~86–87%
* Comparable performance to XGBoost
* Stable and easier to deploy
* No system-level dependencies

---

## ⚖️ Why Random Forest over XGBoost?

Although XGBoost showed slightly better performance, Random Forest was chosen due to:

* ⚙️ **Deployment Stability**: XGBoost requires system-level dependencies (OpenMP / libomp), which caused compatibility issues on macOS
* 🚀 **Ease of Integration**: Random Forest works seamlessly across environments
* 📦 **Maintainability**: Fewer external dependencies → easier for real-world deployment
* ⚖️ **Minimal Performance Difference**: Accuracy difference was negligible

> Decision was made based on **engineering practicality, not just model accuracy**.

---

## 📈 Model Performance

| Metric          | Value      |
| --------------- | ---------- |
| Accuracy        | ~86–87%    |
| Churn Precision | ~0.75      |
| Churn Recall    | ~0.47–0.50 |
| F1 Score        | ~0.58–0.60 |

⚠️ Observation:

* Model performs well overall
* Recall for churn class is moderate → future improvement area

---
## ⚠️ Model Files

The trained model (`.pkl`) is not included in this repository due to:

* GitHub file size limitations (25MB)
* Best practices for maintaining lightweight repositories
* Industry standard of storing models separately from code

To reproduce the model:

* Train the model using the provided pipeline
* Or integrate your own trained model into the application


## 💡 Features

* 🔍 Predict churn probability
* ⚠️ Identify high-risk customers
* 📊 Display probability scores
* 💡 Suggest retention strategies:

  * Senior benefits
  * Premium services
  * Engagement campaigns
  * Discounts & loyalty rewards

---

## 🖥️ Application

Built using Streamlit:

* Clean UI
* Interactive inputs
* Real-time predictions

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
customer-retention-intelligence-system/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
```

---

## 🚧 Future Improvements

* Improve churn recall using class balancing (SMOTE)
* Hyperparameter tuning
* Add model explainability (SHAP / feature importance UI)
* Deploy on cloud (Streamlit Cloud / Render)

---

## 🧠 Key Learning

This project highlights an important real-world lesson:

> The best model is not always the most complex one —
> it is the one that is reliable, deployable, and maintainable.

---

## 📌 Conclusion

This project demonstrates:

* End-to-end ML workflow
* Model comparison & decision-making
* Deployment-focused thinking
* Real-world problem solving

---

## 🚀 Author

Built with focus on practical machine learning and deployment-ready systems.
