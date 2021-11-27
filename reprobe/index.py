# -*- coding: utf-8 -*-
from pathlib import Path


class Index:
    def __init__(self, path):
        if isinstance(path, str):
            path = Path(path)
        self.path = path

    def __repr__(self):
        return str(self.path)

    def parse_gene_id(self, raw_gene_id):
        return raw_gene_id


class GencodeIndex(Index):
    def parse_gene_id(self, raw_gene_id):
        return raw_gene_id.split('|')[5]
