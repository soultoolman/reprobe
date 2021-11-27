# -*- coding: utf-8 -*-
import tempfile
from pathlib import Path

import sh


class Matches:
    def __init__(self):
        self.data = {}

    def add(self, probe_id, gene_id):
        if probe_id in self.data:
            self.data[probe_id].append(gene_id)
        else:
            self.data[probe_id] = [gene_id]

    def probe_ids(self):
        return self.data.keys()

    def probe_id_to_gene_ids(self):
        return self.data.items()

    def __getitem__(self, probe_id):
        return self.data[probe_id]


class MatchReader:
    def read(self, file):
        raise NotImplementedError


class BowtieMatchReader(MatchReader):
    @staticmethod
    def add_line(line, matches):
        temp = line.rstrip().split('\t')
        matches.add(temp[0], temp[2])

    def read(self, file):
        matches = Matches()
        if isinstance(file, str):
            file = Path(file)
        with file.open() as fp:
            for line in fp:
                self.add_line(line, matches)
        return matches


class Aligner:
    def align(self, probe_sequences_file, index):
        raise NotImplementedError


class BowtieAligner(Aligner):
    def __init__(self):
        self.command = sh.Command('bowtie')
        self.reader = BowtieMatchReader()

    def run_bowtie(self, mismatches, index, probe_sequences_file, result_file):
        mismatches = str(mismatches)
        index = str(index)
        probe_sequences_file = str(probe_sequences_file)
        result_file = str(result_file)
        self.command(
            '-f',
            '-v', mismatches,
            '--best',
            index,
            probe_sequences_file,
            result_file
        )

    def align(self, probe_sequences_file, index, mismatches=2):
        with tempfile.TemporaryDirectory() as tempdir:
            tempdir = Path(tempdir)
            result_file = tempdir / 'bowtie-result.txt'
            self.run_bowtie(
                mismatches,
                index,
                probe_sequences_file,
                result_file
            )
            return self.reader.read(result_file)
