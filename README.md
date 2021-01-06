# Atom Type Analysis.
01-06-21

This repo will contain the steps that can be used to analyze a gmso structure, and identify the forcefield applied to it.

Contains an example using networkx structures to visualize the bond and atom types of an acetic acid molecule.

To run this notebook, create and activate a conda environment with the following open source packages that are up to date:
mbuild, foyer, and gmso.
These can be found on conda-forge, or are availabe at https://github.com/mosdef-hub

To create an environment use:
conda create --name Atom_Type python=3.6 mbuild foyer jupyter py3dmol matplotlib
conda activate Atom_Type

Then, clone a copy of gmso from https://github.com/mosdef-hub/gmso:
cd gmso
pip install -r requirements.txt
pip install -e .

Finally:
jupyter notebook

And the notebook should work as intended.

Email nicholas.c.craven@vanderbilt.edu for help and questions.
