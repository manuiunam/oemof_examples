from pathlib import Path
from IPython.display import Image, display
from oemof.visio import ESGraphRenderer


def plot_energy_system(energysystem):

    output_path = Path("temp_energy_system")

    renderer = ESGraphRenderer(
        energysystem,
        filepath=str(output_path),
        img_format="png",
        legend=True
    )

    renderer.render()

    display(Image(filename=f"{output_path}.png"))


import graphviz