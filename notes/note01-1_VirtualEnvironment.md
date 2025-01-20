# What is Virtual environment?

A virtual environment is a named, isolated, working copy of Python that that maintains its own files, directories, and paths so that you can work with specific versions of libraries or Python itself without affecting other Python projects.

# Why do I care?

* Python is evolving fast.
* Python’s third-party packages are evolving really fast too.
* Different versions are not always compatible.
* You don't want to mess up the default Python in your computer system.

## Scenario 1

* The versions of Python and packages you used in a project may be out of date after a while.
* If you update the Python and packages, your previous code may not work under new version (Damn!).

## Scenario 2

* Your project A uses Python 3.6 and package a (v1.2)
* Your project B uses Python 3.8 and package a (v2.2)
* You can’t use the default Python on your computer system, as well as other packages, which are set to be a certain version.
  ![image](https://miro.medium.com/max/493/1*YB6YkrefMAj7MRn8nzrvXQ.png)

## Scenario 3

* Your co-worker is working on a project and he is using an Python version that is different from yours.
* He/she sent the project to you to ask for collaboration.
* The codes may not work.

## Scenario 4

* Ever wondered why your code works on your laptop fine, but not on your desktop?

## and more ...

# Fix

* To fix this, you can use a **virtual environment tool** to produce easily sharable virtual environment files.
* Eeach virtual environment can be conceptualized as a separate box where you have the desired Python version and the required packages for your project.
* These boxes are separate such that what you do in one project won’t affect other projects.
* It’s always recommended that you create distinct virtual environments for your projects.

# Setup Virtual Environment

Although there are many options to use, **Conda** and **Venv** are environment managers that are most popular and widely used. Here, we will use the first option. Setting up virtual environment using Venv can be found [here](https://realpython.com/python-virtual-environments-a-primer/).

**Note**: the codes in the following should be typed in:

* Anaconda Prompt (Windows)
* Terminal (Mac and Linux)

## Creating virtual environments

First, check out existing virtual environments

```shell
conda env list
```

You should see only one virtual environment called *base* if you use Anaconda.

Now, we show several ways to create a virtual environment.

### 1. Building a new virtual environments

```shell
conda create -n my_venv python=3.9.7
```

The above code create an virtual environment called *my_venv* with Python version 3.9.7

### 2. Creating a virtual environment by cloning

```shell
conda create -n my_venv_clone --clone my_venv
```

### 3. Creating a virtual environment from a YAML file

```shell
conda env create -n my_venv_3 -f environment.yml
```

## Install specific versions of packages in virtual environments

You can use `conda` or `pip`. `pip` is the Python Packaging Authority’s
recommended tool for installing packages from the Python Package Index
([PyPI](https://pypi.org/)).

* `conda` is an environment and package and
  management system. It install packages from the [Anaconda
  repository](https://repo.anaconda.com/).
* [PyPI](https://pypi.org/) contains more
  Python packages, while `conda` can package and distribute software for any
  language.
* If you use `conda` to setup your python virtual evnironment, use `conda` to
 install python packages unless it is not available from the Anaconda repository.

```shell
conda install matplotlib=3.7.1
```

```shell
pip install matplotlib==3.7.1
```

## Activating virtual environments

After the above creation, we have new virtual environments. Using `conda
 env list` you can see the new names. The environment that has asterisk
 indicates the active environment we are in. This means we are still in the base
 environment. To use the newly created virtual environment, we need to activate
 it

```shell
conda activate my_venv
```

Try `shell conda env list` again to see the effect.

## Exporting environment specifications to YAML file

We can check the specifications of the current environment with:

```shell
conda list
```

This will show environment details such as Python version used, package names
installed and their versions. To export the specifications of the current
environment into a YAML file into the current directory, we can use one of the
commands below:

```shell
conda env export -f environment.yml
```

You can use the option `--from-history` to include only the manually installed packages.

```shell
conda env export --from-history -f environment.yml
```

## Deactivating virtual environments

Once you are done using the virtual environment, if you want to switch back to
the base environment, you can use one of the following to deactivate the
environment:

```shell
conda deactivate
```

## Removing virtual environment

After you know you no longer need the virtual environment, you can delete it
using the following code (**make sure to it is deactivated first**):

```shell
conda env remove -n my_venv
```

```shell
conda env remove -n my_venv_clone
```

## Rename a virtual environment

  * To rename a virtual environment, use

```shell
conda rename -n old_name new_name
```


## Set up for jupyter notebook

1. create a new virtual environment

```shell
conda create -n stat2255 python=3.12.4
```

2. activate the virtual environment

```shell
conda activate stat2255
```

3. Install ipykernel and jupyter

```shell
# conda install -c anaconda ipykernel
conda install jupyter
```

<!-- 4. Update to notebook 7 -->

<!-- ```shell -->
<!-- pip install jupyter notebook --upgrade -->
<!-- ``` -->

4. Now you can start notebook

```shell
jupyter notebook
```

In case Jupyter notebook does not load correctly in you browser, you can try the three different ways of accessing the it given from the commend line output. It should looks like this:

```shell
    To access the server, open this file in a browser:
        file:///home/ossifragus/.local/share/jupyter/runtime/jpserver-306254-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/tree?token=79fbaa927aec8dfc33c71e15cbc70b086fd63d4d66d4ecf6
        http://127.0.0.1:8888/tree?token=79fbaa927aec8dfc33c71e15cbc70b086fd63d4d66d4ecf6
```

<!-- 4. Add the stat2255 kernel in jupyter -->

<!-- ```shell -->

<!-- python -m ipykernel install --user --name=stat2255 -->

<!-- ``` -->

<!-- 5. To remove the kernel  -->

<!-- ```shell -->

<!-- jupyter kernelspec uninstall stat2255 -->

<!-- ``` -->

## Reference

[https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28](https://towardsdatascience.com/introduction-to-conda-virtual-environments-eaea4ac84e28)

[https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

[https://python.plainenglish.io/virtual-environments-1d09041771d](https://python.plainenglish.io/virtual-environments-1d09041771d)

[https://towardsdatascience.com/beginner-friendly-virtual-environment-management-anaconda-pycharm-36178e20129f](https://towardsdatascience.com/beginner-friendly-virtual-environment-management-anaconda-pycharm-36178e20129f)
