# PBS-builder

A simplified version of workflow management system for scalable data analysis.

# Change log

- Version 0.4.7: consistent behaviour in mu02 and mu04
- Version 0.4.6: add suport for escape character in variable names
- Version 0.4.5: add progress bar and verbose output options
- Version 0.4.4: add elapsed time for each job
- Version 0.4.3: add support for non-BIOLS machines
- Version 0.4.2: integrate `pushover` service
- Version 0.4.1: auto-switch to corresponding pbs_server for qbatch
- Version 0.4.0: merge qcancel into qbatch commands, change API
- Version 0.3.1: add allocated/total gpus in `pestat` output
- Version 0.3.0: include `pestat` in package data
- Version 0.2.0: move `sample_sheet` from header to job section, add `group_sheet` support.
- Version 0.1.0: first functional version.

# Usage

`pbs-builder` include the following commands:

1. [`qbatch`](https://bioinfo.biols.ac.cn/git/zhangjy/pbs-builder/wiki/01.qbatch+-+building+automated+and+reproducible+pipelines)for batch submission of TORQUE/SLURM jobs

2. [`pestat`](https://bioinfo.biols.ac.cn/git/zhangjy/pbs-builder/wiki/02.pestat+-+monitor+node+status) for monitoring cluster & nodes status 

3. [`pushover`](https://bioinfo.biols.ac.cn/git/zhangjy/pbs-builder/wiki/03.pushover+-+get+nofications+from+compute+nodes+using+Pushover+service) for get noficiations from compute nodes

Please refer to our [wiki](https://bioinfo.biols.ac.cn/git/zhangjy/pbs-builder/wiki/_pages) for detailed instructions.

# Installation

pbs-builder runs in **python3.7+** with the `tomli` package installed, no other dependencies are required.

Install pbs-builder using the following command:

```bash
pip install pbs-builder
```
