import joblib
import pandas as pd
hpp = joblib.load("house_rent_prediction.pkl")
e = hpp['encoder']
s = hpp['scaler']
m = hpp['model']

new_house= pd.DataFrame({
    'BHK': [2],
    'Size': [1200],
    'Area Type': ['Super  Area'],
    'City': ['Bangalore'],
    'Furnishing Status': ['Semi-Furnished'],
    'Tenant Preferred': ['Family'],
    'Bathroom': [2],
    'Point of Contact': ['Contact Owner']
})

new_encoded = encoder.transform(new_house)
new_scaled = scaler.transform(new_encoded)


prediction = model.predict(new_scaled)
print("Predicted Rent:", prediction[0])