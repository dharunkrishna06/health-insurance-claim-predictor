# Insurance Claim Estimator | Streamlit App

This repository features an interactive Streamlit application that estimates health insurance claim amounts based on user inputs. Built with Python and scikit-learn, the solution provides a quick and user-friendly way to demonstrate predictive modeling on real-world healthcare data.

---

## 🧠 Project Summary

This project aims to simulate how health insurers assess potential claim amounts based on an individual's demographic and health profile. Users enter values like age, BMI, diabetic status, and smoking habits, and the model returns an estimated claim value. The goal is to assist insurers in pricing, reserve planning, and risk stratification.

---

## 📊 Dataset & Features

The dataset includes:
- **Demographics**: Age, Gender, Region
- **Health Indicators**: BMI, Blood Pressure, Diabetic, Smoker
- **Household**: Number of Children
- **Target**: Insurance claim amount in USD

---

## 🔧 Technical Stack

- **Language**: Python  
- **Frameworks**: Streamlit  
- **Machine Learning**: Linear Regression (sklearn), Pipeline, OneHotEncoder, StandardScaler  
- **Data Handling**: Pandas, Numpy  
- **Model Persistence**: joblib  
- **Visualization**: Streamlit UI components

---

## ⚙️ Model Workflow

1. **Preprocessing**  
   - One-hot encoding for categorical features  
   - Scaling of numerical columns  
   - Null handling

2. **Training**  
   - Built using `LinearRegression` with cross-validation  
   - Pipeline stored as `insurance.pkl`

3. **Retraining Ready**  
   - `retrain_model.py` included to easily update the model with new data

4. **Deployment**  
   - Hosted locally via Streamlit for live predictions

---

## 💼 Business Use Case

Insurers often rely on claim estimates for:
- **Premium pricing models**
- **Risk assessment**
- **Claims fraud detection (when paired with other models)**
- **Financial reserve forecasting**

---

## 🖥️ How to Run Locally

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/insurance-claim-estimator.git
cd insurance-claim-estimator
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Launch the App**
```bash
streamlit run app.py
```

4. **Open in Browser**  
Visit [http://localhost:8501](http://localhost:8501)

---

## 🧪 Interface Overview

Once the app launches, users can:
- Select demographic/medical values via sidebar
- Hit "Predict"
- View real-time estimated claim amount on-screen

---

## 📁 Project Structure

```
.
├── app.py                # Main Streamlit application
├── insurance.pkl         # Trained ML model (joblib)
├── retrain_model.py      # Script to retrain model using CSV
├── insurance_data.csv    # Sample dataset
├── requirements.txt      # Python dependencies
└── README.md             # You're reading it!
```

---

## 🤝 Credits

Originally adapted and improved upon a public repository to better reflect practical applications and improve feature handling. Model retrained, app redesigned, and bugs resolved to demonstrate production-readiness.

---

## 📌 Note

This project is educational and portfolio-driven, not intended for clinical or actuarial use. If you’d like to collaborate or request a new feature, feel free to open a pull request.

---

## 🚀 Author

Dharun Krishna Nagaraj  
Feel free to connect on [LinkedIn](https://linkedin.com/in/dharunkrishna06)
