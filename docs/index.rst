MELODIES-MONET
==============

**MELODIES-MONET** is a joint project between NCAR and NOAA to develop a modular framework 
that integrates existing and future diverse atmospheric chemistry observational datasets 
with chemistry model results for the evaluation of air quality and atmospheric composition.
MELODIES-MONET combines the Model EvaLuation using Observations, DIagnostics and Experiments
Software (MELODIES) project at NCAR with the Model and ObservatioN Evaluation Toolkit (MONET)
project at NOAA to develop a python diagnostic package that is open source, generic, portable,
and model-agnostic. Overall, the project provides a framework for evaluating a wide range of
models in a more consistent manner. The tool is accessible to everyone including university
and national laboratory researchers, as well as graduate students and postdocs.

The goal is to evaluate research, operational, and regulatory models against a variety of 
observations including surface, aircraft and satellite data all within a common framework. 
MELODIES-MONET uses the functionality already developed by MONETIO to read in multiple 
observational and model datasets and MONET to do pairing/analysis/plotting. For more 
information on MONET and MONETIO github repositories please refer to:
 
- https://monet-arl.readthedocs.io
- https://monetio.readthedocs.io


.. note::
   If you use MELODIES-MONET, please use the following citations:

   - Baker, Barry; Pan, Li. 2017. “Overview of the Model and Observation Evaluation Toolkit (MONET) Version 1.0 for Evaluating Atmospheric Transport Models.” Atmosphere 8, no. 11: 210

   - TBD - An NCAR Technote?


.. warning::
   MELODIES-MONET has not yet been released, please contact the development team prior to using the plots for publication.

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Background and Setup

   background/introduction
   background/description
   background/installation
   background/getting-started
   background/supported-datasets
   background/viewing-output
   background/under-development
   background/contributing


.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Capabilities and Examples

   examples/regional_ts


.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Test Suite

   testsuite/unit_tests
   testsuite/data_tests
   testsuite/analysis_tests


.. toctree::
   :maxdepth: 1
   :caption: Help and Reference

   api
   tutorial/machine-specific-install


