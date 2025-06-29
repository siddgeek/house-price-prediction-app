# 🏘️ End-to-End House Price Prediction App (19 Features, ML + Streamlit)

This is a **machine learning-powered web application** built using **Streamlit**, which predicts house prices based on multiple features like number of bedrooms, bathrooms, living area, and more. The model has been trained using a real dataset of house sales from King County (Seattle), USA.

🌐 **Live Demo:** [Click here to open the app](https://house-price-prediction-app-b9a7kmh9l83xreuvrr5rbr.streamlit.app)

---

## 📌 Project Highlights

- 🔍 Predicts house prices based on **19 real-world features**
- ⚙️ Built with **Python, Pandas, Scikit-learn, and Streamlit**
- 💾 Uses **Gradient Boosting Regressor** for high accuracy
- 📈 Data visualization using **Seaborn and Matplotlib** (EDA Phase)
- 💻 **Responsive UI** built with Streamlit
- 📦 Easily deployable to **Streamlit Cloud**

---

## 🔧 Tech Stack

| Tool/Library  | Usage                        |
| ------------- | ---------------------------- |
| Python        | Core Programming Language    |
| Pandas, NumPy | Data Handling and Processing |
| Scikit-learn  | Model Training & Evaluation  |
| Joblib        | Model Serialization          |
| Streamlit     | Web App Interface            |

---

## 📁 Project Structure

```
├── app.py                # Streamlit web app code
├── model.pkl             # Trained ML model (GradientBoostingRegressor)
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation (this file)
```

---

## 📊 Features Used for Prediction

The model uses the following input features:

- Bedrooms
- Bathrooms
- Square footage (living area)
- Lot size (sqft\_lot)
- Number of floors
- Waterfront presence
- View quality
- Condition of the house
- Grade (overall construction)
- Above-ground square footage
- Basement square footage
- Year built
- Year renovated
- Zipcode
- Latitude & Longitude
- Living area of neighboring 15 houses
- Lot size of neighboring 15 houses

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
https://github.com/siddgeek/house-price-prediction-app.git

# 2. Navigate to the folder
cd house-price-prediction-app

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```



## 🧠 Future Enhancements

- Add map-based house visualization
- Add user authentication
- Improve model using hyperparameter tuning
- Add feature to save predictions



