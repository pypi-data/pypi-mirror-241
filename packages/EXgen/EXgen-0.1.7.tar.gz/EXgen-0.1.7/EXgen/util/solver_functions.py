from typing import List
import numpy as np
import matplotlib.pyplot as plt
from lcapy import Circuit
import EXgen.util.expression_handler as eh
from EXgen.util.util import draw_netlist

# consts : 
EPS0 = 8.854e-12

MSH_PTS = 9
FIG_DPI = 100

#################################################
#* util functions : 
#################################################

def construct_points_list(variables):
    Plist = []
    Qlist = []

    var_keys = list(variables.keys())
    P_keys = [x for x in var_keys if x[0] == 'P']
    n = len(P_keys)
    for ind in range(1, n+1):

        Q = variables[f"Q{ind}"]
        P = variables[f"P{ind}"]

        Qlist.append(Q)
        Plist.append(P)

    return Qlist, Plist

def construct_points_list_from_inserts(task):

    Plist = []
    Qlist = []

    var_keys = list(task["variables"].keys())
    P_keys = [x for x in var_keys if x[0] == 'P']
    n = len(P_keys) // 2
    for ind in range(1, n+1):

        Q = task["variables"][f"Q{ind}"]
        Px = task["variables"][f"P{ind}x"]
        Py = task["variables"][f"P{ind}y"]

        Qlist.append(Q)
        Plist.append(np.array([Px, Py]))

    return Qlist, Plist

def switch_current_source_polarity(task):

    for key in task["variables"].keys():
        if key[0] == "I":
            task["variables"][key] *= -1

def switch_current_result_polarity(results):

    for key in results.keys():
        if key[0] == "I":
            results[key] *= -1
            
#################################################
#* field calc helper functions : 
#################################################

def calc_dir_vec(Pq, Pa):
    rQA = Pa - Pq
    r = np.sqrt(sum(rQA**2))
    e_rQA = rQA/r

    return e_rQA, r

def calc_e_field_in_point(Q, Pq, Pa):
    e_rQA, r = calc_dir_vec(Pq, Pa)
    return Q/(4*np.pi*EPS0*r**2) * e_rQA

def calc_e_field_in_region(Q, Pq, rng, N:int=20):
    x = np.linspace(rng[0,0],rng[0,1],N)
    y = np.linspace(rng[1,0],rng[1,1],N)

    xx, yy = np.meshgrid(x, y)

    rx = xx - Pq[0]
    ry = yy - Pq[1]

    rr = np.sqrt(rx**2 + ry**2)
    notzero = rr > 1e-16

    erx = np.zeros_like(rr)
    ery = np.zeros_like(rr)
    
    erx[notzero] = rx[notzero] / rr[notzero]
    ery[notzero] = ry[notzero] / rr[notzero]

    E = np.zeros((2, *xx.shape), dtype=np.float64)
    E[0, notzero] = Q/(4*np.pi*EPS0*rr[notzero]**2) * erx[notzero]
    E[1, notzero] = Q/(4*np.pi*EPS0*rr[notzero]**2) * ery[notzero]

    Enorm = np.zeros((2, *xx.shape), dtype=np.float64)
    Eabs = np.sqrt(E[0, :, :]**2 + E[1, :, :]**2)
    Enorm[0, notzero] = E[0, notzero]/Eabs[notzero]
    Enorm[1, notzero] = E[1, notzero]/Eabs[notzero]

    return xx, yy, rr, E, Enorm

def calc_total_e_field(Qlist, Plist, rng, N, totnorm=False):
    
    E = np.zeros((2, N, N))
    xx = yy = []

    for Q, P in zip(Qlist, Plist):
        xx, yy, rr, Ep, Enorm = calc_e_field_in_region(Q, P, rng, N)

        if totnorm:        
            E += Ep
        else:
            E += Enorm
    
    if totnorm:
        Eabs = np.sqrt(E[0, :, :]**2 + E[1, :, :]**2)
        E /= Eabs
    else:
        E /= len(Qlist)

    return xx, yy, E

def helmholtz_setup_equation_R3(net_full, deactivate_sources: List[str]):
    
    net = source_sub_with_Ri(net_full, deactivate_sources)
    expr = '0.0'

    net_expr = net.R3.V.expr 

    if 't' in net_expr.keys():
        expr = net_expr["t"]

    return expr

