# mapGL
## Prediction of lineage-specific gain and loss of genomic sequence elements based on phylogenetic maximum parsimony.

Label genomic regions as orthologous, gained in the query species, or lost in
the target species, based on inferred presence/absence in the most-recent
common ancestor (MRCA). Chained alignment files are used to map features from
query to target and one or more outgroup species. Features that map directly from
query to target are labeled as orthologs, and ortholgous coordinates in the
target species are given in the output. Non-mapping features are assigned as
gains or losses based on a maximum-parsimony algorithm predicting presence
or absence in the MRCA.

Based on bnMapper.py, by Ogert Denas (James Taylor lab):
  * https://github.com/bxlab/bx-python/blob/master/scripts/bnMapper.py
  * https://travis-ci.org/bxlab/bx-python

## Dependencies
numpy
Cython
six

## Usage

```mapGL.py [-h] [-o FILE] [-t FLOAT] [-g GAP] [-v {info,debug,silent}] [-k] input tree qname tname alignments [alignments ...] ```

## Required Arguments

  | Argument | Description |
  |---|---|
  | __input__ | Input regions to process. Should be in standard bed format. Only the first four bed fields will be used. |
  | __tree__ | Phylogenetic tree describing relationships of query and target species to outgroups. Must be in standard Newick format. Branch lengths are optional, and will be ignored. |
  | __qname__ | Name of the query species. Regions from this species will be mapped to target species coordinates. |
  | __tname__ | Name of the target species. Regions from the query species will be mapped to coordinates from this species. |
  | __alignments__ | Alignment files (.chain or .pkl): One for the target species and one per outgroup species. Files should be named according to the convention: qname.tname[...].chain.gz, where qname is the query species name and tname is the name of the target/outgroup species. Names used for qname and tname must match names used in the phylogenetic tree. |

## Options

  | Option | Description |
  |---|---|
  | __-h, --help__ | Show help message and exit. |
  | __-o FILE, --output FILE__ | Output file. (default: stdout) |
  | __-t FLOAT, --threshold FLOAT__ | Mapping threshold i.e., (elem * threshold) <= mapped_elem (default: 0.0) |
  | __-g GAP, --gap GAP__ | Ignore elements with an insertion/deletion of this or bigger size. (default: -1) |
  | __-v {info,debug,silent}, --verbose {info,debug,silent}__ | Verbosity level (default: info) |
  | __-d, --drop_split__ | Follow the bnMapper convention of silently dropping elements that span multiple chains, rather than the liftOver mapping convention for split alignments: keep elements that span multiple chains and report the longest aligned segment. This is not recommended, as it may lead to spurious gain/loss predictions for orthologous elements that happen to be split across chains due to chromosomal rearrangements, etc... (default: False) |
  | __-i {BED,narrowPeak}, --in_format__ {BED,narrowPeak} | Input file format. (default: BED) |

## Output

Predictions are reported in tab-delimited format with the first four columns following the BED4 convention. The predicted evolutionary history (i.e., ortholog, gain in query, or loss in target) is reported in the "status" column. The final three columns contain the mapped location, in target coordinates, of mapped (ortholog) elements.

| Column | Description |
|---|---|
| __chrom__ | Chromosome on which the query element is located. |
| __start__ | Start position on query chromosome. |
| __end__ | End position on query chromosome. |
| __name__ | Element name or ID. |
| __peak__ | Peak location (narrowPeak input) or element midpoint (BED input) |
| __status__ | Predicted phylogenetic history: __ortholog__, __gain_qname__, or __loss_tname__ |
| __mapped chrom__ | For mapped (ortholog) elements, the chromosome on which the mapped element is located, in target coordinates. |
| __mapped start__ | For mapped (ortholog) elements, the start position on the target chromosome on which the mapped element is located. |
| __mapped end__ | For mapped (ortholog) elements, the end position on the target chromosome on which the mapped element is located. |
| __mapped_peak__ | For mapped (ortholog) elements, the mapped peak position (narrowPeak input) or mapped element midpoint (BED input). |

Copyright 2018, Adam Diehl (adadiehl@umich.edu), Boyle Lab, University of Michigan
