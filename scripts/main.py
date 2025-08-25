#!/usr/bin/env python3
import glob
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

from rope.base.project import Project
from rope.refactor.move import create_move


class CodeCleaner:
    def __init__(
        self,
        input_file,
        specifications,
        types_folder,
        resources_folder,
        enums_folder,
        collections_folder,
    ):
        with open(specifications, "r") as file:
            self.json_data = json.loads(file.read())
        self.specifications = specifications
        self.project = Project("..", ropefolder=None)
        self.types_files = [
            f for f in listdir(types_folder) if isfile(join(types_folder, f))
        ]
        self.resources_files = [
            f for f in listdir(resources_folder) if isfile(join(resources_folder, f))
        ]
        self.enums_files = [
            f for f in listdir(enums_folder) if isfile(join(enums_folder, f))
        ]
        self.collections_files = [
            f
            for f in listdir(collections_folder)
            if isfile(join(collections_folder, f))
        ]

        with open(input_file, "r") as file:
            input_data = file.read()
            self.wip = self.project.root.create_file("icar/wip.py")
            self.wip.write(input_data)

        self.resources_module = self.project.root.create_file("icar/resources.py")
        self.types_module = self.project.root.create_file("icar/types.py")
        self.enums_module = self.project.root.create_file("icar/enums.py")
        self.collections_module = self.project.root.create_file("icar/collections.py")
        self.geojson_module = self.project.root.create_file("icar/geojson.py")
        self.others_module = self.project.root.create_file("icar/others.py")
        self.module_map = {}

    def clean(self):
        self.map_files()

        while True:
            data = self.wip.read()
            lookup = "\nclass "
            index = data.rfind(lookup)
            if index == -1:
                break
            index = index + len(lookup)
            class_name = data[index:].split("(", 1)[0]
            destination = self.get_destination_module(class_name)
            print(f"{class_name} --> {destination.name}")
            mover = create_move(
                self.project,
                self.wip,
                index,
            )
            self.project.do(mover.get_changes(destination))

        self.close()
        self.convert_to_relative_imports()

    def get_destination_module(self, class_name):
        destination = self.module_map.get(class_name)

        if destination:
            return destination

        if class_name.endswith("Event"):
            return self.resources_module
        if class_name.endswith("Array") or class_name in {"BatchResults", "View"}:
            return self.collections_module

        if class_name in {
            "Coordinate",
            "Type",
            "Type1",
            "Type2",
            "Type3",
            "Type4",
            "Type5",
            "Geometry",
            "Geometry1",
            "Geometry2",
            "Geometry3",
            "Geometry4",
            "Geometry5",
            "Geometry6",
        }:
            return self.geojson_module
        return self.others_module

    def map_files(self):
        self.map_modules(self.enums_module, self.enums_files)
        self.map_modules(self.types_module, self.types_files)
        self.map_modules(self.resources_module, self.resources_files)
        self.map_modules(self.collections_module, self.collections_files)

    def close(self):
        self.project.close()
        os.remove("../icar/wip.py")

    def convert_to_relative_imports(self):
        for filepath in glob.iglob("../icar/*.py"):
            with open(filepath) as file:
                s = file.read()
            s = s.replace("from icar import", "from . import")
            with open(filepath, "w") as file:
                file.write(s)

    def map_modules(self, destination, files):
        for file in files:
            no_extension = Path(file).stem
            capitalize = no_extension[0].capitalize() + no_extension[1:]
            self.module_map[capitalize] = destination


if __name__ == "__main__":
    for f in glob.iglob("../icar/*.py"):
        if os.path.exists(f) and not f.endswith("__init__.py"):
            os.remove(f)
    code_cleaner = CodeCleaner(
        input_file="../tmp/raw_models.py",
        specifications="../ICAR-schema/bundled-schemes/combinedURLScheme.json",
        types_folder="../ICAR-schema/types",
        resources_folder="../ICAR-schema/resources",
        enums_folder="../ICAR-schema/enums",
        collections_folder="../ICAR-schema/collections",
    )
    code_cleaner.clean()
