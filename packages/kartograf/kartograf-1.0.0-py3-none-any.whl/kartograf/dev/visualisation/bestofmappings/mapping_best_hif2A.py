import time
import pymol
from pymol import cmd

pymol.finish_launching()

import pymol_utils as pu

pu.openfe_colors()

file_path = '/home/riesbenj/Code/OpenFE/openfe-benchmarks/openfe_benchmarks/data/hif2a_ligands.sdf'

def std_surface():
    cmd.set("transparency_mode", 3)
    cmd.set("surface_quality",5)
    cmd.set("ambient", 0.85)
    cmd.set("direct", 0.25)
    cmd.set("reflect", 0.0)
    cmd.set("backface_cull", 0)
    cmd.set("solvent_radius", 0.3)
    cmd.set("stick_radius", 0.1)



def reinit():
    cmd.reinitialize()
    time.sleep(1)
    pu.openfe_colors()
    time.sleep(1)
    std_surface()
    cmd.bg_colour("white")


time.sleep(1)
cmd.window(action="maximize")
time.sleep(1)

cmd.load(file_path, "benz")
cmd.split_states("benz")
cmd.delete("benz")

#cmd.set("retain_order", 1)
cmd.color("grey60", "elem C")
cmd.bg_colour("white")



def draw_mapping(state_A, state_B, mapping, ):
    #Clean
    cmd.hide()
    cmd.disable("all")

    # Start:
    cmd.enable(state_A)
    cmd.enable(state_B)

    cmd.color("lightblue", "elem C and " + state_A)
    cmd.color("darksalmon", "elem C and " + state_B)

    cmd.show("sticks")
    cmd.set("sphere_transparency", 0.2)
    cmd.set("sphere_scale", 0.35)

    colors = [k for k in pu.ofe_color_dict]
    for i, (maA, maB) in enumerate(mapping.items()):
        print("(",maA, maB, ")", "(", maA+1, maB+1, ")")
        c= colors[i%len(colors)]
        selA = state_A+" and id "+str(maA+1)
        selB = state_B+" and id "+str(maB+1)

        cmd.show("spheres", selA)
        cmd.show("spheres", selB)

        cmd.set("sphere_color", c, selA)
        cmd.set("sphere_color", c, selB)

cmd.set("grid_mode", 0)
time.sleep(1)


# Ring Re-Alignment
state_A = "lig_163"
state_B = "lig_124"
out_prefix = "hif2a_re_alignment_1"

view = [0.581673563,    0.584961474,   -0.565220833,
     0.564392447,    0.210145995,    0.798308551,
     0.585759759,   -0.783362448,   -0.207909569,
     0.000000000,    0.000000000,  -35.295707703,
    24.068984985,   -0.339787960,  -10.189199448,
     7.499221802,   63.092189789,  -20.000000000]
cmd.set_view(view)


if (False):
    mapping =     {2: 22, 4: 21, 5: 23, 6: 8, 7: 7, 8: 6, 9: 28, 10: 29, 11: 30, 12: 31, 13: 1, 14: 0, 15: 2, 16: 3, 18: 4, 19: 5, 20: 9, 21: 10, 22: 11, 23: 12, 24: 13,
                   25: 14, 26: 16, 27: 15, 28: 17, 29: 18, 30: 20, 31: 19}

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap3d_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap3d_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap3d_" + out_prefix + "_mapped_overlap")

    #cmd.hide("spheres")
    #pu.make_picture("lomap3d_" + out_prefix + "_overlap")

    time.sleep(1)


if (False):
    mapping =     {10: 5, 14: 0, 19: 29, 21: 10, 23: 12, 29: 18, 30: 20, 31: 19, 4: 21, 5: 23, 6: 8, 7: 7, 8: 6, 9: 4, 11: 2, 12: 3, 13: 1, 15: 30, 16: 31, 18: 28, 20: 9, 22: 11, 24: 13, 25: 14, 26: 16, 27: 15, 28: 17}

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("kartograf_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("kartograf_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("kartograf_" + out_prefix + "_mapped_overlap")

    cmd.hide("spheres")
    pu.make_picture("kartograf_" + out_prefix + "_overlap")

    time.sleep(1)

