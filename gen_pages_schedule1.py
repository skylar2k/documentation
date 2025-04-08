import json
from enum import Enum
from pathlib import Path
import mkdocs_gen_files
from jinja2 import Environment, FileSystemLoader


class EDrugTypes(Enum):
    Marijuana = 0
    Methamphetamine = 1
    Cocaine = 2
    MDMA = 3
    Shrooms = 4
    Heroin = 5


class ELegalStatus(Enum):
    Legal = 0
    ControlledSubstance = 1
    LowSeverityDrug = 2
    ModerateSeverityDrug = 3
    HighSeverityDrug = 4


def walk_json_files(path: str):
    for p in Path(path).iterdir():
        if p.is_dir():
            continue
        yield p


def load_json_file(path: Path):
    with open(path, "r") as f:
        content = json.load(f)
    return content


def generate_product_pages(env):
    template = environment.get_template("schedule1/product.j2")

    for j in walk_json_files("gen_pages/schedule1/products"):
        product = load_json_file(j)
        drug_type = EDrugTypes(product['DrugTypes'][0]['DrugType']).name
        filename = f"Reverse Engineering/Games/Schedule 1/Products/{drug_type}/{j.stem}.md"

        content = template.render({
            'product': product,
            'drug_type': drug_type,
            'legal_status': ELegalStatus(product["legalStatus"]).name
        })

        with mkdocs_gen_files.open(filename, "w") as f:
            f.write(content)

        mkdocs_gen_files.set_edit_path(filename, "gen_pages_schedule1.py")


environment = Environment(loader=FileSystemLoader("templates/"))
generate_product_pages(environment)
