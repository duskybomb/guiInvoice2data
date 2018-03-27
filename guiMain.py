from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QPushButton, QGridLayout, QComboBox,
                             QCheckBox)
import sys


class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        file_label = QLabel('File')
        open_file_button = QPushButton('Select File', self)

        input_reader_label = QLabel('Input Reader')
        # self.input_reader_selected = QLabel("pdftotext", self)

        combo = QComboBox(self)
        combo.addItem("pdftotext")
        combo.addItem("pdfminer")
        combo.addItem("tesseract")
        # combo.activated[str].connect(self.onActivated)

        output_format_label = QLabel('Output Format')

        csv_checkbox = QCheckBox('csv', self)
        csv_checkbox.toggle()
        json_checkbox = QCheckBox('json', self)
        xml_checkbox = QCheckBox('XML', self)
        # cb.stateChanged.connect(self.changeTitle)

        output_field_button = QPushButton('Select Output Fields')

        template_label = QLabel('Template')
        custom_template_checkbox = QCheckBox('Use custom template', self)
        exclude_template_checkbox = QCheckBox('Exclude inbuilt template', self)
        select_custom_template_button = QPushButton('Select custom template')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(file_label, 1, 0)
        grid.addWidget(open_file_button, 1, 1)

        grid.addWidget(input_reader_label, 2, 0)
        # grid.addWidget(self.input_reader_selected, 2, 2)
        grid.addWidget(combo, 2, 1)

        grid.addWidget(output_format_label, 3, 0)
        grid.addWidget(csv_checkbox, 3, 1)
        grid.addWidget(json_checkbox, 3, 2)
        grid.addWidget(xml_checkbox, 3, 3)

        grid.addWidget(output_field_button, 4, 1)

        grid.addWidget(template_label, 5, 0)
        grid.addWidget(custom_template_checkbox, 5, 1)
        grid.addWidget(select_custom_template_button, 5,2)

        grid.addWidget(exclude_template_checkbox, 6, 1)

        self.setLayout(grid)

        # self.setFixedSize(self.layout.sizeHint())

        # self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Invoice2data')
        self.show()

    # def onActivated(self, text):
    #     self.input_reader_selected.setText(text)
    #     self.input_reader_selected.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
