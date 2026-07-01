from pathlib import Path
import json
import logging

# Determine data directory
def build_paths():
    home_dir = Path(__file__).resolve().parent
    data_dir = home_dir.parent / "data"
    return data_dir

def build_registries(data_dir, target_registry):
    for category in target_registry.keys():
        category_path = data_dir / category
        
        # Handle folders
        if category_path.is_dir():
            target_registry[category] = {}
            for item_folder in category_path.iterdir():
                if item_folder.is_dir():
                    # Load all .json files in folder
                    item_data = {}
                    for json_file in item_folder.glob("*.json"):
                        logging.info("Loading {json_file.stem} from {item_folder}")
                        item_data[json_file.stem] = load_data(json_file)
                    target_registry[category][item_folder.name] = item_data
        # Handle files in data_dir
        else:
            file_path = data_dir / f"{category}.json"
            if file_path.exists():
                target_registry[category] = load_data(file_path)
                logging.info("Loading {file_path.stem}")

    return target_registry    

# Load SRD data from a JSON file
def load_data(filename):
    with open(filename) as file:
        return json.load(file)