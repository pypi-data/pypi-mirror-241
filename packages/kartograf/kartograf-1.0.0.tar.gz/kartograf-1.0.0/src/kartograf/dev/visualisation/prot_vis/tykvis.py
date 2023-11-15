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

protein_path = '/home/riesbenj/Code/OpenFE/openfe-benchmarks/openfe_benchmarks/data/tyk2_old_protein.pdb'
ligands_path = '/home/riesbenj/Code/OpenFE/openfe-benchmarks/openfe_benchmarks/data/tyk2_old_ligands.sdf'

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

cmd.set_view([0.413438112,    0.531763673,    0.739119828,
    -0.910140157,    0.217502117,    0.352616549,
     0.026748074,   -0.818490684,    0.573901653,
    -0.000017077,    0.000149138, -183.322357178,
    -5.773821354,   16.303249359,  -25.987199783,
   141.423095703,  225.215759277,  -20.000000000])

make_picture("tyk2_overview.png")

cmd.set_view([     0.493184596,    0.627412677,    0.602597356,
    -0.793012202,    0.039472200,    0.607926369,
     0.357634515,   -0.777690291,    0.517011046,
    -0.000082269,    0.000186792,  -49.186103821,
    -3.683972359,   22.692491531,  -29.718978882,
     7.284318924,   91.077033997,  -20.000000000 ])

cmd.show("sticks", "byres lig_ejm_31 around 5.0")
cmd.hide("sticks", "elem H")

make_picture("tyk2_close.png")

cmd.set_view([0.421581000,   -0.450693935,    0.786857843,
    -0.827147841,   -0.546740413,    0.130004555,
     0.371615976,   -0.705653906,   -0.603289843,
    -0.000114491,    0.000066349,  -70.139770508,
    -4.605390549,   24.690153122,  -30.676511765,
    28.245510101,  112.038261414,  -20.000000000])

cmd.disable("protein")
cmd.set("grid_mode")
make_picture("tyk2_ligands.png")

