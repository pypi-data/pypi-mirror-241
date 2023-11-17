Installation
============

Requirements
------------

dew_gwdata relies on some specific Python packages to be installed in order to
work. Most of these will install themselves automatically using the Python package manager
program pip.

However, some of the prerequisite packages (geopandas, rasterio and pyodbc) cannot be 
installed on Windows
by this method. The simplest way to install these is via the package
manager conda (or mamba if you have that installed). To do so,
run this in Command Prompt:

.. code-block:: none

    conda install -c conda-forge geopandas rasterio pyodbc 

(Substitute ``mamba`` for ``conda`` if you have mamba installed - if you don't know
what the difference is, disregard this!)

You will also need to install the minimum required version of a private DEW WSM Python
package called ``sageodata_db``:

.. parsed-literal:: 

    pip install -U "P:\\Projects_GW\\State\\Groundwater_Toolbox\\Python\\wheels\\sageodata_db-\ |sageodata_db_version|\ -py3-none-any.whl"

Installing dew_gwdata
---------------------

You can install this package by running the following command in Command Prompt:

.. parsed-literal:: 

    pip install -U "P:\\Projects_GW\\State\\Groundwater_Toolbox\\Python\\wheels\\dew_gwdata-\ |version|\ -py3-none-any.whl"

.. note:: 

    Wheel distributions of private DEW Water Science Python packages like this are stored at this network
    location: ``P:\Projects_GW\State\Groundwater_Toolbox\Python\wheels``. The code itself is stored
    on GitHub under the ``dew-waterscience`` organisation account: https://github.com/dew-waterscience.
    You can join by sending an email with your GitHub username to Kent.Inverarity@sa.gov.au.
    
