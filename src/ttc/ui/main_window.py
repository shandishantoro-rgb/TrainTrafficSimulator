from datetime import datetime

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QDockWidget, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMessageBox, QPlainTextEdit, QSplitter, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget
)

from ttc import APP_NAME, APP_SHORT_NAME, __version__
from ttc.core.simulation import SimulationController, SimulationState
from ttc.data.sample_project import make_sample_project
from .network_view import NetworkView
from .styles import APP_STYLE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.project = make_sample_project()
        self.sim = SimulationController()
        self.setWindowTitle(f"{APP_SHORT_NAME} – {APP_NAME}")
        self.resize(1500, 900)
        self.setMinimumSize(1100, 700)
        self.setStyleSheet(APP_STYLE)

        self._build_actions()
        self._build_menus()
        self._build_toolbar()
        self._build_center()
        self._build_left_docks()
        self._build_right_docks()
        self._build_bottom_dock()
        self._build_statusbar()

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._tick)
        self._log("Sistem", "TTC siap digunakan")

    def _build_actions(self):
        self.act_new = QAction("Baru", self, shortcut=QKeySequence.New, triggered=self._new_project)
        self.act_open = QAction("Buka", self, shortcut=QKeySequence.Open, triggered=self._not_implemented)
        self.act_save = QAction("Simpan", self, shortcut=QKeySequence.Save, triggered=self._not_implemented)
        self.act_exit = QAction("Keluar", self, shortcut=QKeySequence.Quit, triggered=self.close)

        self.act_run = QAction("Jalankan", self, triggered=self._run)
        self.act_pause = QAction("Jeda", self, triggered=self._pause)
        self.act_stop = QAction("Hentikan", self, triggered=self._stop)
        self.act_reset = QAction("Atur Ulang", self, triggered=self._reset)

        self.act_zoom_in = QAction("Perbesar", self, shortcut=QKeySequence.ZoomIn, triggered=lambda: self.network.scale(1.2, 1.2))
        self.act_zoom_out = QAction("Perkecil", self, shortcut=QKeySequence.ZoomOut, triggered=lambda: self.network.scale(1/1.2, 1/1.2))
        self.act_fit = QAction("Sesuaikan", self, triggered=lambda: self.network.fitInView(self.network.scene().sceneRect(), Qt.KeepAspectRatio))
        self.act_about = QAction("Tentang TTC", self, triggered=self._about)

    def _build_menus(self):
        for title in ["Berkas", "Edit", "Tampilan", "Simulasi", "Jadwal", "Infrastruktur", "Kereta", "Alat", "Jendela", "Bantuan"]:
            menu = self.menuBar().addMenu(title)
            if title == "Berkas":
                menu.addActions([self.act_new, self.act_open, self.act_save])
                menu.addSeparator(); menu.addAction(self.act_exit)
            elif title == "Simulasi":
                menu.addActions([self.act_run, self.act_pause, self.act_stop, self.act_reset])
            elif title == "Tampilan":
                menu.addActions([self.act_zoom_in, self.act_zoom_out, self.act_fit])
            elif title == "Bantuan":
                menu.addAction(self.act_about)
            else:
                placeholder = QAction("Fitur akan dikembangkan", self)
                placeholder.setEnabled(False)
                menu.addAction(placeholder)

    def _build_toolbar(self):
        tb = QToolBar("Toolbar Utama", self)
        tb.setMovable(False)
        tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(tb)
        tb.addActions([self.act_new, self.act_open, self.act_save])
        tb.addSeparator()
        tb.addActions([self.act_run, self.act_pause, self.act_stop, self.act_reset])
        tb.addSeparator()
        tb.addWidget(QLabel("Kecepatan Simulasi: "))
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["0.5x", "1x", "2x", "5x", "10x"])
        self.speed_combo.setCurrentText("1x")
        self.speed_combo.currentTextChanged.connect(self._speed_changed)
        tb.addWidget(self.speed_combo)
        tb.addSeparator()
        tb.addActions([self.act_zoom_in, self.act_zoom_out, self.act_fit])

    def _build_center(self):
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(False)
        self.network = NetworkView()
        self.tabs.addTab(self.network, "Peta Jalur")
        diagram_placeholder = QLabel("Diagram perjalanan akan tersedia pada tahap berikutnya.")
        diagram_placeholder.setAlignment(Qt.AlignCenter)
        self.tabs.addTab(diagram_placeholder, "Diagram Perjalanan")
        self.setCentralWidget(self.tabs)

    def _build_left_docks(self):
        dock = QDockWidget("Proyek", self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        tree = QTreeWidget(); tree.setHeaderHidden(True)
        root = QTreeWidgetItem(["TTC"])
        tree.addTopLevelItem(root)
        for group, items in {
            "Jalur dan Stasiun": ["Jalur", "Stasiun", "Sinyal", "Wesel", "Objek Lainnya"],
            "Jadwal Kereta": ["Layanan Kereta", "Diagram Perjalanan"],
            "Data Infrastruktur": ["Kecepatan Jalur", "Kemiringan", "Blok", "Lainnya"],
        }.items():
            g = QTreeWidgetItem([group]); root.addChild(g)
            for item in items: g.addChild(QTreeWidgetItem([item]))
        root.setExpanded(True)
        for i in range(root.childCount()): root.child(i).setExpanded(True)
        dock.setWidget(tree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock)

        prop_dock = QDockWidget("Properti", self)
        w = QWidget(); form = QFormLayout(w)
        st = self.project.stations[0]
        for k, v in [
            ("Nama", st.name), ("Kode", st.code), ("Tipe", "Stasiun Penumpang"),
            ("Panjang Peron (m)", str(st.platform_length_m)), ("Jumlah Jalur", str(st.track_count)),
            ("Elevasi (m)", f"{st.elevation_m:+g}"), ("Wilayah", st.region), ("Keterangan", st.description)
        ]:
            form.addRow(k, QLabel(v))
        prop_dock.setWidget(w)
        self.addDockWidget(Qt.LeftDockWidgetArea, prop_dock)
        self.tabifyDockWidget(dock, prop_dock)
        dock.raise_()

    def _build_right_docks(self):
        dock = QDockWidget("Daftar Kereta", self)
        table = QTableWidget(len(self.project.trains), 4)
        table.setHorizontalHeaderLabels(["ID", "Nama Kereta", "Status", "Posisi"])
        table.setAlternatingRowColors(True)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        for r, t in enumerate(self.project.trains):
            for c, value in enumerate([t.train_id, t.name, t.status.value, t.position]):
                table.setItem(r, c, QTableWidgetItem(str(value)))
        table.resizeColumnsToContents()
        dock.setWidget(table)
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        info_dock = QDockWidget("Informasi Kereta", self)
        w = QWidget(); form = QFormLayout(w)
        t = self.project.trains[2]
        for k, v in [
            ("ID Kereta", t.train_id), ("Nama Kereta", t.name), ("Jenis", t.train_type),
            ("Status", t.status.value), ("Kecepatan", f"{t.speed_kmh:g} km/jam"),
            ("Posisi", t.position), ("Tujuan", t.destination), ("Keterlambatan", f"{t.delay_min:+d} menit")
        ]:
            form.addRow(k, QLabel(str(v)))
        info_dock.setWidget(w)
        self.addDockWidget(Qt.RightDockWidgetArea, info_dock)

        view_dock = QDockWidget("Opsi Tampilan", self)
        w2 = QWidget(); lay = QVBoxLayout(w2)
        for text, checked in [
            ("Tampilkan Nama Stasiun", True), ("Tampilkan Sinyal", True),
            ("Tampilkan Nomor Jalur", False), ("Tampilkan Nama Kereta", True),
            ("Tampilkan Blok", False), ("Mode Latar Gelap", True)
        ]:
            cb = QCheckBox(text); cb.setChecked(checked); lay.addWidget(cb)
        lay.addStretch(1)
        view_dock.setWidget(w2)
        self.addDockWidget(Qt.RightDockWidgetArea, view_dock)

    def _build_bottom_dock(self):
        dock = QDockWidget("Log Simulasi", self)
        self.log = QTableWidget(0, 3)
        self.log.setHorizontalHeaderLabels(["Waktu", "Kategori", "Pesan"])
        self.log.horizontalHeader().setStretchLastSection(True)
        dock.setWidget(self.log)
        self.addDockWidget(Qt.BottomDockWidgetArea, dock)

    def _build_statusbar(self):
        bar = QStatusBar(); self.setStatusBar(bar)
        self.lbl_state = QLabel("Siap")
        self.lbl_clock = QLabel("Waktu Simulasi: 00:00:00")
        self.lbl_speed = QLabel("Kecepatan: 1x")
        self.lbl_count = QLabel(f"Jumlah Kereta: {len(self.project.trains)}")
        self.lbl_version = QLabel(f"TTC v{__version__}  |  Indonesia")
        bar.addWidget(self.lbl_state)
        bar.addPermanentWidget(self.lbl_clock)
        bar.addPermanentWidget(self.lbl_speed)
        bar.addPermanentWidget(self.lbl_count)
        bar.addPermanentWidget(self.lbl_version)

    def _log(self, category: str, message: str):
        row = self.log.rowCount(); self.log.insertRow(row)
        values = [datetime.now().strftime("%H:%M:%S"), category, message]
        for c, value in enumerate(values): self.log.setItem(row, c, QTableWidgetItem(value))
        self.log.scrollToBottom()

    def _run(self):
        self.sim.start(); self.timer.start(); self.lbl_state.setText("Berjalan")
        self._log("Sistem", "Simulasi dijalankan")

    def _pause(self):
        self.sim.pause(); self.timer.stop(); self.lbl_state.setText("Jeda")
        self._log("Sistem", "Simulasi dijeda")

    def _stop(self):
        self.sim.stop(); self.timer.stop(); self.lbl_state.setText("Berhenti")
        self._log("Sistem", "Simulasi dihentikan")

    def _reset(self):
        self.sim.reset(); self.timer.stop(); self.lbl_state.setText("Siap")
        self.lbl_clock.setText("Waktu Simulasi: 00:00:00")
        self._log("Sistem", "Simulasi diatur ulang")

    def _tick(self):
        self.sim.simulated_seconds += max(1, int(self.sim.speed_factor))
        s = self.sim.simulated_seconds
        h, rem = divmod(s, 3600); m, sec = divmod(rem, 60)
        self.lbl_clock.setText(f"Waktu Simulasi: {h:02d}:{m:02d}:{sec:02d}")

    def _speed_changed(self, text: str):
        self.sim.speed_factor = float(text.removesuffix("x"))
        self.lbl_speed.setText(f"Kecepatan: {text}")
        self._log("Sistem", f"Kecepatan simulasi diubah menjadi {text}")

    def _new_project(self):
        self._log("Proyek", "Proyek baru dibuat")

    def _not_implemented(self):
        QMessageBox.information(self, "TTC", "Fitur ini disiapkan pada tahap pengembangan berikutnya.")

    def _about(self):
        QMessageBox.about(
            self, "Tentang TTC",
            f"<b>TTC – Train Traffic Simulator</b><br>Versi {__version__}<br><br>"
            "Simulator lalu lintas kereta dengan antarmuka Bahasa Indonesia.<br>"
            "Implementasi baru yang dikembangkan bertahap untuk kebutuhan simulasi operasi kereta."
        )
