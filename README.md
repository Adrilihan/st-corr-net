# Graph representation of interactions for spatio-temporal data

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This repo was the result of the final project of the curriculum unit [Time and Spatial Econometrics](https://www.ua.pt/en/uc/15124) where the objective was to create a graph-based representation of the interactions between spatio-temporal data with the intent of improving and/or justifying the definition of the neighboring matrix that is commonly used in spacial analysis [^1].

To showcase the methodology HIV/AIDS infection data across the African continent [^2] was chosen as a case study where the following weighted graph was obtained.

<p align="center">
  <img 
    style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 50%;
           height: 50%;"
    src="https://github.com/user-attachments/assets/eca6c1e7-f913-4b6e-a9d5-4327fe915c7b" 
    alt="Graph representation of spatial correlations in HIV infection rates in Africa from 1990 to 2019.">
</p>

where

- **Nodes** represent countries.
- **Edges** represent spatial correlations in HIV infection rates from 1990 to 2019.
- **Weights** quantify the strength of correlation.

With such graph it's possible to visually indentify clusters of correlation and define a cut-off value to descard the connection iproving the definition of the neighboring matrix that can be used for instance with VAR models.

The methodology is applicable beyond epidemiology, with potential use cases in economics, environmental modeling, and other domains involving spatially distributed time series.

## Data Sources

- Archived time series data for HIV infections from [Our World in Data – HIV/AIDS](https://web.archive.org/web/20240604204632/https://ourworldindata.org/grapher/deaths-and-new-cases-of-hiv)

- African countries geometries from [RCRMD Open Data Portal – Africa Countries Dataset](https://opendata.rcmrd.org/datasets/rcmrd::africa-countries-dataset/about)

## Setup

To run this project, you need to have the following tools installed:

- Anaconda
- Make

> [!NOTE]
> A VSCode `settings.json` file with Anaconda terminal profile was created for easier use yet it assumes you installed the **Miniconda** version.  
> If you installed the **Anaconda distribution**, you’ll need to manually change the default terminal to the Anaconda one.

The environment is created by running in the Anaconda terminal:

```sh
make create_enviroment
```

To fetch the data, run:

```sh
conda activate st-corr-net
make data
```

With that, the notebooks should be runnable

## Project Organization

```
├── LICENSE            <- License file
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         st_corr_net and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── environment.yml    <- The requirements file for reproducing the analysis environment.
│
└── st_corr_net   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes st_corr_net a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

## References

[^1]: Sergio J. Rey, Dani Arribas-Bel, and Levi J. Wolf (2023) — “Geographic Data Science with Python” Published online at GeographicData.Science. Retrieved from: '<https://geographicdata.science/book/intro.html>' [Online Resource]

[^2]: Max Roser and Hannah Ritchie (2023) - “HIV / AIDS” Published online at OurWorldInData.org. Retrieved from: '<https://web.archive.org/web/20240604204631/https://ourworldindata.org/hiv-aids>' [Online Resource]

