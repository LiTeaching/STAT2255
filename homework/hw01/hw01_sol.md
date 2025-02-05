```python

```


# Problem 1 (homework1)


## Commands to setup the virtual environment

1.  Create and activate the virtual environment named \`homework1\`
    
    ```shell
    conda create -n homework1 python=3.11.9
    conda activate homework1
    ```

2.  Install Jupyter 1.0.0.
    
    ```shell
    conda install jupyter=1.0.0
    ```

3.  Install the package \`matplotlib\` version 3.7.1
    
    ```shell
    conda install matplotlib==3.7.1
    ```

4.  Start \`jupyter notebook\`
    
    ```shell
    jupyter notebook
    ```


## Run the codes in Jupyter notebook

```python
import platform
platform.python_version()
```

```python
import notebook
notebook.__version__
```

```python
import matplotlib
matplotlib.__version__
```


# Problem 2 (stat2255)


## Commands to setup the virtual environment

1.  Create and activate \`stat2255\` from environment.yml.
    
    ```shell
    conda env create -n stat2255 -f environment.yml
    conda activate stat2255
    ```

2.  Start \`jupyter notebook\`.
    
    ```shell
    jupyter notebook
    ```

3.  Run the codes.


## Run the codes in Jupyter notebook

```python
import platform, notebook, matplotlib, pandas, scipy, statsmodels, seaborn, numpy

print('Python version: ', platform.python_version())
print('Jupyter notebook version: ', notebook.__version__)
print('Matplotlib version: ', matplotlib.__version__)
print('Pandas version: ', pandas.__version__)
print('Scipy version: ', scipy.__version__)
print('Statsmodels version: ', statsmodels.__version__)
print('Seaborn version: ', seaborn.__version__)
print('Numpy version: ', numpy.__version__)
```
