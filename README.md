# reprobe: tool for re-annotating probe

## installation

```
pip install reprobe
```

## Usage

### use as commandline tool

```
reprobe_bowtie \
    -p <PROBE_SEQUENCES_FILE> \
    -i <INDEX> \
    -o <RESULT>
```

2. `-p`: probe sequences file
4. `-i`: bowtie index path
6. `-o`: output file path

### use as Python library

```python
from reprobe.reprobers import BowtieReprober


reprober = BowtieReprober()
result = reprober.reprobe(probe_sequences_file='xxx', index='xxx')
```