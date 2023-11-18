==========
genomicspy
==========


.. image:: https://img.shields.io/pypi/v/genomicspy.svg
        :target: https://pypi.python.org/pypi/genomicspy

.. image:: https://img.shields.io/travis/vivianleung/genomicspy.svg
        :target: https://travis-ci.com/vivianleung/genomicspy

.. image:: https://readthedocs.org/projects/genomicspy/badge/?version=latest
        :target: https://genomicspy.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Tools for manipulating vcfs doing genomics work


Features
=========



Classes:
---------

* ``Chunk``: for handling chunks of vcfpy.Record objects
* ``Saver``: to save Chunks and vcfpy.Record objects

Types:
-------

* ``SeqType``
  

Methods and constants:
-----------------------

allele_msa:  multiple sequence alignments operations

* ``find_read_msas``
* ``gen_variants_df``
* ``parse_alignments``


alleles:  manipulating and filling in alleles and variants

* ``combine_ivrs_variants``
* ``calc_circular``
* ``calc_end_pos``
* ``calc_ivrs``
* ``check_overlap``
* ``gen_alleles_for_chrom_vcf``
* ``gen_alleles_from_variants_df``


alleles2fastas:  converting allele data to fasta sequences

* ``check_fasta_seq_coverage``
* ``get_seqlen``
* ``infer_entry_name``
* ``read_alleles_gts_from_variants``
* ``read_alleles_gts_from_vcf``
* ``write_fasta_seq``


regions:  reading and parsing GFF3 and region-feature info

* ``consolidate_gff3``
* ``parse_gff3``
* ``select_regions``
* ``GFF3_COLS``


trim:  trim alleles or sequences

* ``trim_alleles``
* ``trim_allele_seqs``


vcf:  read VCFs

* ``get_entry_data``
* ``parse_records_generator``
* ``VCF_COLS``
* ``VCF_DEFAULT_DICT``




* Free software: MIT license
* Documentation: https://genomicspy.readthedocs.io.


Credits
--------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
