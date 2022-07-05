\ Model model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  z
Subject To
 R0: bin_PaloAlto_LosAngeles_path_0 + bin_PaloAlto_LosAngeles_path_1 = 1
 R1: bin_PaloAlto_Denver_path_0 + bin_PaloAlto_Denver_path_1 = 1
 R2: bin_LosAngeles_PaloAlto_path_0 + bin_LosAngeles_PaloAlto_path_1 = 1
 R3: bin_LosAngeles_Denver_path_0 + bin_LosAngeles_Denver_path_1 = 1
 R4: bin_Denver_PaloAlto_path_0 + bin_Denver_PaloAlto_path_1 = 1
 R5: bin_Denver_LosAngeles_path_0 + bin_Denver_LosAngeles_path_1 = 1
 qc0: [ PaloAlto_LosAngeles_path_0 * bin_PaloAlto_LosAngeles_path_0
   + PaloAlto_LosAngeles_path_1 * bin_PaloAlto_LosAngeles_path_1 ] = 0
 qc1: [ PaloAlto_Denver_path_0 * bin_PaloAlto_Denver_path_0
   + PaloAlto_Denver_path_1 * bin_PaloAlto_Denver_path_1 ] = 0
 qc2: [ LosAngeles_PaloAlto_path_0 * bin_LosAngeles_PaloAlto_path_0
   + LosAngeles_PaloAlto_path_1 * bin_LosAngeles_PaloAlto_path_1 ] = 0
 qc3: [ LosAngeles_Denver_path_0 * bin_LosAngeles_Denver_path_0
   + LosAngeles_Denver_path_1 * bin_LosAngeles_Denver_path_1 ] = 0
 qc4: [ Denver_PaloAlto_path_0 * bin_Denver_PaloAlto_path_0
   + Denver_PaloAlto_path_1 * bin_Denver_PaloAlto_path_1 ] = 0
 qc5: [ Denver_LosAngeles_path_0 * bin_Denver_LosAngeles_path_0
   + Denver_LosAngeles_path_1 * bin_Denver_LosAngeles_path_1 ] = 0
Bounds
Binaries
 bin_PaloAlto_LosAngeles_path_0 bin_PaloAlto_LosAngeles_path_1
 bin_PaloAlto_Denver_path_0 bin_PaloAlto_Denver_path_1
 bin_LosAngeles_PaloAlto_path_0 bin_LosAngeles_PaloAlto_path_1
 bin_LosAngeles_Denver_path_0 bin_LosAngeles_Denver_path_1
 bin_Denver_PaloAlto_path_0 bin_Denver_PaloAlto_path_1
 bin_Denver_LosAngeles_path_0 bin_Denver_LosAngeles_path_1
End
