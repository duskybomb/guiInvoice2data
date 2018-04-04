from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QPushButton, QGridLayout, QComboBox,
                             QCheckBox, QFileDialog)
import sys
from invoice2data import main

class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.args = ""

        file_label = QLabel('File')
        open_file_button = QPushButton('Select File', self)
        self.file_selected = QLabel('')

        open_file_button.clicked.connect(self.showFileDialog)

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
        self.template_selected = QLabel('')

        select_custom_template_button.clicked.connect(self.showTempalateDialog)

        empty_row_label = QLabel('')

        submit_button = QPushButton('Submit')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(file_label, 1, 0)
        grid.addWidget(open_file_button, 1, 1)
        grid.addWidget(self.file_selected, 1, 2)

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
        grid.addWidget(self.template_selected, 6, 2)

        grid.addWidget(empty_row_label, 7, 1)

        grid.addWidget(submit_button, 8, 1)

        self.setLayout(grid)

        # self.setFixedSize(self.layout.sizeHint())

        # self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Invoice2data')
        self.show()

    # def onActivated(self, text):
    #     self.input_reader_selected.setText(text)
    #     self.input_reader_selected.adjustSize()
    def showFileDialog(self):

        fname = QFileDialog.getOpenFileNames(self, 'Open file', '/home', "pdf (*.pdf);; All Files (*)")
        if fname[0]:
            # print(str(fname[0][0]))
            self.file_selected.setText(str(fname[0][0]))
            # self.args = self.parser.parse_args(['--output-name', test_file, '--output-format', 'csv'] + self._get_test_file_path())

    def showTempalateDialog(self):

        custom_template_name = QFileDialog.getOpenFileName(self, 'Open file', '/home', "YAML (*.yml);; All Files (*)")
        if custom_template_name[0]:
            # print(str(fname[0][0]))
            self.template_selected.setText(str(custom_template_name[0]))
            # self.args = self.parser.parse_args(['--output-name', test_file, '--output-format', 'csv'] + self._get_test_file_path())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
