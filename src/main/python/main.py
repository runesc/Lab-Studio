import sys
from fbs_runtime.application_context.PySide6 import ApplicationContext, LifeCycle
from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget
from core.funcions import d_flex


#! Vistas de la app
from views import Report
from views import FirstSetup


class MyApp(LifeCycle, QMainWindow, ApplicationContext):

    def render_(self):

        self.first_setup = FirstSetup(self)

        """#* Area de barras
        self.top_bar = QWidget(parent=self, objectName='top-bar')
        self.left_bar = QWidget(parent=self, objectName='left-bar')


        #* Contenido principal de la app
        self.content = QStackedWidget(parent=self, objectName='content')

        # Cargar vistas en el stacked widget
        for widget in [FirstSetup, Report]:
            self.content.addWidget(widget(self))"""


    def translate(self):
        self.first_setup.resize(self.frameSize())
        #* Area de barras
        """self.top_bar.resize(self.width(), d_flex(10, self.height()))

        self.left_bar.resize(d_flex(7, self.width()), d_flex(90, self.height()))
        self.left_bar.move(0, d_flex(10, self.height()))


        #* Contenido principal de la app

        self.content.resize(d_flex(93, self.width()), d_flex(90, self.height()))
        self.content.move(d_flex(7, self.width()), d_flex(10, self.height()))
        """

    def resizeEvent(self, event):
        self.translate()

    def setCss(self):
        with open(self.get_resource('css/styles.css'), 'r') as styles:
            self.setStyleSheet(styles.read())

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MyApp()
    window.resize(1200, 695)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)