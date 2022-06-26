import os
import pathlib

RESOURCES_DIRECTORY = pathlib.Path(__file__).parent.resolve()
RESULTS_DIRECTORY = os.path.join(RESOURCES_DIRECTORY, "Results")
