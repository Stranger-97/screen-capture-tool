# -*- coding: utf-8 -*-
import sys
from forms.mainForm.index import mainForm
from PyQt5.QtWidgets import QApplication

if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    mf = mainForm()
    mf.show()
    sys.exit(app.exec_())