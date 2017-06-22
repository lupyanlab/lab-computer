# Installing psychopy with conda on Windows

This works on Windows 10 64-bit. This installation method uses pygame for playing sound files. pyo is preferred, but it is only available for 32-bit python, and even then, it is tricky to install.

1. Install Anaconda.
2. Create a new conda environment.

```bash
conda create -n psychopy python=2
```

3. Activate the new environment.

```bash
activate psychopy
```

4. Install conda depedencies.

```bash
conda install numpy scipy matplotlib pandas pyopengl pillow lxml openpyxl xlrd configobj pyyaml gevent greenlet msgpack-python psutil pytables requests seaborn
```

5. Install external dependencies.

```bash
conda install -c conda-forge pyglet
conda install -c cogsci pygame
```

6. Install pip dependencies.

```bash
pip install moviepy pyosf python-bidi psychopy_ext
```

7. Install psychopy with pip.

```bash
pip install psychopy
```

# Installing from environment file.

To get a psychopy environment set up from scratch, you can download the environment file.

```bash
git clone https://github.com/lupyanlab/labcomputer.git
cd labcomputer
conda env create -f psychopy-environment.yml
```
