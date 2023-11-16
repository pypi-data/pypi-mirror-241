#  This file is part of the Traffic Assignment Package developed at KU Leuven.
#  Copyright (c) 2023 Jeroen Verstraete
#  License: GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007, see license.txt
#  More information at: https://gitlab.kuleuven.be/ITSCreaLab
#  or contact: ITScrealab@kuleuven.be
#
#
#
#
import numpy as np
from numba import njit

from tsakul.demand import InternalStaticDemand
from tsakul.sta.utilities import _bpr_cost, aon
from tsakul.supply import Network


@njit
def dun(
    network: Network, demand: InternalStaticDemand
):
    f1 = np.zeros(network.tot_links)
    f2 = f1.copy()
    ff_tt = network.links.length / network.links.free_speed

    ff_costs = _bpr_cost(
        capacities=network.links.capacity,
        ff_tts=ff_tt,
        flows=f2,
    )

    ssp_costs, f2 = aon(demand, ff_costs, network)

    costs = _bpr_cost(
        capacities=network.links.capacity,
        ff_tts=ff_tt,
        flows=f2,
    )

    return costs, f2
