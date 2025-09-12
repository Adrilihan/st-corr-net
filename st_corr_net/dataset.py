from functools import reduce
from pathlib import Path
import pooch

from loguru import logger
from tqdm import tqdm
import typer

import json
import pandas as pd

from st_corr_net.config import PROCESSED_DATA_DIR, EXTERNAL_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    logger.info("Downloading raw data...")

    variables = {
        "People living with HIV": 744591,
        "New HIV infections (cases)": 744590,
        "Deaths from HIV/AIDS": 758076
    }
    hashes = ("sha256:456c962f053a9a87a9464aff84a68612eb938ae205f93db9026507043a19bd38",
              "sha256:46e0123df1b13e57c65df39378df18d049b4667b99fdca9439ab9dc6971cbdf6",
              "sha256:8d0ac7b2b74b80e9dfee875fb9bf5c3d3321b92a5c655bd6a5f55e31b14f4411",
              "sha256:20c87f0d14ef67b6ae8730eed01cdc65cbdaf902cf78cdaefa3a50b06892cdc2",
              "sha256:a7ba2f46603b0d1f3c1de9ee970d1b1f9a586f4f43b0b3c07706161edb3312a8",
              "sha256:901609c8dff235abb9e1d1662a4279dc65a932de23be01eab4398ef63c33c15d",)

    i = 0   # index for hashes tuple
    registry = dict()
    for name, var_id in variables.items():
        for kind in ["data", "metadata"]:
            filename = f"{var_id}.{kind}.json"
            file_hash = hashes[i]
            registry[filename] = file_hash
            i += 1

    odie = pooch.create(
        path=RAW_DATA_DIR,
        base_url="https://web.archive.org/web/20240604204632/https://api.ourworldindata.org/v1/indicators",
        # The registry specifies the files that will be fetched
        registry=registry,
    )
    raw_file_paths = list(map(lambda x: odie.fetch(x, progressbar=True), registry.keys()))
    
    logger.success("Downloading raw data complete.")


    logger.info("Downloading external data (spatial)...")
    external_file_path = pooch.retrieve(
        url="https://services6.arcgis.com/zOnyumh63cMmLBBH/arcgis/rest/services/Africa_Countries/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson",
        known_hash="sha256:007596f84a52b0f7a33f3fd7108ce665fb3edc1c23189063eddf7b72e124ee33",
        fname="africa_countries.geojson",
        path=EXTERNAL_DATA_DIR,
        progressbar=True
    )
    
    logger.success("Downloading external data complete.")


    logger.info("Processing dataset...")
    # Carregar todos os dados
    data_frames = []
    for i in range(0, len(raw_file_paths), 2):
        # Files must be read in pairs: data + metadata
        df = pd.read_json(raw_file_paths[i])
        with open(raw_file_paths[i+1]) as f: metadata = json.load(f)
        md_df = pd.DataFrame(metadata["dimensions"]['entities']['values'])
        merged_df = pd.merge(df, md_df, left_on='entities', right_on='id')

        cols = merged_df.columns.tolist()
        new_order = ['name', 'code', 'years', 'values', 'entities']
        merged_df = merged_df[new_order]

        merged_df.columns = ['Entitie', 'Code', 'Year', metadata['name'], 'Id']
        data_frames.append(merged_df)

    final_df = reduce(lambda left, right: pd.merge(left, right, on=['Entitie', 'Code', 'Year', "Id"]), data_frames)

    final_df.pop('Id')
    final_df.to_csv(PROCESSED_DATA_DIR / 'deaths-and-new-cases-of-hiv.csv', index=False)

    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
