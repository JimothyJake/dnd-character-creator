from flask import Flask, render_template
from scripts import registry
import logging

app = Flask(__name__) 

REGISTRY = {
    "constants": {},
    "classes": {},
    "races": {},
    "features": {},
    "backgrounds": {},
    "items": {},
    "spells": {}
}

current_character = {
    "name": "",
    "character_level": 0,
    "race": {},
    "background": {},
    "classes": [{"": 0}]
}

# 2. Initialize Data
print("Loading registries...")
data_path = registry.build_paths()
registry.build_registries(data_path, REGISTRY)

@app.route("/")
def index():
    return render_template("builder.html", REGISTRY=REGISTRY)

if __name__ == "__main__":
    app.run(debug=True)