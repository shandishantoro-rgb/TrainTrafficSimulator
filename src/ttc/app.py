import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

from . import APP_NAME, __version__
from .ui.main_window import MainWindow


def main() -> int:
    QCoreApplication.setOrganizationName("TTC Indonesia")
    QCoreApplication.setApplicationName(APP_NAME)
    QCoreApplication.setApplicationVersion(__version__)

    app = QApplication(sys.argv)
    app.setApplicationDisplayName(f"TTC – {APP_NAME}")
    window = MainWindow()
    window.show()
    return app.exec()
