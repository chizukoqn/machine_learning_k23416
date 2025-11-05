import sys
import numpy as np
import pickle
from PyQt6 import QtWidgets
from HousePricePrediction import Ui_MainWindow

class HousePriceApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = None

        self.ui.pushButtonLoadModel.clicked.connect(self.load_model)
        self.ui.pushButtonPredict.clicked.connect(self.predict_price)
        self.ui.pushButtonClear.clicked.connect(self.clear_fields)
        self.ui.pushButtonExit.clicked.connect(self.close_app)

    def load_model(self):
        try:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, "Chọn mô hình", "", "Model Files (*.zip *.pkl)"
            )
            if file_path:
                self.model = pickle.load(open(file_path, 'rb'))
                QtWidgets.QMessageBox.information(self, "Thông báo", "✅ Đã nạp mô hình thành công!")
            else:
                QtWidgets.QMessageBox.warning(self, "Cảnh báo", "⚠ Bạn chưa chọn file mô hình.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi nạp mô hình:\n{str(e)}")

    def predict_price(self):
        try:
            if self.model is None:
                QtWidgets.QMessageBox.warning(self, "Cảnh báo", "⚠ Hãy nạp mô hình trước khi dự báo!")
                return

            # Lấy dữ liệu từ các ô nhập
            income = float(self.ui.lineEditIncome.text())
            house_age = float(self.ui.lineEditHouseAge.text())
            rooms = float(self.ui.lineEditRooms.text())
            bedrooms = float(self.ui.lineEditBedroom.text())
            population = float(self.ui.lineEditPopulation.text())

            input_data = np.array([[income, house_age, rooms, bedrooms, population]])

            predicted_price = self.model.predict(input_data)[0]
            self.ui.lineEditPrice.setText(f"${predicted_price:,.2f}")

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đúng định dạng số!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Lỗi khi dự báo:\n{str(e)}")

    def clear_fields(self):
        self.ui.lineEditIncome.clear()
        self.ui.lineEditHouseAge.clear()
        self.ui.lineEditRooms.clear()
        self.ui.lineEditBedroom.clear()
        self.ui.lineEditPopulation.clear()
        self.ui.lineEditPrice.clear()

    def close_app(self):
        choice = QtWidgets.QMessageBox.question(
            self, "Thoát", "Bạn có chắc muốn thoát không?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if choice == QtWidgets.QMessageBox.StandardButton.Yes:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HousePriceApp()
    window.show()
    sys.exit(app.exec())