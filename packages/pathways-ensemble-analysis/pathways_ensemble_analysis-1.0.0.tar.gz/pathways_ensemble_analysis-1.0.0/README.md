# Pathways Ensemble Analysis

## Overview and scope

The `pathways-ensemble-analysis` (short: `pea`) package allows you to perform multi-criteria evaluation style analyses of pathway ensembles produced by energy and climate models.

It has a range of functionality, including the ability to:

- Evaluate user-defined criteria for an ensemble of pathways - for example the share of renewables in 2050.
- Filter the ensemble on the basis of the defined criteria to identify a subset of pathways which is of particular interest - for example based on maximum sustainable levels of carbon dioxide removal.
- Rank pathways on the basis of these criteria by performing a multi-criteria evaluation of the ensemble.
- Visualise the evaluated and ranked criteria of the ensemble.


## What's Here
In this repo, there are the following folders and sets of files:

1. `src/pathways-ensemble-analysis`: contains the source code for the pea package. The definitions of the evaluation criteria are located in the `criteria` folder, with the `base` module providing more basic, general criteria, and the `library` module providing more specific, pre-defined criteria, as for example the average level of CCS/CDR deployment, biomass consumption, and the probability of overshooting 1.5°C.

2. `tests`: contains the unit testing scripts for the package, which can be run with `pytest`.

3. `notebooks`: contains an example notebook which shows how the pea package can be used to filter, rank and visualise a diverse set of pathways.

## Getting started

1. Clone this repository to your local machine.

2. Create an environment `pea` with the help of conda, by running

   ```
   conda env create -f environment.yml
   ```
3. Activate this environment via 

   ```
   conda activate pea
   ```

## Example
An example for how to use this package is given in the notebooks folder [here](https://gitlab.com/climateanalytics/model-dev-team/pathways-ensemble-analysis/-/tree/main/notebooks).

## Contributors
* Lara Welder (@l-welder) <lara.welder@climateanalytics.org>
* Neil Grant (@neilgrant) <neil.grant@climateanalytics.org>
* Jonas Hörsch (@coroa) <jonas.hoersch@climateanalytics.org>
* Tina Aboumahboub (@Tinaab) <tina.aboumahboub@climateanalytics.org>

## License
Copyright (C) 2022 Climate Analytics. All versions released under the [MIT License](https://opensource.org/licenses/MIT).

## Repository Organization

```
├── CONTRIBUTORS.md                   <- List of developers and maintainers.
├── CHANGELOG.md                      <- Changelog to keep track of new features and fixes.
├── LICENSE.txt                       <- License as chosen on the command-line.
├── README.md                         <- README file for the repository
├── environment.yml                   <- The conda environment file for reproducibility.
├── notebooks                         <- Jupyter notebooks.
├── setup.cfg                         <- Declarative configuration of your project.
├── setup.py                          <- Use `pip install -e .` to install.
├── src
│   └── pathways_ensemble_analysis  <- Actual Python package where the main functionality goes.
├── tests                             <- Unit tests which can be run with `pytest`.
├── .coveragerc                       <- Configuration for coverage reports of unit tests.
├── .gitignore                        <- Lists folders and files not tracked by git
├── .isort.cfg                        <- Configuration for git hook that sorts imports.
└── .pre-commit-config.yaml           <- Configuration of pre-commit git hooks.
```
