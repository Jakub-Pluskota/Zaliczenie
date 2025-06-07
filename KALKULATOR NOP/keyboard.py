from PyQt6.QtWidgets import QGridLayout, QPushButton

class VirtualKeyboard:
    def __init__(self, input_field, on_equal_callback, animate_button):
        self.input_field = input_field
        self.on_equal_callback = on_equal_callback
        self.animate_button = animate_button

    def create(self):
        layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('+', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('*', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('(', 3, 2), (')', 3, 3),
            ('C', 4, 0), ('=', 4, 1, 1, 3)
        ]

        for btn_data in buttons:
            if len(btn_data) == 3:
                label, row, col = btn_data
                rowspan, colspan = 1, 1
            else:
                label, row, col, rowspan, colspan = btn_data

            btn = QPushButton(label)
            btn.setFixedSize(50, 40)
            layout.addWidget(btn, row, col, rowspan, colspan)

            if label == '=':
                btn.clicked.connect(lambda _, b=btn: (self.animate_button(b), self.on_equal_callback()))
            elif label == 'C':
                btn.clicked.connect(lambda _, b=btn: (self.animate_button(b), self.input_field.clear()))
            else:
                btn.clicked.connect(lambda _, b=btn, t=label: (self.animate_button(b), self.input_field.insert(t)))

        return layout