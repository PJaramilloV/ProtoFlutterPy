from functools import partial 
import os

project_path = os.path.dirname(__file__)
project_dir = os.path.basename(project_path)
safe_path_partial = partial(os.path.join, project_path)

def safe_path_to(*args):
    return safe_path_partial(*args)