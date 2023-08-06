# -*- coding: utf-8 -*-
import os
import sys
import time
from PyFastSgg import PyFastSGG


def test_ins(filename: str, b_running_mode: bool=True) -> PyFastSGG:
    pysgg_ins = PyFastSGG(filename, b_running_mode)
    return pysgg_ins


def test_gen(pysgg_ins: PyFastSGG) -> bool:
    b_run = pysgg_ins.run()
    if b_run:
        print('Generation running ...')
    else:
        print('Generation run failed ...')
        return False
    print('All Edges: {}'.format(
        pysgg_ins.get_all_edge_names()
    ))
    progress = 0.0
    cur_edge = ''
    while progress < 1.0:
        progress = pysgg_ins.current_generation_progress()
        print('Progress: %05f' % progress)
        tag = pysgg_ins.current_generation_tag()
        print('Tag: {}'.format(tag))
        if tag != cur_edge:
            cur_edge = tag
            progress = 0.0
        time.sleep(1)
    print('Generation done.')
    return True


def test_metrics(pysgg_ins: PyFastSGG) -> None:
    def for_a_subgraph(e_label: str):
        print('In-Out Degree Histogram: {}'.format(
            pysgg_ins.get_in_out_deg_hist(e_label)
        ))
        print('Effective Diameter: {}'.format(
            pysgg_ins.get_eff_diam(e_label)
        ))
        print('Average Path Length: {}'.format(
            pysgg_ins.get_avg_spl(e_label)
        ))
        print('Clustering Coefficient: {}'.format(
            pysgg_ins.get_cc(e_label)
        ))
        print('Assortativity Coefficient: {}'.format(
            pysgg_ins.get_assort_coeff(e_label)
        ))
    e_list = pysgg_ins.get_all_edge_names()
    e_list.append('')
    for _ in e_list:
        print('========== Edge: {} =========='.format(_))
        for_a_subgraph(_)
        print('========== END ==========')


def main():
    if len(sys.argv) < 3:
        print('Usage: python {} [JSON filename] [mode]'.format(__file__))
        return
    filename = sys.argv[1]
    b_running_mode = (sys.argv[2] == '1')
    if b_running_mode:
        pysgg_ins = test_ins(filename)
        b_run = test_gen(pysgg_ins)
        if b_run:
            test_metrics(pysgg_ins)
    else:
        pysgg_ins = test_ins(filename, False)
        test_metrics(pysgg_ins)


if __name__ == '__main__':
    main()
