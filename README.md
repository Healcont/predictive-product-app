**Predictive Analytics Web Application – Product Popularity**



**Overview**



This project is a predictive analytics web application designed to estimate the probability that a product will become popular in the market based on historical data and product attributes. The dataset used to train and evaluate the model was sourced from Kaggle (https://www.kaggle.com), a public platform for data science and machine learning datasets.



The solution combines machine learning, data analytics, and a Flask-based web interface, following good engineering practices such as modularization, virtual environments, and version control with Git/GitHub.



**This repository is presented for:**



* A business-oriented prototype that demonstrates how predictive models can support strategic and commercial decision-making
* For recruiters and technical evaluators



**Business Value**



From a business perspective, the application can support:



* Product portfolio optimization
* Early identification of high-potential products
* Data-driven pricing and commercialization strategies
* Reduction of risk when launching new products
* The model outputs a probability score, allowing decision-makers to act proactively rather than reactively.



**Technical Solution**



**Architecture**



* Machine Learning Model: Random Forest Classifier
* Backend: Python + Flask
* Preprocessing Layer: Modularized feature engineering logic
* Model Persistence: Pickle serialization
* Interface: HTML form rendered via Flask templates





**Machine Learning Approach**



Algorithms evaluated during experimentation:



* Logistic Regression
* Decision Tree
* Random Forest (selected)



Selection criteria:



* Accuracy
* Stability
* Interpretability for business use



The final model was trained offline using a Jupyter Notebook and serialized using pickle for later inference in the web application.



**How to Run the Application**



1\. Clone the repository



&nbsp;	git clone <repository-url>

&nbsp;	cd project-root



2\. Create and activate a virtual environment



&nbsp;	python -m venv predict-env



&nbsp;	Windows:



&nbsp;	predict-env\\Scripts\\activate



3\. Install dependencies



&nbsp;	pip install -r requirements.txt



4\. Run the application



&nbsp;	python app.py



The application will be available at:



&nbsp;	http://127.0.0.1:5000/



**Future Improvements**



* Automated pipeline with CI/CD (GitHub Actions or Azure DevOps)
* API-first architecture for integration with other systems
* Deployment to cloud platforms (Azure / AWS)



**Disclaimer**



This project is for educational and demonstration purposes. Any datasets used have been anonymized or simplified and do not represent confidential business information.

