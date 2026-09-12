from PySide6.QtCore import Qt, QRectF, QPointF
from PySide6.QtGui import QColor, QPen, QBrush, QFont, QPainter
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsTextItem


class NetworkView(QGraphicsView):
    """Kanvas jaringan sederhana untuk UI shell TTC v0.1."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setScene(self._build_scene())
        self.setBackgroundBrush(QBrush(QColor("#101822")))

    def _build_scene(self) -> QGraphicsScene:
        scene = QGraphicsScene(self)
        scene.setSceneRect(QRectF(0, 0, 1450, 720))

        grid_pen = QPen(QColor("#1e2a38"), 1)
        for x in range(0, 1451, 40):
            scene.addLine(x, 0, x, 720, grid_pen)
        for y in range(0, 721, 40):
            scene.addLine(0, y, 1450, y, grid_pen)

        title = scene.addText("TTC")
        title.setDefaultTextColor(QColor("#ffffff"))
        title.setFont(QFont("Arial", 30, QFont.Bold))
        title.setPos(36, 28)
        subtitle = scene.addText("Train Traffic Simulator")
        subtitle.setDefaultTextColor(QColor("#cbd5e1"))
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setPos(40, 72)

        self._label(scene, "Jakarta  ←", 60, 330, 13, True)
        self._label(scene, "Gambir", 325, 230, 12, True)
        self._label(scene, "Jatinegara", 790, 230, 12, True)
        self._label(scene, "Cikarang  →", 1215, 330, 13, True)

        rail_pen = QPen(QColor("#d7dee8"), 3)
        secondary_pen = QPen(QColor("#7f8da0"), 2)
        platform_brush = QBrush(QColor("#455368"))

        ys = [300, 340, 380, 420]
        for y in ys:
            scene.addLine(100, y, 1320, y, rail_pen)

        scene.addRect(285, 316, 240, 10, brush=platform_brush)
        scene.addRect(285, 396, 240, 10, brush=platform_brush)
        scene.addRect(735, 316, 250, 10, brush=platform_brush)
        scene.addRect(735, 396, 250, 10, brush=platform_brush)

        for x in (220, 560, 660, 1030, 1120):
            scene.addLine(x, 300, x + 70, 340, secondary_pen)
            scene.addLine(x, 420, x + 70, 380, secondary_pen)

        for x, y, color in [
            (250, 300, "#40c463"), (535, 340, "#e34f4f"), (690, 380, "#e6b94d"),
            (1000, 300, "#40c463"), (1180, 420, "#e34f4f")
        ]:
            scene.addEllipse(x, y - 6, 12, 12, QPen(Qt.NoPen), QBrush(QColor(color)))

        self._train(scene, "KA 1", 360, 286, "#2e7be6")
        self._train(scene, "KA 12", 435, 366, "#31a354")
        self._train(scene, "KA 3", 610, 406, "#d9485f")
        self._train(scene, "KA 8", 845, 326, "#d8a824")

        slogan = self._label(scene, "Membangun Operasi Kereta di Indonesia", 930, 55, 16, True)
        slogan.setDefaultTextColor(QColor("#f4f7fb"))
        scene.addLine(930, 92, 1240, 92, QPen(QColor("#d9232e"), 3))
        return scene

    @staticmethod
    def _label(scene, text, x, y, size=11, bold=False) -> QGraphicsTextItem:
        item = scene.addText(text)
        item.setDefaultTextColor(QColor("#dfe7ef"))
        item.setFont(QFont("Arial", size, QFont.Bold if bold else QFont.Normal))
        item.setPos(x, y)
        return item

    def _train(self, scene, text, x, y, color):
        scene.addRoundedRect(x, y, 76, 24, 4, 4, QPen(Qt.NoPen), QBrush(QColor(color)))
        item = scene.addText(text)
        item.setDefaultTextColor(QColor("white"))
        item.setFont(QFont("Arial", 9, QFont.Bold))
        item.setPos(x + 12, y + 2)

    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
            self.scale(factor, factor)
            event.accept()
            return
        super().wheelEvent(event)
