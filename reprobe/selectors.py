# -*- coding: utf-8 -*-
from pathlib import Path


class Maps:
    def __init__(self):
        self.data = {}

    def add(self, probe_id, gene_id):
        self.data[probe_id] = gene_id

    def probe_ids(self):
        return self.data.keys()

    def gene_ids(self):
        return self.data.values()

    def probe_id_to_gene_id(self):
        return self.data.items()

    def __getitem__(self, probe_id):
        return self.data[probe_id]

    def save(self, file):
        if isinstance(file, str):
            file = Path(file)
        with file.open('w') as fp:
            fp.write('Probe_ID\tGene_ID\n')
            for probe_id, gene_id in self.probe_id_to_gene_id():
                fp.write(f'{probe_id}\t{gene_id}\n')


class Selector:
    def select(self, matches, index):
        raise NotImplementedError


class BowtieSelector(Selector):
    def select(self, matches, index):
        maps = Maps()
        for probe_id, gene_ids in matches.probe_id_to_gene_ids():
            maps.add(probe_id, index.parse_gene_id(gene_ids[0]))
        return maps
