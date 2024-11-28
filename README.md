
# **Car Price Prediction App**

## **Overview**
The Car Price Prediction App predicts the selling price of a car based on its features such as mileage, age, fuel type, transmission type, and ownership details. This project uses a trained machine learning model and provides a simple web interface through Streamlit, making it accessible to everyone.

---

## **Features**
- **Predict Selling Price**: Input car details to get an estimated selling price.
- **Machine Learning Model**: A Random Forest Regressor trained on car details data.
- **Interactive Web App**: Built with Streamlit for an intuitive user interface.
- **Deployment**: Hosted publicly using Streamlit Cloud.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - **Data Analysis**: `pandas`, `numpy`
  - **Machine Learning**: `scikit-learn`, `joblib`
  - **Web Application**: `streamlit`
- **Deployment**: Streamlit Cloud

---

## **Project Structure**
```
Car Price Prediction/
├── car_price_model.pk1      # Trained Random Forest model
├── app.py                   # Streamlit application script
├── requirements.txt         # Required libraries
├── README.md                # Project documentation
```

---

## **How to Run Locally**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### **2. Install Dependencies**
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### **3. Run the Streamlit App**
Start the Streamlit server:
```bash
streamlit run app.py
```

### **4. Open in Browser**
Visit the URL displayed in your terminal (e.g., `http://localhost:8501`) to use the app.

---

## **Using the App**
1. **Input Car Details**:
   - Enter mileage (`Kilometers Driven`), car age, fuel type, seller type, transmission type, and ownership type in the sidebar.
2. **Get Predictions**:
   - Click "Predict Selling Price" to see the estimated car price.
3. **Output**:
   - The app will display the predicted selling price.

---

## **Deployment**
This project is deployed publicly using Streamlit Cloud. You can access the live app here:

[**Live App Demo**](#) *https://data-science-capstone-project-jfa9qiypapmccuac7mxfqh.streamlit.app/*

---

## **Model Details**
- **Model Type**: Random Forest Regressor
- **Trained On**: A cleaned dataset of car details.
- **Evaluation Metrics**:
  - Mean Absolute Error (MAE): *(Insert value)*
  - R² Score: *(Insert value)*

---

## **Future Improvements**
- Add more features (e.g., car brand, model, engine capacity) to enhance prediction accuracy.
- Explore advanced ML models such as Gradient Boosting or XGBoost.
- Integrate a database to save user inputs and predictions for future reference.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a detailed message about your changes"
   ```
4. Push the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License.

---

## **Contact**
For queries or feedback:
- **Email**: surajy88v@gmail.com
- **GitHub**: github.com/vinu166

