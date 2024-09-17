import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, land_size, house_size, beds, baths):
    try:
        loc_index = __data_columns.index(location.lower())

    except:
        loc_index = -1

    x_pred = np.zeros(len(__data_columns))
    x_pred[1] = land_size
    x_pred[3] = house_size
    x_pred[2] = beds
    x_pred[0] = baths
    if loc_index >= 0:
        x_pred[loc_index] = 1

    return round(__model.predict([x_pred])[0], 2)


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[4:]

    global __model
    with open("./artifacts/Sri_Lanka_House_Price_Prediction_Model_Final.pickle", 'rb') as f:
        model_data = f.read()
        __model = pickle.loads(model_data)
    print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Piliyandala', 2000, 2500, 4, 3))
    print(get_estimated_price('Battaramulla', 1700.00, 2290.00, 4, 3))
    print(get_estimated_price('Colombo 2', 1700, 1800,2 , 1))