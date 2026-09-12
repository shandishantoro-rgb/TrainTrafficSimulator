from ttc.core.models import Project, Station, Train, TrainStatus


def make_sample_project() -> Project:
    stations = [
        Station("Gambir", "GMR", 400, 6, 16, "Daerah Operasi 1", "Stasiun utama Jakarta"),
        Station("Jatinegara", "JNG", 300, 8, 11, "Daerah Operasi 1", "Stasiun persilangan utama"),
        Station("Bekasi", "BKS", 300, 8, 19, "Daerah Operasi 1", "Stasiun komuter"),
    ]
    trains = [
        Train("KA 1", "Argo Bromo Anggrek", "Antarkota", TrainStatus.BERJALAN, "Gambir – Jatinegara", "Surabaya Pasarturi", 72, 0),
        Train("KA 3", "Taksaka", "Antarkota", TrainStatus.BERJALAN, "Jatinegara – Bekasi", "Yogyakarta", 65, 2),
        Train("KA 8", "KRL Commuter Line", "KRL", TrainStatus.BERHENTI, "Jatinegara", "Manggarai", 0, 0),
        Train("KA 12", "Bangkawalan", "Lokal", TrainStatus.BERJALAN, "Cipinang – Jatinegara", "Jatinegara", 44, 1),
        Train("KA 15", "Joglosemarkerto", "Antarkota", TrainStatus.BERJALAN, "Bekasi – Cikarang", "Cikarang", 78, 0),
    ]
    return Project(name="Demo Jabodetabek", stations=stations, trains=trains)
