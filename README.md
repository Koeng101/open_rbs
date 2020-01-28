# RBS strength calculation

RBS calculation takes 5 basic parameters:

1. dG-mRNA:rRNA
2. dG-start
3. dG-spacing
4. dG-standby
5. dG-mRNA

`dG_tot = (dG-mRNA:RNA + dG-start + dG-spacing - dG-standby) - dG-mRNA`

## dG-mRNA:rRNA
Idea: capture the energy in the basepairing between mRNA RBS and the SD sequence in the rRNA. This is energy gained by the system during ribosome assembly on the mRNA due to rRNA recognition. This captures (roughly) the "strength" of an RBS (as measured by gene expression).

Implementation: Use NuPACK to calculate energy of rRNA binding to mRNA.

## dG-start
Idea: capture the energy in the binding of the met-tRNA to the start codon. Non-optimal binding (GTG instead of ATG) will affect translation rate.

Implementation: Use a premade table from Howard Salis's work.

## dG-spacing
Idea: capture the energy that is necessary to overcome non-optimal spacing between the start codon and the RBS. 

Implementation: Calculate where the rRNA binds to the mRNA, then use a premade table from Howard Salis's work to turn spacing into dG.

## dG-standby
Idea: capture the energy lost by unfolding the mRNA sequence upstream of the SD sequence, which the authors call the "standby sequence" and is located 4 bp upstream of the SD. The folding of the standby sequence inhibits the ribosome from physically accessing the SD region on the mRNA, and thus the strength of folding in the standby sequence negatively effects expression.

## dG-mRNA
Idea: capture the energy in the basepairing between the mRNA on itself. mRNA folding on itself competes with rRNA binding to it, and will lower translation rates.

Implementation: Use NuPACK to calculate energy of mRNA binding to itself.

