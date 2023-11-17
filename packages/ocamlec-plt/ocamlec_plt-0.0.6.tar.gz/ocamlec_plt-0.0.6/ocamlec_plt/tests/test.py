#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:30:02 2023

@author: mariohevia
"""

import ocamlec_plt
import ocamlec_plt.coevolution

ocamlec_plt.utils.setGeccoRules()
experiment_path = "./results/"
output_path = "./"
paths = ocamlec_plt.utils.getPaths(experiment_path)

for path in paths:
    ocamlec_plt.coevolution.champions.plotChampions(file_path=path, title="", legend_key="sel_function", file_name=output_path+"oclcoea_champs.pdf")