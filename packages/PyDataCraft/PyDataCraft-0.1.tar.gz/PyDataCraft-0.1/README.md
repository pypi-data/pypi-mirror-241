# PyDataCraft 

<p align="center">
  <img width="" height="200" src=''>
</p>

Python application to manipulate, convert & view different and different Scientific data.

**Inside the project folder (GPSconverter)/DATA you can find a "test_data" repository with inside files to test the applicative.**

## Installation

- **The best way** is create an ad-hoc environment using the anaconda environment function which I tailored to the main Operative System (OS) used. To download and install  with just one command all the packages needed including the installation of the GPSconverter application just run the command below after have downloaded the GPSconverter.yml file corrispective  [HERE](https://anaconda.org/CSammarco/GPSconverter/files) and related to your operative system (OS value written in the "TAG" parameter: Mac, Win and UNIX-tested on linux Ubuntu-) 

  ```
  conda env create -f GPSconverter.yml  
  ```

- Another way is to install the entire environment manually (which I called "myenv" in the example below). To do so please to run the code in the following order:

  ```
  conda create --name myenv (considere to use python>=3.8)
  ```

  Activate the environmet created above with:

  ```
  conda activate myenv
  ```

  Now time to install all the dependencies needed by following the order of the commands below:

  ```
  sudo apy get install gmt
  sudo apt get install cdo
  conda install -c conda-forge gmt geopandas 
  pip install GPSconverter
  ```

**No matter which path you followed, now you have all the packages needed instaled in your envirnment and the GPSconverter Application installed too!** 

**To run the application just type on your terminal/command-propt the following:**

```
PyDataCraft
```

At this point a GUI interface will pop up and you are ready to go!

<p align="center">
  <img width="" height="600" src="">
</p>

Enjoy! :)
