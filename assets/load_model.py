from deta import Deta  
import pickle

# Initialize with a Project Key
deta = Deta("c0qgqjoe_gKmnz1u4fWnpB75rFUHxZXF3wSCztwtr")

def load_model_from_deta_drive():
    drive = deta.Drive("api_model")
    model = pickle.loads(drive.get("model_rf_100.pkl").read())

    return model

def load_model():
    model = pickle.load(open("assets/model_rf_100.pkl", "rb"))
    return model
