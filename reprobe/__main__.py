# -*- coding: utf-8 -*-
import click

from .reprobers import BowtieReprober


@click.command()
@click.option(
    '-p',
    '--probe-sequences-file',
    required=True,
    type=click.Path(exists=True),
    help='probe sequences file'
)
@click.option(
    '-i',
    '--index',
    required=True,
    help='bowtie index path'
)
@click.option(
    '-o',
    '--outfile',
    required=True,
    help='re-annotation result path'
)
def reprobe_bowtie(probe_sequences_file, index, outfile):
    """reprobe using bowtie"""

    reprober = BowtieReprober()
    maps = reprober.reprobe(probe_sequences_file, index)
    maps.save(outfile)


if __name__ == '__main__':
    reprobe_bowtie()