def source_sub_with_Ri(net_full, deactivate_sources: List[str]):
   
    net = net_full.copy()
    
    for source in deactivate_sources:
        if source[0] == "I":
            net = net.remove(source)
        elif source[0] == "V":
            net = net.replace(source, "W")

    return net

#################################################
#* plot functions : 
#################################################

def plot_e_field_and_charges(xx, yy, E, Plist, figpth:str="./task_figures/el_field_mq.pdf"):
    fig, ax = plt.subplots()
    ax.quiver(xx, yy, E[0, :, :], E[1, :, :], pivot="tail", angles="xy")
    for ind, P in enumerate(Plist):
        ax.scatter(P[0], P[1], label=f"Q{ind+1}", s=300, alpha=0.5)
        ax.text(P[0]-0.1, P[1]-0.05, f"Q{ind+1}")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)
    ax.set_aspect('equal', 'box')

    plt.savefig(figpth, dpi=FIG_DPI)

def plot_points_and_field_dir(E, P1, P2, Pm):
    fig, ax = plt.subplots()
    figpath = "./task_figures/el_field_1.pdf"

    ax.scatter([P1[0]], [P1[1]], label="P1")
    ax.scatter([P2[0]], [P2[1]], label="P2")
    ax.scatter([Pm[0]], [Pm[1]], label="Pm")
    ax.quiver(Pm[0], Pm[1], E[0], E[1], label="Em")
    ax.legend()
    ax.grid()
    ax.set_xlabel("x in m")
    ax.set_ylabel("y in m")
    plt.savefig(figpath, dpi=FIG_DPI)
    plt.close()

    return figpath

#################################################
#* main functions : 
#################################################

def electric_field_1(task):
    P1x = task["variables"]["P1x"]
    P1y = task["variables"]["P1y"]
    P2x = task["variables"]["P2x"]
    P2y = task["variables"]["P2y"]
    P1 = np.array([P1x, P1y])
    P2 = np.array([P2x, P2y])
    Q1 = task["variables"]["Q1"] * 1e-10
    Q2 = task["variables"]["Q2"] * 1e-10
    Q3 = task["variables"]["Q3"] * 1e-10
    
    # Task : 1.1.
    Ep1 = calc_e_field_in_point(Q1, P1, P2)
    Ep2 = calc_e_field_in_point(Q2, P2, P1)
    
    F1 = Q1 * Ep2
    F2 = Q2 * Ep1

    # Task : 1.2 
    Pm = (P1 + P2)/2
    Em1 = calc_e_field_in_point(Q1, P1, Pm)
    Em2 = calc_e_field_in_point(Q2, P2, Pm)
    Em = Em1 + Em2

    figpath = plot_points_and_field_dir(Em, P1, P2, Pm)
    task["figpaths_solution"].append(figpath)
    
    # Task : 1.3 
    F3 = Q3 * Em

    return {"F1": F1, "F2": F2, "Pm": Pm, "Em": Em, "F3": F3}

def electric_field_2(task):
    P1x = task["variables"]["P1x"]
    P1y = task["variables"]["P1y"]
    P2x = task["variables"]["P2x"]
    P2y = task["variables"]["P2y"]
    P3x = task["variables"]["P3x"]
    P3y = task["variables"]["P3y"]
    P1 = np.array([P1x, P1y])
    P2 = np.array([P2x, P2y])
    P3 = np.array([P3x, P3y])
    Q1 = task["variables"]["Q1"] * 1e-10
        
    # Task : 1.1.
    Ep1 = calc_e_field_in_point(Q1, P1, P3)
    
    e2_rQA, r2 = calc_dir_vec(P2, P3)
    Q2 = - Ep1[1]*4*EPS0*r2**2/e2_rQA[1]

    return {"Q2": Q2}

def electric_field_mpq_1(task):
    # Mutpltiple question task solver function : 
    # Given a number of point charges and a location 
    # range for the charges - this function will 
    # generate a total electric field and plot it for the 
    # given configuration for the given multiple choice 
    # question. 
    
    rng = np.array([[0, 3], [0, 3]], dtype=np.float64)
    
    Qlist, Plist = construct_points_list(task["variables"])
    xx, yy, E = calc_total_e_field(Qlist, Plist, rng, MSH_PTS, totnorm=True)
    
    plot_e_field_and_charges(xx, yy, E, Plist, task["figpaths"][0])
    # task["solution-figpaths"].append(figpath)

    return {}

