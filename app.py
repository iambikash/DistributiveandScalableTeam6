from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load('Gradient_Boosting.pkl')
Final_data_set=joblib.load('Final_data_set.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict_price', methods=['POST'])
def predict_price():
    # Get input values from the form
    OverallQual= float(request.form['overall_qual'])
    GrLivArea= float(request.form['gr_liv_area'])
    TotalBsmtSF= float(request.form['total_bsmt_sf'])
    GarageCars= float(request.form['garage_cars'])
    SecondFlrSF= float(request.form['second_flr_sf'])
    BsmtFinSF1= float(request.form['bsmt_fin_sf1'])
    BsmtQual= float(request.form['bsmt_qual'])
    FirstFlrSF= float(request.form['first_flr_sf'])
    LotArea= float(request.form['lot_area'])
    YearRemodAdd= float(request.form['year_remod_add'])
    GarageType= float(request.form['garage_type'])
    YearBuilt= float(request.form['year_built'])
    FullBath= float(request.form['full_bath'])
    KitchenQual= float(request.form['kitchen_qual'])
    Fireplaces= float(request.form['fireplaces'])
    OverallCond= float(request.form['overall_cond'])
    GarageArea= float(request.form['garage_area'])
    MSZoning= float(request.form['ms_zoning'])
    FireplaceQu= float(request.form['fireplace_qu'])
    Neighborhood= float(request.form['neighborhood'])
    State = request.form['state']


    # Convert the input data to a DataFrame
    input_values =[OverallQual,GrLivArea,TotalBsmtSF,GarageCars,SecondFlrSF,BsmtFinSF1,
                   BsmtQual,FirstFlrSF,LotArea,YearRemodAdd,GarageType,YearBuilt,FullBath,
                   KitchenQual,Fireplaces,OverallCond,GarageArea,MSZoning,FireplaceQu,Neighborhood
                   ]
    #print(input_values)
    #print([Final_data_set])
    # Convert the input data to a DataFrame
    # Make predictions
    predicted_price = model.predict([input_values])
    Final_set = Final_data_set[Final_data_set['State']==State]
    Final_price = int(Final_set['Average_Price']/predicted_price * Final_set['Year 2023'])
    Crime_rate = int(Final_set['Crime_rate'])
    Number_of_hospital = int(Final_set['Number of Hospitals'])
    Number_of_school = int(Final_set['Number of Schools'])
    #print(State)

    # Render the template with the predicted price
    return render_template('result.html', predicted_price=predicted_price[0],Crime_rate=Crime_rate,Number_of_hospital=Number_of_hospital,
                           Number_of_school=Number_of_school,State=State,Final_price=Final_price)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)