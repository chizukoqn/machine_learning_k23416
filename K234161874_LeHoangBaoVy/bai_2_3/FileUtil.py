import pickle
import datetime
import os

class FileUtil:
    @staticmethod
    def savemodel(model, filename):
        try:
            pickle.dump(model, open(filename, "wb"))
            return True
        except:
            print("An exception occurred")
            return False
    @staticmethod
    def loadmodel(filename):
        try:
            model = pickle.load(open(filename, 'rb'))
            return model
        except:
            print("An exception occurred")
            return None

    @staticmethod
    def savemodel_auto(model, folder="models"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"housingmodel_{timestamp}.zip"
        filepath = os.path.join(folder, filename)
        try:
            pickle.dump(model, open(filepath, "wb"))
            return filepath
        except Exception as e:
            print("An exception occurred while auto-saving:", e)
            return None

    @staticmethod
    def list_models(folder="models"):
        if not os.path.exists(folder):
            return []
        files = [f for f in os.listdir(folder) if f.endswith(".zip")]
        return sorted(files, reverse=True)