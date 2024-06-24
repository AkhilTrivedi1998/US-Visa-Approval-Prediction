import os
from pathlib import Path

project_name = "us-visa"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entitiy.py",
    f"{project_name}/entity/artifact_entitiy.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",

]

for filepath in list_of_files:
    filepath = Path(filepath) # gives the path based on the os. ex - the paths above uses '/' but wimdows path contain '\'. Path will do the conversion.
    filedir, filename = os.path.split(filepath) # splits the filepath into filename and directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # exit_ok ensures that if the directory already exists then makedirs doesn't do anything.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # 'with' helps us to efficiently close the file, once operations are complete within the 'with' block.
        with open(filepath, 'w') as f:
            pass
    else:
        print(f"File {filepath} already exists")