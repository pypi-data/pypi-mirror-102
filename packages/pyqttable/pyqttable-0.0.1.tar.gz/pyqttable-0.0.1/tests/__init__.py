# -*- coding: utf-8 -*-
"""doc string"""

import datetime as dt
import pandas as pd
import sys

from PyQt5 import QtWidgets
from pyqttable import PyQtTable

app = QtWidgets.QApplication(sys.argv)
config = [{'key': 'name', 'name': 'Name', 'sort_lt': lambda x, y: x[-1] < y[-1],
           'filter_type': 'multiple_choice', 'editable': False},
          {'key': 'age', 'name': 'Age', 'type': int, 'h_align': 'r', 'filter_type': 'expression'},
          {'key': 'gender', 'name': 'Gender', 'selection': ['male', 'female'], 'bg_color': (135, 206, 250)},
          {'key': 'smart', 'name': 'Smart', 'type': bool, 'filter_type': 'expression'},
          {'key': 'birthday', 'name': 'Birthday', 'type': dt.date, 'filter_type': 'expression'},
          {'key': 'time', 'name': 'Time', 'type': dt.time},
          ]
table = PyQtTable(None, config, True)
data = pd.DataFrame([
    {'name': 'Xu Tongyan', 'age': 27, 'gender': 'male', 'smart': True,
     'birthday': dt.date(1994, 6, 27), 'time': dt.time(20, 30, 0)},
    {'name': 'Su Chenyao', 'age': 24, 'gender': 'female', 'smart': False,
     'birthday': dt.date(1996, 10, 12), 'time': dt.time(20, 30, 0)},
])
table.set_data(data)
table.setMinimumWidth(400)
table.setMinimumHeight(300)
table.show()
signal = app.exec_()
print(table.get_data(full=False))
sys.exit(signal)
