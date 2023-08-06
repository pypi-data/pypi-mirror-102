import csv
import threading

from .classes import Assignment
from .colgen import _assignment
from .consts import MAX_TIME_BUDGET, MIN_TIME_BUDGET, BUDGET_TIME_INTVL


__all__ = ['evaluate_accessiblity']


def _get_interval_id(t):
    """ return interval id in predefined time budget intervals

    [0, MIN_TIME_BUDGET],

    (MIN_TIME_BUDGET + (i-1)*BUDGET_TIME_INTVL, MIN_TIME_BUDGET + i*BUDGET_TIME_INTVL]
        where, i is integer and i>=1
    """
    if t < MIN_TIME_BUDGET:
        return 0

    if (t % (MIN_TIME_BUDGET+BUDGET_TIME_INTVL)) == 0:
        return int(t/(MIN_TIME_BUDGET+BUDGET_TIME_INTVL))

    return int(t/(MIN_TIME_BUDGET+BUDGET_TIME_INTVL)) + 1


def _update_generalized_link_cost_a(spnetworks):
    """ update generalized link costs to calculate accessibility """
    for sp in spnetworks:
        vot = sp.get_agent_type().get_vot()
        ffs = sp.get_agent_type().get_free_flow_speed()

        if sp.get_agent_type().get_type().startswith('p'):
            for link in sp.get_links():
                sp.link_cost_array[link.get_seq_no()] = (
                link.get_free_flow_travel_time()
                + link.get_route_choice_cost()
                + link.get_toll() / min(0.001, vot) * 60
            )
        else:
            for link in sp.get_links():
                sp.link_cost_array[link.get_seq_no()] = (
                (link.get_length() / max(0.001, ffs) * 60)
                + link.get_route_choice_cost()
                + link.get_toll() / min(0.001, vot) * 60
            )


def _update_min_travel_time(column_pool):
    max_min = 0

    for cv in column_pool.values():
        min_travel_time = -1

        for col in cv.get_columns().values():
            # the naming of get_toll() may be confusing but it is the path
            # generalized cost or gradient cost from the first iteration of 
            # assignment
            # see _backtrace_shortest_path_tree()
            # and _update_generalized_link_cost_a() for details
            travel_time = col.get_toll()
            # update minmum travel time
            if travel_time < min_travel_time or min_travel_time == -1:
                min_travel_time = travel_time

        cv.update_min_travel_time(min_travel_time)

        if min_travel_time > max_min:
            max_min = min_travel_time

    return max_min


def _output_accessiblity(column_pool, at, output_dir='.'):
    """ output accessiblity for each OD pair (i.e., travel time) """
    with open(output_dir+'/accessibility.csv', 'w',  newline='') as f:
        headers = ['o_zone_id', 'o_zone_name',
                   'd_zone_id', 'd_zone_name',
                   'accessibility', 'geometry']

        writer = csv.writer(f)
        writer.writerow(headers)

        # for multimodal case, find the minimum travel time
        # under mode 'p' (i.e., auto)
        dp = 0
        for k, cv in column_pool.items():
            # k = (at, dp, oz, dz)
            if k[0] != at or k[1] != dp:
                continue

            min_tt = max(0, cv.get_min_travel_time())

            # output assessiblity
            line = [k[2], '', k[3], '', min_tt, '']
            writer.writerow(line)


def _output_accessibility_aggregated(column_pool, interval_num,
                                     zones, ats, output_dir='.'):
    """ output aggregated accessiblity matrix for each agent type """

    with open(output_dir+'/accessibility_aggregated.csv', 'w',  newline='') as f:
        time_bugets = [
            'TT_'+str(MIN_TIME_BUDGET+BUDGET_TIME_INTVL*i) for i in range(interval_num)
        ]

        headers = ['zone_id', 'geometry', 'mode']
        headers.extend(time_bugets)

        writer = csv.writer(f)
        writer.writerow(headers)

        # calculate accessiblity
        dp = 0
        for oz in zones:
            if oz == -1:
                continue

            for atype in ats:
                at = atype.get_id()
                # number of accessible zones from oz for each agent type
                counts = [0] * interval_num
                for dz in zones:
                    if (at, dp, oz, dz) not in column_pool.keys():
                        continue

                    cv = column_pool[(at, dp, oz, dz)]
                    if cv.get_min_travel_time() == -1:
                        continue

                    id = _get_interval_id(cv.get_min_travel_time())
                    while id < interval_num:
                        counts[id] += 1
                        id += 1
                # output assessiblity
                line = [oz, '', atype.get_type()]
                line.extend(counts)
                writer.writerow(line)


def evaluate_accessiblity(ui, multimodal=True, output_dir='.'):
    """ evaluate and output accessiblity matrices

    Parameters
    ----------
    ui
        network object generated by pg.read_demand()
    multimodal
        True or False. If true, the accessibility of each mode specified in
        settings.yml will be calculated and outputed; If false, only the
        accessibility under mode auto will be calculated and outpute.

        The default is True.
    output_dir
        directory of output files. The default is the current working directory.

    Outputs
    -------
    accessibility.csv
        accessibility between each OD pair in terms of free flow travel time
    accessibility_aggregated.csv
        aggregated accessibility as to the number of accessible zones from each
        zone for each transportation mode specified in settings.yml

    Developer's Notes
    -----------------
    This is a simple implementation without creating virtual centroids and
    connectors between each centroid and its corresponding activity nodes.
    """

    print('this operation will reset link volume and travel time!!!\n')

    # set up assignment object dedicated to accessibility evaluation
    base = ui._base_assignment
    A = Assignment()
    A.network = base.get_network()

    if multimodal:
        for at in base.get_agent_types():
            A.update_agent_types(at)
    else:
        # otherwise, only consider mode 'p' (i.e., auto)
        at = base.get_agent_type('p')
        A.update_agent_types(at)

    # we only need one demand period even multiple could exist
    # see setup_spntwork_a() too
    dp = base.get_demand_periods()[0]
    A.update_demand_periods(dp)

    A.setup_spntwork_a()
    A.setup_column_pool_a()

    zones = A.get_zones()
    ats = A.get_agent_types()
    column_pool = A.get_column_pool()

    # update generalized link cost with free flow speed
    _update_generalized_link_cost_a(A.get_spnetworks())
    # run assignment for one iteration to generate column pool
    _assignment(A.get_spnetworks(), column_pool, 0)
    # update minimum travel time between O and D for each agent type
    max_min = _update_min_travel_time(column_pool)
    if max_min > MAX_TIME_BUDGET:
        # manual cutoff to avoid potential long computation time
        max_min = MAX_TIME_BUDGET
    interval_num = _get_interval_id(max_min) + 1

    multitheading = True
    if multitheading:
        at_id = A.get_agent_type_id('p')
        t = threading.Thread(
            target=_output_accessiblity,
            args=(column_pool, at_id, output_dir,))
        t.start()

        t = threading.Thread(
            target=_output_accessibility_aggregated,
            args=(column_pool, interval_num, zones, ats, output_dir)
        )
        t.start()
    else:
        # calculate and output accessiblity for each OD pair (i.e., travel time)
        _output_accessiblity(column_pool, at)
        # calculate and output aggregated accessiblity matrix for each agent type
        _output_accessibility_aggregated(column_pool, interval_num, zones, ats)