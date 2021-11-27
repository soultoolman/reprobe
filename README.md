# reprobe: tool for re-annotating probe

## installation

```
pip install reprobe
```

## Usage

```python
from reprobe import BowtieReprober


reprober = BowtieReprober()
result = reprober.reprobe(
    probe_sequences_file='xxx',
    index='xxx'
)
```

GENCODE sequences contains multiple gene IDs,
If your bowtie index build from GENCODE sequences,
you should use GencodeIndex explicitly.

```python
from reprobe import GencodeIndex, BowtieReprober


reprober = BowtieReprober()
result = reprober.reprobe(
    probe_sequences_file='xxx',
    index=GencodeIndex('xxx')
)
```

Sequences have up to 2 mismatches were considered as match in `reprobe`,
if you want change to 3 mismatches, you can:


```python
from reprobe import GencodeIndex, BowtieReprober

reprober = BowtieReprober()
result = reprober.reprobe(
    probe_sequences_file='xxx',
    index=GencodeIndex('xxx'),
    mismatches=3
)
```