def norton_equivalent(task):

    net_full = Circuit(task["netlist"])

    # draw netlist to figure : 
    net_full.draw(task["figpaths"][0], style="european")

    # generate reduced netlist : 
    net = net_full.copy()
    net = net.remove("RL")

    # generate norton equivalent : 
    net_n = net.norton('k', 'l')
    net_n = net_n.circuit()

    equations = {"In": net_n.I1.I.expr["dc"], 
                 "Ri": net_n.Y1.R.expr}
    
    solutions = eh.evaluate_equations(equations, task["variables"])

    Ri = solutions["Ri"]
    In = solutions["In"]

    I = lambda x: In*(Ri/(Ri + x))

    solutions["PR_Lmax"] = Ri*I(Ri)**2
    solutions["PR_Lmax/2"] = 0.5*Ri*I(0.5*Ri)**2
    solutions["PR_Lmax*2"] = 2*Ri*I(2*Ri)**2

    return solutions

def norton_thevenin_equivalent(task):

    net_full = Circuit(task["netlist"])

    # draw netlist to figure : 
    net_full.draw(task["figpaths"][0], style="european")

    # generate reduced netlist : 
    net = net_full.copy()
    net = net.remove("RL")

    # generate norton equivalent : 
    net_n = net.norton('k', 'l')
    net_n = net_n.circuit()

    net_th = net.thevenin('k', 'l')
    net_th = net_th.circuit()

    equations = {"In": net_n.I1.I.expr["dc"], 
                 "Rin": net_n.Y1.R.expr,
                 "Uth": net_th.V1.V.expr['dc'],
                 "Rith": net_th.Z1.R.expr}
    
    solutions = eh.evaluate_equations(equations, task["variables"])

    Rin = solutions["Rin"]
    Rith = solutions["Rith"]
    Rl = task["variables"]["RL"]
    In = solutions["In"]
    Uth = solutions["Uth"]

    R_p = Rin*Rl/(Rin + Rl)
    R_s = Rith + Rl

    I = lambda x, y: In*(x/(x + y))

    solutions["PQ,n"] = -In**2 * R_p
    solutions["PR_i,n"] = I(Rl, Rin)**2 * Rin
    solutions["PR_L,n"] = I(Rin, Rl)**2 * Rl

    U = lambda x, y: Uth*(x/(y + x))

    solutions["PQ,th"] = -Uth**2 / R_s
    solutions["PR_i,th"] = U(Rith, Rl)**2 / Rith
    solutions["PR_L,th"] = U(Rl, Rith)**2 / Rl

    return solutions

def helmholtz_one_v_two_i(task):

    switch_current_source_polarity(task)

    source_pairs = [["I0", "I1"], ["V0", "I1"], ["V0", "I0"]]

    net_full = Circuit(task["netlist"])

    # draw netlist to figure : 
    net_full.draw(task["figpaths"][0], style="european")

    # generate equations : 
    equations = {}

    for ind, source_pair in enumerate(source_pairs):
        eq_id = f"UR3_{ind + 1}"
        equations[eq_id] = helmholtz_setup_equation_R3(net_full, source_pair)
    
    solutions = eh.evaluate_equations(equations, task["variables"])
    solutions["UR3"] = solutions["UR3_1"] + solutions["UR3_2"] + solutions["UR3_3"]
    solutions["UR3_abs"] = abs(solutions["UR3"])

    switch_current_source_polarity(task)

    return solutions

