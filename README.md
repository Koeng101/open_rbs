
RBS calculation takes 5 basic parameters:

1. dG-mRNA:rRNA
2. dG-start
3. dG-spacing
4. dG-standby
5. dG-mRNA


## dG-mRNA:rRNA
Idea: capture the energy in the basepairing between mRNA RBS and the SD sequence in the rRNA. This is energy gained by the system during ribosome assembly on the mRNA due to rRNA recognition. This captures (roughly) the "strength" of an RBS (as measured by gene expression).

## dG-start
Idea: capture the energy in the binding of the met-tRNA to the start codon. Non-optimal binding (GTG instead of ATG) will affect translation rate.

## dG-spacing


## dG-standby
Idea: capture the energy lost by unfolding the mRNA sequence upstream of the SD sequence, which the authors call the "standby sequence" and is located 4 bp upstream of the SD. The folding of the standby sequence inhibits the ribosome from physically accessing the SD region on the mRNA, and thus the strength of folding in the standby sequence negatively effects expression.

## dG-mRNA
Idea: capture the energy in the basepairing between the mRNA on itself. mRNA folding on itself competes with rRNA binding to it, and will lower translation rates.
