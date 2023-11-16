import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
from PyQt5.uic import loadUi

from main_window_ui import Ui_MainWindow
from find_replace_window_ui import Ui_FindReplaceWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_New.triggered.connect(self.NewFile)
        self.action_Open.triggered.connect(self.OpenFile)
        self.action_Save.triggered.connect(self.SaveFile)
        self.action_Find_Replace.triggered.connect(self.findAndReplace)
        self.action_About.triggered.connect(self.about)

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        text = self.textEdit.toPlainText()
        text = text.replace("qw", "ab")
        self.textEdit.setPlainText(text)
        dialog.exec()

    def NewFile(self):
        self.textEdit.setText("")

    def OpenFile(self):
        file_name = QFileDialog.getOpenFileName(self)[0]

        try:
            with open(file_name, 'r') as file:
                data = file.read()
                self.textEdit.setText(data)
            file.close()
        except FileNotFoundError:
            print("No such file")

    def SaveFile(self):
        file_name = QFileDialog.getSaveFileName(self)[0]

        try:
            file = open(file_name, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        except FileNotFoundError:
            print("No such file")

    def about(self):
        QMessageBox.about(
            self,
            "About Text Editor",
            "<pre><strong>Basic functionality:<br /></strong></pre>"
            "<ul>"
            "<li><span>Ability to edit the file</span></li>"
            "<li><span><span>Text search and replace</span></span></li>"
            "<li><span>Hotkeys for coping, pasting, saving and exiting</span></li>"
            "</ul>"
            "<p><span>Python, PyQt5</span></p>"
            "<p><em>Developed by Kirill Lukashev</em></p>"
        )

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())