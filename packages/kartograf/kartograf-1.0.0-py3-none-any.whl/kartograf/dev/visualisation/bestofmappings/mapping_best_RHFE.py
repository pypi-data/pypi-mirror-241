import time
import pymol
from pymol import cmd

pymol.finish_launching()

import pymol_utils as pu

pu.openfe_colors()

file_path = "/home/riesbenj/Code/OpenFE/Experiments/setups/mappers/Kartograf/theory/benz_oH.sdf"


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

#aliphatics
state_A = "lig_1"
state_B = "lig_3"
out_prefix = "aliphatic_aromatic"


view = [
     0.985486031,   -0.046392597,   -0.163286507,
    -0.009717439,    0.944930673,   -0.327122062,
     0.169471189,    0.323959857,    0.930767834,
     0.000000000,    0.000000000,  -24.021314621,
     0.675092220,   -0.212792397,    0.105792284,
    11.992041588,   36.050594330,  -20.000000000
]
cmd.set_view(view)

##2D Lomap Mapping
if(False):
    mapping = {0: 0, 1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 6: 8, 7: 10}

    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap2D_"+out_prefix+"_"+state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap2D_"+out_prefix+"_"+state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap2D_"+out_prefix+"_mapped_overlap")

    cmd.hide("spheres")
    pu.make_picture("lomap2D_"+out_prefix+"_overlap")

    time.sleep(1)

##Kartograf mapping
if(False):
    mapping = {1: 7, 2: 6, 4: 10, 5: 3, 6: 4, 7: 5}

    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("kartograf_"+out_prefix+"_"+state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("kartograf_"+out_prefix+"_"+state_B)

    cmd.enable(state_A)
    pu.make_picture("kartograf_"+out_prefix+"_mapped_overlap")

    cmd.hide("spheres")
    pu.make_picture("kartograf_"+out_prefix+"_overlap")


# Bad Alignment
state_A = "lig_10"
state_B = "lig_5"
out_prefix = "bad_alignment"

view = [ 0.985486031,   -0.046392597,   -0.163286507,
    -0.009717439,    0.944930673,   -0.327122062,
     0.169471189,    0.323959857,    0.930767834,
    -0.000002226,    0.000006451,  -30.573804855,
     0.788973093,   -1.633970976,   -0.373573571,
    18.544658661,   42.603229523,  -20.000000000]
cmd.set_view(view)

##2D Lomap Mapping
if(False):
    mapping = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6,  8: 15, 9: 10, 10: 8, 11:7, 7:16 }

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap_" + out_prefix + "_mapped_overlap")

    #cmd.hide("spheres")
    #pu.make_picture("lomap_" + out_prefix + "_overlap")

    time.sleep(1)

##Kartograf mapping
if(False):
    mapping = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 6: 6, 11:7}

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

# re-Alignment
state_A = "lig_1"
state_B = "lig_5"
out_prefix = "re_alignment_1"

view = [0.985486031, -0.046392597, -0.163286507,
        -0.009717439, 0.944930673, -0.327122062,
        0.169471189, 0.323959857, 0.930767834,
        -0.000002226, 0.000006451, -30.573804855,
        0.788973093, -1.633970976, -0.373573571,
        18.544658661, 42.603229523, -20.000000000]
cmd.set_view(view)

##2D Lomap Mapping
if (False):
    mapping = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 7, 7: 6}

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap2D_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap2D_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap2D_" + out_prefix + "_mapped_overlap")

    # cmd.hide("spheres")
    # pu.make_picture("lomap2D_" + out_prefix + "_overlap")

    time.sleep(1)

##2D Lomap Mapping
if (False):
    mapping = {1: 0, 2: 1, 3: 7, 4: 6, 5: 4, 6: 3, 7: 2}

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap3D_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap3D_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap3D_" + out_prefix + "_mapped_overlap")

    # cmd.hide("spheres")
    # pu.make_picture("lomap3D_" + out_prefix + "_overlap")

    time.sleep(1)

##Kartograf Mapping
if (False):
    mapping = {1: 0, 2: 1, 3: 7, 4: 6, 5: 4, 6: 3, 7: 2}

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


# re-Alignment
state_A = "lig_11"
state_B = "lig_5"
out_prefix = "re_alignment_2"

view = [0.985486031, -0.046392597, -0.163286507,
        -0.009717439, 0.944930673, -0.327122062,
        0.169471189, 0.323959857, 0.930767834,
        -0.000002226, 0.000006451, -30.573804855,
        0.788973093, -1.633970976, -0.373573571,
        18.544658661, 42.603229523, -20.000000000]
cmd.set_view(view)

##Kartograf Mapping
if (False):
    mapping ={0: 9, 1: 8, 2: 7, 3: 6, 4: 16, 5: 17, 6: 15, 7: 10}

    cmd.sort(state_A)
    draw_mapping(state_A, state_B, mapping)

    cmd.disable("all")
    cmd.enable(state_A)
    pu.make_picture("lomap2D_" + out_prefix + "_" + state_A)

    cmd.disable("all")
    cmd.enable(state_B)
    pu.make_picture("lomap2D_" + out_prefix + "_" + state_B)

    cmd.enable(state_A)
    pu.make_picture("lomap2D_" + out_prefix + "_mapped_overlap")

    cmd.hide("spheres")
    pu.make_picture("lomap2D_" + out_prefix + "_overlap")

    time.sleep(1)

if (True):
    mapping ={0: 0, 1: 1, 2: 7, 3: 6, 4: 4, 5: 5, 6: 3, 7: 2}

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

    #cmd.hide("spheres")
    #pu.make_picture("kartograf_" + out_prefix + "_overlap")

    time.sleep(1)