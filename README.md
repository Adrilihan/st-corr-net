
# Graph representation of interactions for spatio-temporal data

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

## Installation

The project uses conda so after cloning the repo you just need to replicate the enviroment with

```pwsh
conda env create -f environment.yml
```

the notebook where the graph representation is created is the `Africa_HIV.ipynb`. The name of the data files should be `deaths-and-new-cases-of-hiv.csv` and `Africa_Countries_Dataset.geojson` for the [Our World in Data – HIV/AIDS](https://web.archive.org/web/20240604204632/https://ourworldindata.org/grapher/deaths-and-new-cases-of-hiv) and [RCRMD Open Data Portal – Africa Countries Dataset](https://opendata.rcmrd.org/datasets/rcmrd::africa-countries-dataset/about) respectively.

## References

[^1]: Sergio J. Rey, Dani Arribas-Bel, and Levi J. Wolf (2023) — “Geographic Data Science with Python” Published online at GeographicData.Science. Retrieved from: '<https://geographicdata.science/book/intro.html>' [Online Resource]

[^2]: Max Roser and Hannah Ritchie (2023) - “HIV / AIDS” Published online at OurWorldInData.org. Retrieved from: '<https://web.archive.org/web/20240604204631/https://ourworldindata.org/hiv-aids>' [Online Resource]

