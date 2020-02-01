import re
import subprocess

class RbsCalculator:
    def __init__(self): # Add more parameters
        self.dG_start = {"AUG": -1.194,
            "GUG": -0.0748,
            "UUG": -0.0435, 
            "CUG":-0.03406} # Taken from https://github.com/hsalis/Ribosome-Binding-Site-Calculator-v1.0/blob/master/RBS_Calculator.py 
        self.rRNA = 'ACCUCCUUA"'
    
    def fold_rna(self,RNA:str) -> float:
        return float(subprocess.check_output('echo {} | LinearFold/./linearfold --verbose | grep -F "Energy(kcal/mol):" | cut -d ":" -f2'.format(RNA),shell=True).decode('utf-8'))
        
    def dG_tot(self,mRNA_pre:str,mRNA_post:str) -> float:
        # Calculate dG_mRNA_rRNA
        dG_mRNA_rRNA = 1

        # Calculate dG_mRNA
        dG_mRNA = self.fold_rna(mRNA_pre+mRNA_post)

        # Calculate dG_start
        dG_start = self.dG_start[mRNA_post[0:3]]

        # Calculate dG_spacing
        dG_spacing = 1

        # Calculate dG_standby
        dG_standby = 1


        return (dG_mRNA_rRNA + dG_start + dG_spacing - dG_standby) - dG_mRNA

    def calculate_rbs(mRNA:str) -> float: # Runs additional sanity checks
        # Check if mRNA sequence
        mRNA = mRNA.replace('T','U')
        if re.search(mRNA, "^[AUGC]*$") is None:
            raise ValueError('Not an mRNA sequence')