def thevenin_helmholtz_one_v_one_i(task):

    switch_current_source_polarity(task)

    sources = [["I0"], ["V0"]]

    net_full = Circuit(task["netlist"])

    # draw netlist to figure : 
    # net_full.draw(task["figpaths"][0], style="european")
    draw_netlist(task, 0)
    
    # generate reduced netlist : 
    net = net_full.copy()
    net = net.remove("RL")

    # generate the two nets with only one active source : 
    net_1 = source_sub_with_Ri(net, sources[0])
    net_2 = source_sub_with_Ri(net, sources[1])
    
    # generate thevenin equivalent : 

    net_th = net.thevenin('k', 'l')
    net_th = net_th.circuit()

    net_th_1 = net_1.thevenin('k', 'l')
    net_th_1 = net_th_1.circuit()

    net_th_2 = net_2.thevenin('k', 'l')
    net_th_2 = net_th_2.circuit()

    net_th_has_Z = True if "Z1" in net_th.elements.keys() else False
    net_th_1_has_V = True if "V1" in net_th_1.elements.keys() else False
    net_th_2_has_V = True if "V1" in net_th_2.elements.keys() else False

    equations = {"Uth_1": net_th_1.V1.V.expr['dc'] if net_th_1_has_V else "0.0",
                 "Uth_2": net_th_2.V1.V.expr['dc'] if net_th_2_has_V else "0.0", 
                 "Ri":  net_th.Z1.R.expr if net_th_has_Z else "0.0",
                 }
    
    if not net_th_1_has_V or not net_th_2_has_V:
        print(" - B2 : Zero V inserted somewhere!")
        print(task["netlist"])

    solutions = eh.evaluate_equations(equations, task["variables"])

    solutions["Uth"] = solutions["Uth_1"] + solutions["Uth_2"]
    solutions["Uth_abs"] = abs(solutions["Uth"])

    solutions["URL"] = solutions["Uth"]*(task["variables"]["RL"]/(solutions["Ri"] + task["variables"]["RL"]))

    solutions["IRL"] = solutions["Uth"]/(task["variables"]["RL"] + solutions["Ri"])

    switch_current_source_polarity(task)

    return solutions    

def nodal_analysis(task):

    from lcapy.sexpr import s

    t = task.copy()
    t["netlist"] = t["netlist"].replace(".net", "p.net")
    
    net = Circuit(t["netlist"]).dc()

    draw_netlist(task, 0, resistor_v_i=True)

    # calculate I01 from V0 : 
    t["variables"]["I01"] = t["variables"]["V0"]/t["variables"]["Ri1"]
    switch_current_source_polarity(task)

    # substitute variables : 
    net_subs = net.subs(t["variables"])

    # do nodal analysis : 
    na = net.nodal_analysis()
    na_subs = net_subs.nodal_analysis()

    # get nodal equations : 
    ne = na.nodal_equations()
    ne_subs = na_subs.nodal_equations()

    # solve to get nodal voltages : 
    ne_sol = ne_subs(s).solve(na.unknowns)

    # get actual values from symbolics : 
    solutions = {}
    node_voltages = [f"UK{i}" for i in range(1, len(na.unknowns)+1)]
    
    for vid, nv in zip(node_voltages, list(ne_sol.values())):
        solutions[vid] = float((nv.evalf()*s).evaluate())

    # calculate element current and voltages : 
    net_elements = eh.get_passive_elements(list(net_subs.elements))

    for e in net_elements:
        vid = f"U{e}"
        iid = f"I{e}"

        solutions[vid] = float(net_subs[e].V.expr['t'])
        solutions[iid] = float(net_subs[e].I.expr['t'])

    # generate latex equations : 
    equations_latex = ''
    equations_latex += "\\textbf{Nodal equations : } \n"
    equations_latex += "\\begin{itemize} \n"

    nodes = list(ne.keys())
    for node in nodes:
        node_tex = ne[node].latex()
        node_tex = node_tex.replace("(t)", '')
        node_tex = node_tex.replace("V", 'U')
        equations_latex += "\\item " + node + " : $" + node_tex + '$ \n'

    equations_latex += "\\end{itemize} \n"

    equations_latex += "\\textbf{After inserting given values : } \n"

    equations_latex += "\\begin{itemize} \n"

    for node in nodes:
        node_tex = ne_subs[node].evalf(6).latex()
        node_tex = node_tex.replace("(t)", '')
        node_tex = node_tex.replace("V", 'U')
        equations_latex += "\\item " + node + " : $" + node_tex + '$ \n'

    equations_latex += "\\end{itemize} \n"

    solutions["equations_latex"] = equations_latex

    switch_current_source_polarity(task)

    return solutions