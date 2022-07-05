\ Model model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  z
Subject To
 R0: PaloAlto_LosAngeles_path_0 >= 0
 R1: PaloAlto_LosAngeles_path_1 >= 0
 R2: bin_PaloAlto_LosAngeles_path_0 + bin_PaloAlto_LosAngeles_path_1 = 1
 R3: PaloAlto_Denver_path_0 >= 0
 R4: PaloAlto_Denver_path_1 >= 0
 R5: bin_PaloAlto_Denver_path_0 + bin_PaloAlto_Denver_path_1 = 1
 R6: LosAngeles_PaloAlto_path_0 >= 0
 R7: LosAngeles_PaloAlto_path_1 >= 0
 R8: bin_LosAngeles_PaloAlto_path_0 + bin_LosAngeles_PaloAlto_path_1 = 1
 R9: LosAngeles_Denver_path_0 >= 0
 R10: LosAngeles_Denver_path_1 >= 0
 R11: bin_LosAngeles_Denver_path_0 + bin_LosAngeles_Denver_path_1 = 1
 R12: Denver_PaloAlto_path_0 >= 0
 R13: Denver_PaloAlto_path_1 >= 0
 R14: bin_Denver_PaloAlto_path_0 + bin_Denver_PaloAlto_path_1 = 1
 R15: Denver_LosAngeles_path_0 >= 0
 R16: Denver_LosAngeles_path_1 >= 0
 R17: bin_Denver_LosAngeles_path_0 + bin_Denver_LosAngeles_path_1 = 1
 R18: z + PaloAlto_LosAngeles_path_0 + PaloAlto_Denver_path_1
   + Denver_LosAngeles_path_1 <= 1
 R19: z + LosAngeles_PaloAlto_path_0 + LosAngeles_Denver_path_1
   + Denver_PaloAlto_path_1 <= 1
 R20: z + PaloAlto_LosAngeles_path_1 + PaloAlto_Denver_path_0
   + LosAngeles_Denver_path_1 <= 1
 R21: z + LosAngeles_PaloAlto_path_1 + Denver_PaloAlto_path_0
   + Denver_LosAngeles_path_1 <= 1
 R22: z + PaloAlto_Denver_path_1 + LosAngeles_PaloAlto_path_1
   + LosAngeles_Denver_path_0 <= 1
 R23: z + PaloAlto_LosAngeles_path_1 + Denver_PaloAlto_path_1
   + Denver_LosAngeles_path_0 <= 1
 qc0: [ PaloAlto_LosAngeles_path_0 * bin_PaloAlto_LosAngeles_path_0
   + PaloAlto_LosAngeles_path_1 * bin_PaloAlto_LosAngeles_path_1 ]
   = 0.2951328498531105
 qc1: [ PaloAlto_Denver_path_0 * bin_PaloAlto_Denver_path_0
   + PaloAlto_Denver_path_1 * bin_PaloAlto_Denver_path_1 ]
   = 0.0767190361437367
 qc2: [ LosAngeles_PaloAlto_path_0 * bin_LosAngeles_PaloAlto_path_0
   + LosAngeles_PaloAlto_path_1 * bin_LosAngeles_PaloAlto_path_1 ]
   = 0.2413066014921761
 qc3: [ LosAngeles_Denver_path_0 * bin_LosAngeles_Denver_path_0
   + LosAngeles_Denver_path_1 * bin_LosAngeles_Denver_path_1 ]
   = 0.2628860761859587
 qc4: [ Denver_PaloAlto_path_0 * bin_Denver_PaloAlto_path_0
   + Denver_PaloAlto_path_1 * bin_Denver_PaloAlto_path_1 ]
   = 0.1190411219242894
 qc5: [ Denver_LosAngeles_path_0 * bin_Denver_LosAngeles_path_0
   + Denver_LosAngeles_path_1 * bin_Denver_LosAngeles_path_1 ]
   = 0.2708395996021846
Bounds
Binaries
 bin_PaloAlto_LosAngeles_path_0 bin_PaloAlto_LosAngeles_path_1
 bin_PaloAlto_Denver_path_0 bin_PaloAlto_Denver_path_1
 bin_LosAngeles_PaloAlto_path_0 bin_LosAngeles_PaloAlto_path_1
 bin_LosAngeles_Denver_path_0 bin_LosAngeles_Denver_path_1
 bin_Denver_PaloAlto_path_0 bin_Denver_PaloAlto_path_1
 bin_Denver_LosAngeles_path_0 bin_Denver_LosAngeles_path_1
End
