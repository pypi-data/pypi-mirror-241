# bodo_jupyterlab

![Github Actions Status](https://github.com/Bodo-inc/jupyterlab-extensions.git/workflows/Build/badge.svg)

A JupyterLab extension for use on the Bodo Cloud Platform.

The extension has two components: a frontend component (see files in `src`) and a server component (see files in `bodo_jupyterlab`).

## Requirements

- JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install bodo_jupyterlab
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall bodo_jupyterlab
```

## Contributing

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

You also need to first install our fork of remote-ikernel: https://github.com/Bodo-inc/remote_ikernel

```bash
sudo chown bodo:bodo -R /opt
# Make sure you have nodejs installed.
# If you don't have mamba installed: conda install -c conda-forge mamba.
mamba install -c conda-forge nodejs=16.12
# Clone the repo to your local environment
# Install package in development mode
pip install -e .
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Rebuild extension Typescript source after making changes
jlpm run build
# Enable it
jupyter server extension enable bodo_jupyterlab
jupyter lab extension enable bodo_jupyterlab
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm run watch
# Run JupyterLab in another terminal
jupyter lab
```

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm run build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
pip uninstall bodo_jupyterlab
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `bodo-jupyterlab` within that folder.

### Packaging the extension

See [RELEASE](RELEASE.md)
