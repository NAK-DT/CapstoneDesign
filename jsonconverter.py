import shutil
import os
import json
import re
from ast import parse
from ast2json import ast2json

dir_path = "https://github.com/NAK-DT/CapstoneDesign.git"
regex = r'(?<!: )"(\S*?)"'

# create the AST and save it in a .json file
def createAst(file, filename, dest_dir):
    """docstring"""
    ast = ast2json(parse(open(file).read()))
    jsonString = re.sub(regex, '\\1', json.dumps(ast, indent=4))
    jsonFile = open(dest_dir + "/%s.json" % filename, "w")
    jsonFile.write(jsonString)
    jsonFile.close()

for subfolder in next(os.walk(dir_path))[1]:
    print("Going through: " + subfolder)
    for file in os.listdir(os.path.join(dir_path, subfolder)):
        try:
            createAst(file=os.path.join(os.path.join(dir_path, subfolder), file), filename=os.path.splitext(file)[0], dest_dir=os.path.join(dir_path, subfolder))
        except:
            continue

