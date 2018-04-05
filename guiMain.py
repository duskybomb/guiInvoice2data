from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QPushButton, QGridLayout, QComboBox,
                             QFileDialog, QCheckBox, QMessageBox)
import sys
from invoice2data.main import *


class Interface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # self.args_list = []
        # self.args = ""
        self.file_names = []
        self.input_reader_list = []
        self.output_format_list = []

        file_label = QLabel('File')
        open_file_button = QPushButton('Select File', self)
        self.file_selected = QLabel('')

        open_file_button.clicked.connect(self.showFileDialog)

        input_reader_label = QLabel('Input Reader')
        # self.input_reader_selected = QLabel("pdftotext", self)

        input_combo = QComboBox(self)
        input_combo.addItem("pdftotext")
        input_combo.addItem("pdfminer")
        input_combo.addItem("tesseract")
        input_combo.activated[str].connect(self.onActivated)

        output_format_label = QLabel('Output Format')

        output_combo = QComboBox(self)
        output_combo.addItem("none")
        output_combo.addItem("csv")
        output_combo.addItem("json")
        output_combo.addItem("xml")
        output_combo.activated[str].connect(self.outputFormat)

        # csv_radio = QRadioButton('csv', self)
        # json_radio = QRadioButton('json', self)
        # xml_radio = QRadioButton('XML', self)

        # csv_checkbox.stateChanged.connect(self.csvOutputFormat)
        # json_checkbox.stateChanged.connect(self.jsonOutputFormat)
        # xml_checkbox.stateChanged.connect(self.xmlOutputFormat)

        output_field_button = QPushButton('Select Output Fields')

        template_label = QLabel('Template')
        custom_template_checkbox = QCheckBox('Use custom template', self)
        exclude_template_checkbox = QCheckBox('Exclude inbuilt template', self)
        select_custom_template_button = QPushButton('Select custom template')
        self.template_selected = QLabel('')

        select_custom_template_button.clicked.connect(self.showTempalateDialog)

        empty_row_label = QLabel('')

        submit_button = QPushButton('Submit')
        submit_button.clicked.connect(self.sendArg)
        self.submit_clicked_confirmation = QLabel('')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(file_label, 1, 0)
        grid.addWidget(open_file_button, 1, 1)
        grid.addWidget(self.file_selected, 1, 2)

        grid.addWidget(input_reader_label, 2, 0)
        # grid.addWidget(self.input_reader_selected, 2, 2)
        grid.addWidget(input_combo, 2, 1)

        grid.addWidget(output_format_label, 3, 0)
        grid.addWidget(output_combo, 3, 1)

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

    def onActivated(self, text):
        self.input_reader_list = ['--input-reader', text]

    def showFileDialog(self):

        fname = QFileDialog.getOpenFileNames(self, 'Open file', '/home', "pdf (*.pdf);; All Files (*)")
        if fname[0]:
            # print(str(fname[0][0]))
            self.file_selected.setText(str(fname[0][0]))
            self.file_names = fname[0]

    def outputFormat(self, text):
        self.output_format_list = ['--output-format', text]

    def showTempalateDialog(self):

        custom_template_name = QFileDialog.getOpenFileName(self, 'Open file', '/home', "YAML (*.yml);; All Files (*)")
        if custom_template_name[0]:
            # print(str(fname[0][0]))
            self.template_selected.setText(str(custom_template_name[0]))

    def sendArg(self):
        if self.file_names:
            parser = create_parser()
            print(parser.parse_args(self.file_names + self.input_reader_list + self.output_format_list))
            args = parser.parse_args(self.file_names + self.input_reader_list + self.output_format_list)
            main(args)
            QMessageBox.about(self, "Title", "Operation Executed")
        else:
            QMessageBox.about(self, "Title", "Error! Please specify the file")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Interface()
    sys.exit(app.exec_())
