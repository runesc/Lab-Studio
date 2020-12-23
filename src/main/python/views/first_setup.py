from fbs_runtime.application_context.PySide6 import LifeCycle
from PySide6.QtWidgets import QWidget, QPushButton

class FirstSetup(QWidget, LifeCycle):

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)

        self.parent = parent
        self.kwargs = kwargs

        self.app_life_cycle()

    def render_(self):
        message = QPushButton("hola", self)