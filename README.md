# ERDDAP-GenerateDatasets

There are three python scripts:
* concat_datasetsxml_WFP.py
* concat_datasetsxml_MOAS.py
* concat_datasetsxml_adcp.py. 

I wrote them to be run specifically in the order (WFP,MOAS,ADCP). 

The approach is to generate a basic xml element tree representing the datasets.xml file. Then populate it with a new datasets based on existing netcdf files. Once that is done, write the entire thing to a datasets.xml file.
