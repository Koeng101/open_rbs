import re

class RbsCalculator:
    def __init__(self): # Add more parameters
        self.dG_start = {"AUG": -1.194,
            "GUG": -0.0748,
            "UUG": -0.0435, 
            "CUG":-0.03406} # Taken from https://github.com/hsalis/Ribosome-Binding-Site-Calculator-v1.0/blob/master/RBS_Calculator.py 

    def dG_tot(self,mRNA:str) -> int:
        # Calculate dG_mRNA_rRNA
        dG_mRNA_rRNA = 1

        # Calculate dG_mRNA
        dG_mRNA = 1

        # Calculate dG_start
        dG_start = 1

        # Calculate dG_spacing
        dG_spacing = 1

        # Calculate dG_standby
        dG_standby = 1


        return (dG_mRNA_rRNA + dG_start + dG_spacing - dG_standby) - dG_mRNA

    def calculate_rbs(mRNA:str) -> int: # Runs additional sanity checks
        # Check if mRNA sequence
        mRNA = mRNA.replace('T','U')
        if re.search(mRNA, "^[AUGC]*$") is None:
            raise ValueError('Not an mRNA sequence')

