💰 Insurance Cost Predictor

The Insurance Cost Predictor is a Machine Learning–based application designed to estimate medical insurance charges based on user-specific factors such as age, BMI, number of dependents, smoking habits, and region.

This project demonstrates a complete end-to-end ML workflow, including data preprocessing, model training, model serialization, and deployment using a simple interactive user interface.

🎯 Objectives

Predict insurance costs accurately using machine learning

Understand real-world regression problems

Apply feature encoding and data preprocessing

Deploy a trained model for real-time predictions

🛠️ Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Pickle

GitHub

⚙️ Key Features

Cleaned and preprocessed real-world insurance dataset

Exploratory Data Analysis (EDA)

Categorical feature encoding

Regression model training and evaluation

Saved trained model (insurance_model.pkl)

Interactive UI for insurance cost prediction

🧠 System Design

insurance.csv contains the dataset used for training

insurance.ipynb includes data preprocessing, EDA, and model training

insurance_model.pkl stores the trained regression model

ui.py loads the trained model and takes user inputs

requirements.txt manages project dependencies

📂 Project Structure
Insurance_Cost_Predictor/
│
├── insurance.csv              # Dataset
├── insurance.ipynb            # Model training & analysis
├── insurance_model.pkl        # Trained ML model
├── ui.py                      # Streamlit user interface
├── requirements.txt           # Project dependencies
├── LICENSE                    # MIT License
└── README.md

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/ritik12004/Insurance_Cost_Predictor.git

2️⃣ Navigate to the project directory
cd Insurance_Cost_Predictor

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
streamlit run ui.py

📊 Learning Outcomes

Hands-on experience with regression models

Understanding of categorical feature encoding

Practical exposure to model deployment

Real-world dataset handling and prediction

🚀 Future Enhancements

Improve accuracy using advanced regression techniques

Add feature importance visualization

Deploy the app on cloud platforms (Streamlit Cloud / AWS)

Add model explainability (SHAP)

👤 Author

Ritik Gujre
Student | Aspiring Data Scientist | Python Developer
Samrat Ashok Technological Institute, Vidisha

GitHub: https://github.com/ritik12004

LinkedIn: https://www.linkedin.com/in/ritikgujre/

Email: ritik26cs103@satiengg.in

📜 License

This project is licensed under the MIT License.
See the LICENSE file for more details.
