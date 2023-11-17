# Module QC Database Tools v2.2.2rc0

The package to regisiter ITkPixV1.1 modules, and generate YARR configs from ITk
production database using `itkdb` API.

## Set-Up and First-time Installation

A minimum of python version 3.7+ is required.

### Virtual Python Environment

Python virtual environment only needs to be created once and used throughout all
module QC tools.

Creating a python virtual environment the standard way used the python version
available on the operating system. For CentOS 7 this is version 3.6. If using
CentOS 7, you can either install python 3.8 following these
[instructions](https://tecadmin.net/install-python-3-8-centos/) (needs `sudo`),
or use [anaconda](https://docs.anaconda.com/anaconda/install/index.html) or
[miniconda](https://docs.conda.io/en/latest/miniconda.html) (see below).

After installing python 3.8, create the virtual environment outside any git
repo. `<venv>` can be substituted with any descriptive name:

```
$ python3 -m venv <venv>
$ source <venv>/bin/activate
```

For future use, activate the virtual environment like instructed below, or add
this line to your `~/.bashrc`:

```
$ source <venv>/bin/activate
```

#### Anaconda or Miniconda

Alternatively, [anaconda](https://docs.anaconda.com/anaconda/install/index.html)
or [miniconda](https://docs.conda.io/en/latest/miniconda.html) also provides a
higher python version and do not require python installation on the Linux
system. They can also be installed following the instructions in the links.

For future use, activate the virtual environment like instructed below, or add
this line to your `~/.bashrc`:

```
$ conda activate
```

### Install

```
$ python -m pip install module-qc-database-tools
```

### Environment Variables

If not already set elsewhere (e.g. `~/.bashrc`), copy `.env.template` to `.env`
and update the values of the shell variables. Essentially, the following
variables regarding the production database should be available, shown below as
an example of environmental variables in `~/.bashrc`:

```bash
export INSTITUTION="LBNL_PIXEL_MODULES"
export ITKDB_ACCESS_CODE1="accesscode1"
export ITKDB_ACCESS_CODE2="accesscode2"
```

## Module registration

Under construction...

## Generate YARR configuration

This script has been tested on python 3.7+.

To generate YARR configuration for a given module, run `generateYARRConfig` or
`mqdbt generate-yarr-config`:

```
$ generateYARRConfig -sn [ATLAS SN] -o [outdir]
$ mqdbt generate-yarr-config -sn [ATLAS SN] -o [outdir]

Parameters:
-sn, --sn, required=True: ATLAS serial number of the module
-ch, --chipTemplate, default="configs/YARR/chip_template.json": provide the path of a chip config template to generate the new chip configs from
-o, --outdir, path to output directory config folder will be placed in. If not supplied, the config files will be pushed into mongoDB if connection is set up.
-f, --fast, fast generation of configs files without any linebreaks.
--noeos, Do not use eos token.
--reverse, Use reversed order of chip ID, e.g. for old L0 linear triplets.
```

For example, to generate the YARR configs for the module `20UPGR91301046` with
all power configs:

```
$ generateYARRConfig -sn 20UPGR91301046 -o ~/module_data/.
$ mqdbt generate-yarr-config -sn 20UPGR91301046 -o ~/module_data/.
```

The time needed to generate warm and cold L2 configs for a quad module is about
4 seconds.
