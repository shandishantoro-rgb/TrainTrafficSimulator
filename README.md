# Train Traffic Simulator (TTC)

Train Traffic Simulator adalah aplikasi desktop simulasi operasi kereta api yang dibangun ulang dari awal untuk kebutuhan perencanaan, visualisasi jaringan, jadwal perjalanan, dan pengembangan analisis operasi.

## Status

**v0.1.0 — Fondasi aplikasi / UI shell**

Versi awal ini memfokuskan pada identitas aplikasi, antarmuka berbahasa Indonesia, struktur proyek, model data dasar, dan kontrol simulasi awal. Engine simulasi operasional lengkap belum diimplementasikan.

## Teknologi

- Python 3.11+
- PySide6 / Qt 6
- PyInstaller untuk packaging desktop

## Menjalankan aplikasi

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m ttc
```

Windows:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -e .
python -m ttc
```

## Struktur awal

```text
src/ttc/
├── app.py
├── core/
│   ├── models.py
│   └── simulation.py
├── data/
│   └── sample_project.py
└── ui/
    ├── main_window.py
    ├── network_view.py
    └── styles.py
```

## Sasaran pengembangan

1. Fondasi UI Train Traffic Simulator.
2. Model stasiun, jalur, kereta, dan jadwal.
3. Penyimpanan proyek TTC.
4. Editor jaringan.
5. Grafik perjalanan KA.
6. Engine simulasi waktu tempuh, dwell, headway, dan konflik.
7. Analisis operasi dan perbandingan skenario.
8. Packaging macOS dan Windows.

Lihat `docs/ROADMAP.md` untuk tahapan pengembangan.
