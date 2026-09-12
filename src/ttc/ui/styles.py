APP_STYLE = """
QMainWindow, QWidget {
    font-family: "Inter", "Segoe UI", "Arial";
    font-size: 12px;
}
QMainWindow { background: #eef1f5; }
QMenuBar { background: #ffffff; border-bottom: 1px solid #d7dce3; }
QMenuBar::item { padding: 6px 9px; }
QToolBar { background: #ffffff; border-bottom: 1px solid #d7dce3; spacing: 4px; padding: 4px; }
QToolButton { padding: 5px 8px; border-radius: 5px; }
QToolButton:hover { background: #edf2f7; }
QDockWidget { color: #15253f; font-weight: 600; }
QDockWidget::title { background: #f7f9fb; padding: 7px; border-bottom: 1px solid #d7dce3; }
QTreeWidget, QTableWidget, QTableView, QPlainTextEdit { background: #ffffff; border: 1px solid #d7dce3; }
QHeaderView::section { background: #f4f6f9; border: 0; border-bottom: 1px solid #d7dce3; padding: 5px; font-weight: 600; }
QTabWidget::pane { border: 1px solid #cfd6df; }
QTabBar::tab { background: #e9edf2; padding: 7px 14px; border: 1px solid #cfd6df; border-bottom: 0; }
QTabBar::tab:selected { background: #ffffff; }
QGroupBox { font-weight: 600; border: 1px solid #d7dce3; border-radius: 6px; margin-top: 9px; padding-top: 8px; }
QGroupBox::title { subcontrol-origin: margin; left: 8px; padding: 0 4px; }
QStatusBar { background: #172f55; color: white; }
QStatusBar QLabel { color: white; }
"""
