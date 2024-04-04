import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys

class CompassPlotWidget(QWidget):
    """
    Widget displaying a compass plot with a red data point.
    """

    def __init__(self, parent=None):
        """
        Initializes the widget and creates the compass plot.
        """
        super(CompassPlotWidget, self).__init__(parent)

        # Create layout
        layout = QVBoxLayout(self)

        # Configure plot
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

        # Define data
        theta = 90  # Compass bearing in degrees
        theta = 360 - theta - 180

        # Add data point
        ax.plot(np.radians(theta), 7, marker='s', markersize=15, markerfacecolor='red', zorder=2)

        # Set axis limits and ticks
        ax.set_rmax(12)  # Adjusted the maximum radial limit
        ax.set_rticks([1, 3, 6, 9, 12])
        ax.set_rlabel_position(-22.5)
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)

        # Enable grid and adjust appearance
        ax.grid(True, linestyle='--', alpha=0.7, zorder=0)

        # Set title and labels
        #ax.set_title("Compass Plot with Distance Ticks", va='bottom')
        #ax.set_xlabel('Compass Bearing')
        #ax.set_ylabel('Distance (m)')

        # Set background color to dark green
        ax.set_facecolor('darkgreen')

        # Create graphics scene
        scene = QGraphicsScene(self)

        # Initialize FigureCanvas with fig
        canvas = FigureCanvas(fig)
        canvas.draw()
        pixmap = canvas.grab()

        # Add pixmap to graphics scene
        scene_item = scene.addPixmap(pixmap)

        # Create graphics view
        view = QGraphicsView(scene)

        # Add widgets to layout
        layout.addWidget(view)

        # Set layout
        self.setLayout(layout)


# Create and run the event loop after initializing the QApplication
app = QApplication(sys.argv)

# Create and show the widget
widget = CompassPlotWidget()
widget.show()

# Run the event loop
sys.exit(app.exec_())
