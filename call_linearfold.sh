cat LinearFold/testseq | LinearFold/./linearfold --verbose | grep -F "Energy(kcal/mol):" | cut -d ':' -f2
