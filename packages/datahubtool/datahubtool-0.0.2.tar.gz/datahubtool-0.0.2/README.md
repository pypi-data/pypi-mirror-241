# DatahubTool

[![PyPI - Version](https://img.shields.io/pypi/v/datahubtool)](https://pypi.org/project/datahubtool/)
[![DOI](https://zenodo.org/badge/719921081.svg)](https://zenodo.org/doi/10.5281/zenodo.10150399)

<img src="https://github.com/lbj2011/DatahubTool/blob/main/doc_img/duramat_logo.png" width="200"/>

Toolkit for batch management of data in [DuraMAT Datahub](https://datahub.duramat.org/), like upload and delete.

NOTE: only **authorised users** (API Key required, shown on user page of Datahub) can manage its owned project data in Datahub. 


## Installation
```
pip install datahubtool
```

## Package overview
Here's a high level overview of the important functions of the package.

- 'get_local_file_names': Get the names of local files to upload in a given path
- 'get_Datahub_file_names': Get all existing files's name in a given package in Datahub
- 'upload_files': Upload files to Datahub
- 'delete_Datahub_files': Delete files in Datahub


## Authors
Baojie Li (LBNL)