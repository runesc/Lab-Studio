import sys
from fbs_runtime.application_context.PySide6 import ApplicationContext, LifeCycle
from PySide6.QtWidgets import QMainWindow, QLabel


class MyApp(LifeCycle, QMainWindow):

    def render_(self):
        label = QLabel('Hello World!', parent=self)

    def translate(self):
        self.resize(250, 150)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MyApp()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)