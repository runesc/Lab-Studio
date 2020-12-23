from fbs_runtime.application_context.PySide6 import LifeCycle
from PySide6.QtWidgets import QWidget

class Report(QWidget, LifeCycle):

    def __init__(self, parent=None, **kwargs):
        super().__init__()

        self.parent = parent
        self.kwargs = kwargs

        self.app_life_cycle()

    def render_(self):
        print(self.parent.frameSize())