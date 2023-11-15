import time
import numpy as np

import pymol
from pymol import cmd
pymol.finish_launching()

from pymol_utils import  make_picture, openfe_colors, ofe_color_dict

openfe_colors()


pymol.finish_launching()
time.sleep(1)

cmd.window(action="maximize")
time.sleep(1)

#OFE Style
color_resn1 = "Otherblue"
color_prot = "SandySergio" #Sergioscousin
color_out = "Beastlygrey"
color_map = "Feelingsick"

protein_path = '/home/riesbenj/Code/OpenFE/openfe-benchmarks/openfe_benchmarks/data/hif2a_protein.pdb'
ligands_path = '/home/riesbenj/Code/OpenFE/openfe-benchmarks/openfe_benchmarks/data/hif2a_ligands.sdf'

cmd.set("surface_quality", "2")
cmd.bg_colour("white")
cmd.set("dash_color", 'Feelingspicy')
cmd.load(ligands_path, "ligs")
cmd.split_states("ligs")
cmd.load(protein_path, "protein")

cmd.set("ray_shadow", 0)
cmd.delete("ligs")
time.sleep(1)



time.sleep(1)

cmd.hide()
k = list(filter( lambda x: x != color_prot, ofe_color_dict.keys()))
objs = cmd.get_object_list()
for i, obj in enumerate(objs):
    if(obj == "protein"):
        cmd.set("surface_color", color_prot, obj)
        cmd.set("transparency", 0.3)

        cmd.show("surface", "protein")
        cmd.show("cartoon")
    else:
        cmd.show("sticks", obj)
        cmd.color(k[i%len(k)], obj+" and elem C")

cmd.set_view([-0.779214203,   -0.484445035,    0.397670746,
     0.523400545,   -0.851992726,   -0.012328550,
     0.344789028,    0.198536873,    0.917444825,
    -0.000156403,    0.000047917, -183.326431274,
    16.534111023,   13.936614990,  -11.500465393,
   141.426025391,  225.218688965,  -20.000000000 ])

make_picture("hif2a_overview.png")


cmd.create("sys", "all")
cmd.disable("not sys")
cmd.show("surface", "polymer")
cmd.set("surface_color", color_prot, "sys")

cmd.set_view([ -0.937087715,    0.348106861,   -0.026049960,\
    -0.201353639,   -0.599970520,   -0.774264574,\
    -0.285155952,   -0.720311463,    0.632320225,\
     0.000147551,   -0.000147125,  -47.653507233,\
    22.639177322,    6.088852882,  -15.551014900,\
    36.254550934,   59.065616608,  -20.000000000  ])

cmd.show("sticks", "byres lig_1 around 5.0")
cmd.hide("sticks", "elem H")


make_picture("hif2a_close.png")


cmd.disable("all")
cmd.enable("lig*")
cmd.set_view([  0.981782496,   -0.034166031,    0.186885640,
    -0.023909105,    0.953648508,    0.299958020,
    -0.188473448,   -0.298963130,    0.935462475,
    -0.000237204,    0.000052579,  -40.429862976,
    25.553447723,    0.175751925,   -3.513679028,
    35.243511200,   58.772827148,  -20.000000000])

cmd.disable("protein")
cmd.set("grid_mode")
make_picture("hif2a_ligands.png")
