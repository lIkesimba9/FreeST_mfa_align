# MFA train align for FreeST dataset

## Data

put [FreeST](https://openslr.elda.org/resources/38/ST-CMDS-20170001_1-OS.tar.gz) dataset to data/

## Prerequisites

* Docker: 20.10.7

## Usage

```bash
docker build --rm --tag aligner .
docker run --rm -it -v $(pwd):/aligner aligner
```

Processed data will be located at `data/processed/mfa_outputs` (as `.TextGrid`, grouped by speaker IDs) and `data/processed/mels` (as `.pkl`, grouped by speaker IDs).

