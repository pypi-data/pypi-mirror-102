# -*- coding: utf-8 -*-
# Python 3.8
# 
# Conventions:
# SPL: shortest path length
# 
# Functions:
# 1. Degree Histogram
# 2. Effective Diameter (90-th percentile of the distribution of SPLs)
# 3. Average SPL
# 4. Degree Assortativity Coefficient
# 5. Clustering Coefficient
# 
# Recommend:
# 1. NaiveImpl
# 2. SnapImpl
# 3. NXImpl
# 4. NXImpl
# 5. NXImpl
# 
# Requirements:
# Packages      Version
# networkx      2.5
# snap-stanford 6.0.0

import os
import sys
import snap
import networkx as nx
import traceback
from typing import List, Tuple, Dict
from collections import defaultdict


class NaiveImpl(object):
    """Implement
    0. Read Graph
    1. Degree Histogram
    with naive method
    """
    def __init__(self, filename: str, num_src_nodes: int=-1, num_tgt_nodes: int=-1, is_directed: bool=True, id_from: int=0):
        '''
        @param filename      a directory or a file
        @param num_src_nodes # source nodes, -1: unknown
        @param num_tgt_nodes # target nodes, -1: unknown
        @param is_directed   True: directed; False: undirected
        @param id_from       start node id, -1: not number
        @else  file format   TSV, ADJ
        '''
        super(NaiveImpl, self).__init__()
        self.filename = filename
        self.num_src_nodes = num_src_nodes
        self.num_tgt_nodes = num_tgt_nodes
        self.is_directed = is_directed
        self.id_from = id_from
        self.is_num_id = (id_from >= 0)
        self.has_check = self.check()
        self.in_out_deg_hist = None
        self.deg_hist = None

    def check(self) -> bool:
        if not os.path.exists(self.filename):
            return False
        self.is_file = os.path.isfile(self.filename)
        return True

    def __yield_num_edge_tuple__(self, a_file: str):
        with open(a_file, 'r') as fin:
            for line in fin:
                line = line.strip().split()
                if len(line) < 2:
                    continue
                try:
                    uid = int(line[0])
                    for v in line[1:]:
                        vid = int(v)
                        yield (uid, vid)
                except:
                    continue

    def __yield_str_edge_tuple__(self, a_file: str):
        with open(a_file, 'r') as fin:
            for line in fin:
                line = line.strip().split()
                if len(line) < 2:
                    continue
                uid = line[0]
                for vid in line[1:]:
                    yield (uid, vid)

    def __yield2_dir_edges__(self, dirname: str):
        for path, dirs, files in os.walk(dirname):
            for fn in files:
                filename = os.path.join(path, fn)
                if self.is_num_id:
                    yield self.__yield_num_edge_tuple__(filename)
                else:
                    yield self.__yield_str_edge_tuple__(filename)

    def yield_edges(self):
        if self.has_check:
            if self.is_file:
                if self.is_num_id:
                    return self.__yield_num_edge_tuple__(self.filename)
                else:
                    return self.__yield_str_edge_tuple__(self.filename)
            else:
                for y_file in self.__yield2_dir_edges__(self.filename):
                    for e_tuple in y_file:
                        yield e_tuple

    def __aux__(self, a_list):
        ans = defaultdict(lambda: 0)
        for _ in a_list:
            if _ > 0:
                ans[_] += 1
        return ans

    def get_in_out_degree_histogram(self) -> Tuple[List[List]]:
        '''
        ans[0]: in-degree list:  [[degree, #nodes]]
        ans[1]: out-degree list: [[degree, #nodes]]
        '''
        if self.in_out_deg_hist != None:
            return self.in_out_deg_hist
        if self.has_check:
            if self.is_num_id and self.num_src_nodes != -1 and self.num_tgt_nodes != -1:
                node_in_degree = [0 for _ in range(self.num_tgt_nodes)]
                node_out_degree = [0 for _ in range(self.num_src_nodes)]
                for uid, vid in self.yield_edges():
                    node_out_degree[uid - self.id_from] += 1
                    node_in_degree[vid - self.id_from] += 1
                in_degree_map = self.__aux__(node_in_degree)
                out_degree_map = self.__aux__(node_out_degree)
            else:
                node_in_degree_map = defaultdict(lambda: 0)
                node_out_degree_map = defaultdict(lambda: 0)
                for uid, vid in self.yield_edges():
                    node_out_degree_map[uid] += 1
                    node_in_degree_map[vid] += 1
                in_degree_map = self.__aux__([val for _, val in node_in_degree_map.items()])
                out_degree_map = self.__aux__([val for _, val in node_out_degree_map.items()])
            self.in_out_deg_hist = (
                [[deg, freq] for deg, freq in in_degree_map.items()],
                [[deg, freq] for deg, freq in out_degree_map.items()]
            )
            return self.in_out_deg_hist
        return ([], [])

    def get_degree_histogram(self) -> List[List]:
        '''
        [[degree, #nodes]]
        '''
        if self.deg_hist != None:
            return self.deg_hist
        if self.has_check:
            if self.is_num_id and self.num_src_nodes != -1 and self.num_tgt_nodes != -1:
                mx_nodes = max(self.num_src_nodes, self.num_tgt_nodes)
                degree_list = [0 for _ in range(mx_nodes)]
                for uid, vid in self.yield_edges():
                    degree_list[uid - self.id_from] += 1
                    degree_list[vid - self.id_from] += 1
                degree_map = self.__aux__(degree_list)
            else:
                node_degree_map = defaultdict(lambda: 0)
                for uid, vid in self.yield_edges():
                    node_degree_map[uid] += 1
                    node_degree_map[uid] += 1
                degree_map = self.__aux__([val for _, val in node_degree_map.items()])
            self.deg_hist = [[deg, freq] for deg, freq in degree_list.items()]
            return self.deg_hist
        return []


class SnapImpl(NaiveImpl):
    """Implement
    1. Degree Histogram         GetDegCnt | GetInDegCnt / GetOutDegCnt
    2. Effective Diameter       GetBfsEffDiamAll
    3. Average SPL              GetBfsEffDiamAll
    5. Clustering Coefficient   GetClustCf
    using snap"""
    def __init__(self, filename: str, num_src_nodes: int=-1, num_tgt_nodes: int=-1, is_directed: bool=True, id_from: int=0, src_tag: str='', tgt_tag: str=''):
        super(SnapImpl, self).__init__(filename, num_src_nodes, num_tgt_nodes, is_directed, id_from)
        self.src_tag = src_tag
        self.tgt_tag = tgt_tag
        self.is_homo = (src_tag == tgt_tag)
        self.d_graph = None
        self.un_graph = None
        self.build_graph()
        self.eff_diam = None
        self.avg_spl = None
        self.cc = None
        self.in_out_deg_hist = None
        self.deg_hist = None
        if not self.is_homo and self.num_src_nodes < 0:
            self.num_src_nodes = self.__get_not_homo_num_src__()

    def __wrap_src_node__(self, nid):
        wnid = nid
        if self.src_tag != '':
            wnid = '{}_{}'.format(self.src_tag, nid)
        return wnid

    def __wrap_tgt_node__(self, nid):
        wnid = nid
        if self.tgt_tag != '':
            wnid = '{}_{}'.format(self.tgt_tag, nid)
        return wnid

    def __wrap_edge__(self, uid, vid):
        return (self.__wrap_src_node__(uid), self.__wrap_tgt_node__(vid))

    def __get_not_homo_num_src__(self):
        ans = 0
        for uid, _ in self.yield_edges():
            ans = max(ans, uid)
        return (ans + 1)

    def __add_nodes_edges__(self, graph_ins):
        if self.has_check:
            if self.is_homo:
                if self.is_num_id and self.num_src_nodes > 0 and self.num_tgt_nodes > 0:
                    num_nodes = max(self.num_src_nodes, self.num_tgt_nodes)
                    for nid in range(self.id_from, self.id_from + num_nodes):
                        # nid = self.__wrap_src_node__(nid)
                        graph_ins.AddNode(nid)
            else:
                if self.is_num_id and self.num_src_nodes > 0:
                    for nid in range(self.id_from, self.id_from + self.num_src_nodes):
                        # nid = self.__wrap_src_node__(nid)
                        graph_ins.AddNode(nid)
                if self.is_num_id and self.num_tgt_nodes > 0:
                    for nid in range(self.id_from, self.id_from + self.num_tgt_nodes):
                        # nid = self.__wrap_tgt_node__(nid)
                        nid += self.num_src_nodes
                        graph_ins.AddNode(nid)
            for uid, vid in self.yield_edges():
                # uid, vid = self.__wrap_edge__(uid, vid)
                if not self.is_homo:
                    vid += self.num_src_nodes
                try:
                    graph_ins.AddEdge(uid, vid)
                except:
                    try:
                        graph_ins.AddNode(uid)
                    except:
                        pass
                    try:
                        graph_ins.AddNode(vid)
                    except:
                        pass
                    try:
                        graph_ins.AddEdge(uid, vid)
                    except:
                        pass

    def build_undirected_graph(self):
        self.un_graph = snap.TUNGraph.New()
        self.__add_nodes_edges__(self.un_graph)

    def build_directed_graph(self):
        self.d_graph = snap.TNGraph.New()
        self.__add_nodes_edges__(self.d_graph)

    def build_graph(self):
        if self.is_directed:
            self.build_directed_graph()
        else:
            self.build_undirected_graph()

    def get_in_out_degree_histogram(self) -> Tuple[List[List]]:
        '''
        ans[0]: in-degree list:  [[degree, #nodes]]
        ans[1]: out-degree list: [[degree, #nodes]]
        '''
        if self.in_out_deg_hist != None:
            return self.in_out_deg_hist
        if self.d_graph != None:
            in_degree_cnt = self.d_graph.GetInDegCnt()
            out_degree_cnt = self.d_graph.GetOutDegCnt()
            self.in_out_deg_hist = (
                [[_.GetVal1(), _.GetVal2()] for _ in in_degree_cnt],
                [[_.GetVal1(), _.GetVal2()] for _ in out_degree_cnt]
            )
            return self.in_out_deg_hist
        return ([], [])

    def get_degree_histogram(self) -> List[List]:
        '''
        [[degree, #nodes]]
        '''
        if self.deg_hist != None:
            return self.deg_hist
        if self.un_graph != None:
            degree_cnt = self.un_graph.GetDegCnt()
            self.deg_hist = [[_.GetVal1(), _.GetVal2()] for _ in degree_cnt]
            return self.deg_hist
        return []

    def __calc_eff_diam_avg_spl__(self):
        if self.d_graph != None:
            res = self.d_graph.GetBfsEffDiamAll(10, True)
            self.eff_diam = res[0]
            self.avg_spl = res[3]
        elif self.un_graph != None:
            res = self.un_graph.GetBfsEffDiamAll(10, False)
            self.eff_diam = res[0]
            self.avg_spl = res[3]
        else:
            self.eff_diam = -1
            self.avg_spl = -1

    def __calc_cc__(self):
        if self.d_graph != None:
            self.cc = self.d_graph.GetClustCf()
        elif self.un_graph != None:
            self.cc = self.un_graph.GetClustCf()
        else:
            self.cc = -1

    def get_effective_diameter(self) -> float:
        if self.eff_diam != None:
            return self.eff_diam
        self.__calc_eff_diam_avg_spl__()
        return self.eff_diam

    def get_average_path_length(self) -> float:
        if self.avg_spl != None:
            return self.avg_spl
        self.__calc_eff_diam_avg_spl__()
        return self.avg_spl
 
    def get_clustering_coefficient(self) -> float:
        if self.cc != None:
            return self.cc
        self.__calc_cc__()
        return self.cc


class NXImpl(NaiveImpl):
    """Implement
    1. Degree Histogram         degree_histogram (Not For DiGraph)
    3. Average SPL              average_shortest_path_length
    4. Degree Assort Coeff      degree_assortativity_coefficient
    5. Clustering Coefficient   average_clustering
    using networkx
    """
    def __init__(self, filename: str, num_src_nodes: int=-1, num_tgt_nodes: int=-1, is_directed: bool=True, id_from: int=0, src_tag: str='', tgt_tag: str=''):
        super(NXImpl, self).__init__(filename, num_src_nodes, num_tgt_nodes, is_directed, id_from)
        self.src_tag = src_tag
        self.tgt_tag = tgt_tag
        self.is_homo = (src_tag == tgt_tag)
        self.d_graph = None
        self.un_graph = None
        self.build_graph()
        self.avg_spl = None
        self.cc = None
        self.assort_coef = None

    def __yield_wrap_edges__(self):
        for uid, vid in self.yield_edges():
            if self.src_tag != '':
                uid = '{}_{}'.format(self.src_tag, uid)
            if self.tgt_tag != '':
                vid = '{}_{}'.format(self.tgt_tag, vid)
            yield (uid, vid)

    def build_graph(self):
        if self.is_directed:
            self.d_graph = nx.DiGraph()
            self.d_graph.add_edges_from(self.__yield_wrap_edges__())
        else:
            self.un_graph = nx.Graph()
            self.un_graph.add_edges_from(self.__yield_wrap_edges__())

    def get_graph(self):
        if self.d_graph != None:
            return self.d_graph
        if self.un_graph != None:
            return self.un_graph
        return None

    def get_degree_histogram(self) -> List[List]:
        '''
        [[degree, #nodes]]
        '''
        graph = self.get_graph()
        if graph == None:
            return []
        res = nx.degree_histogram(graph)
        return [[deg + 1, freq] for deg, freq in enumerate(res)]

    def get_average_path_length(self) -> float:
        if self.avg_spl != None:
            return self.avg_spl
        self.avg_spl = 0
        graph = self.get_graph()
        if graph == None:
            return self.avg_spl
        try:
            self.avg_spl = nx.average_shortest_path_length(graph)
        except:
            print('Calculate avg_spl wrong with networkx')
            pass
        return self.avg_spl

    def get_clustering_coefficient(self) -> float:
        if self.cc != None:
            return self.cc
        self.cc = 0.0
        graph = self.get_graph()
        if graph == None:
            return self.cc
        self.cc = nx.average_clustering(graph)
        return self.cc

    def get_assortativity_coefficient(self) -> float:
        if self.assort_coef != None:
            return self.assort_coef
        self.assort_coef = 0.0
        graph = self.get_graph()
        if graph == None:
            return self.assort_coef
        try:
            self.assort_coef = nx.degree_assortativity_coefficient(graph)
        except:
            self.assort_coef = -2
        return self.assort_coef


class HeatMap(NaiveImpl):
    def __init__(self, filename: str, num_src_nodes: int=-1, num_tgt_nodes: int=-1, is_directed: bool=True, id_from: int=0):
        super(HeatMap, self).__init__(filename, num_src_nodes, num_tgt_nodes, is_directed, id_from)
        self.num_row = 0
        self.num_col = 0
        self.has_norm = False
        self.td_array = None
        if num_src_nodes > 0 and num_tgt_nodes > 0:
            self.num_row = num_src_nodes
            self.num_col = num_tgt_nodes
        else:
            self.__get_row_col__()

    def __get_row_col__(self):
        self.source_node_map = dict()   # normalize
        self.target_node_map = dict()   # normalize
        sid, tid = 0, 0
        for uid, vid in self.yield_edges():
            if uid not in self.source_node_map:
                self.source_node_map[uid] = sid
                sid += 1
            if vid not in self.target_node_map:
                self.target_node_map[vid] = tid
                tid += 1
        self.num_row = sid
        self.num_col = tid
        self.has_norm = True

    def get_heat(self, hm_size: int=100) -> List[List[int]]:
        if self.td_array != None:
            return self.td_array
        td_array = [[0 for _ in range(hm_size)] for _ in range(hm_size)]
        row_step = int(self.num_row / hm_size)
        col_step = int(self.num_col / hm_size)
        cell_max_val = 0
        if self.has_norm:
            for uid, vid in self.yield_edges():
                t_row = min(int(self.source_node_map[uid] / row_step), hm_size - 1)
                t_col = min(int(self.target_node_map[vid] / col_step), hm_size - 1)
                td_array[t_row][t_col] += 1
                if not self.is_directed:    # undirected
                    td_array[t_col][t_row] += 1
                cell_max_val = max(cell_max_val, td_array[t_row][t_col])
        else:
            for uid, vid in self.yield_edges():
                t_row = min(int((uid - self.id_from) / row_step), hm_size - 1)
                t_col = min(int((vid - self.id_from) / col_step), hm_size - 1)
                td_array[t_row][t_col] += 1
                if not self.is_directed:    # undirected
                    td_array[t_col][t_row] += 1
                cell_max_val = max(cell_max_val, td_array[t_row][t_col])
        # trick
        further_stat = [0 for _ in range(cell_max_val + 1)]
        gz = 0
        for i in range(hm_size):
            for j in range(hm_size):
                further_stat[td_array[i][j]] += 1
                if td_array[i][j] > 0:
                    gz += 1
        hyper, hyper2 = 40, 50
        tmp, tmp_i = 0, 100
        threshold = int(gz / hyper)
        further_func = [100 - hyper for _ in range(cell_max_val + 1)]
        for i in range(cell_max_val, -1, -1):
            further_func[i] = tmp_i
            tmp += further_stat[i]
            if (tmp_i > (100 - hyper)) and (tmp > threshold):
                tmp = 0
                tmp_i -= 1
        further_func[0] = hyper2
        for i in range(hm_size):
            for j in range(hm_size):
                td_array[i][j] = further_func[td_array[i][j]]
        self.td_array = td_array
        return td_array


class IntegratedImpl(object):
    """
    Input: the whole graph (directed, id from 0)
    Output: metrics
    1. degree histogram         naive method / snap
    2. effective diameter       snap
    3. average SPL              snap
    4. degree assort... coeff   nx
    5. clustering coefficient   nx
    """
    def __init__(self, dirname: str, subdir_map: Dict):
        '''
        subdir_map structure:
        {
            `edge_label`: {`source`: src_node_label, `target`: tgt_node_label, `n_source`: n_src, `n_target`: n_tgt},
            ...
        }
        '''
        super(IntegratedImpl, self).__init__()
        self.dirname = dirname
        self.subdir_map = subdir_map
        self.snap_graph = None
        self.nx_graph = None
        self.in_out_deg_hist = None
        self.eff_diam = None
        self.avg_spl = None
        self.assort_coef = None
        self.cc = None
        self.__build_graph__()

    def __build_graph__(self):
        if not os.path.exists(self.dirname):
            return
        self.snap_graph = snap.TNGraph.New()
        self.nx_graph = nx.DiGraph()
        ugly_pre = 0
        ugly_map = dict()
        for _ in os.listdir(self.dirname):
            path_name = os.path.join(self.dirname, _)
            if not os.path.isdir(path_name): continue
            if _ not in self.subdir_map: continue
            src_tag = self.subdir_map[_]['source']
            tgt_tag = self.subdir_map[_]['target']
            num_src_nodes = self.subdir_map[_]['n_source']
            num_tgt_nodes = self.subdir_map[_]['n_target']
            naive_impl = NaiveImpl(path_name, num_src_nodes, num_tgt_nodes)
            for uid, vid in naive_impl.yield_edges():
                xuid = '{}_{}'.format(src_tag, uid)
                xvid = '{}_{}'.format(tgt_tag, vid)
                self.nx_graph.add_edge(xuid, xvid)
                # for snap
                if src_tag not in ugly_map:
                    ugly_map[src_tag] = ugly_pre
                    ugly_pre += num_src_nodes
                if tgt_tag not in ugly_map:
                    ugly_map[tgt_tag] = ugly_pre
                    ugly_pre += num_tgt_nodes
                tuid = uid + ugly_map[src_tag]
                tvid = vid + ugly_map[tgt_tag]
                try:
                    self.snap_graph.AddEdge(tuid, tvid)
                except:
                    try:
                        self.snap_graph.AddNode(tuid)
                    except:
                        pass
                    try:
                        self.snap_graph.AddNode(tvid)
                    except:
                        pass
                    try:
                        self.snap_graph.AddEdge(tuid, tvid)
                    except:
                        pass

    def get_in_out_degree_histogram(self) -> Tuple[List[List]]:
        '''
        ans[0]: in-degree list:  [[degree, #nodes]
        ans[1]: out-degree list: [[degree, #nodes]]
        '''
        if self.in_out_deg_hist != None:
            return self.in_out_deg_hist
        if self.snap_graph == None:
            return ([], [])
        in_degree_cnt = self.snap_graph.GetInDegCnt()
        out_degree_cnt = self.snap_graph.GetOutDegCnt()
        self.in_out_deg_hist = (
            [[_.GetVal1(), _.GetVal2()] for _ in in_degree_cnt],
            [[_.GetVal1(), _.GetVal2()] for _ in out_degree_cnt]
        )
        return self.in_out_deg_hist

    def get_effective_diameter(self) -> float:
        if self.eff_diam != None:
            return self.eff_diam
        if self.snap_graph == None:
            return 0.0
        res = self.snap_graph.GetBfsEffDiamAll(10, True)
        self.eff_diam = res[0]
        self.avg_spl = res[3]
        return self.eff_diam

    def get_average_path_length(self) -> float:
        if self.avg_spl != None:
            return self.avg_spl
        if self.snap_graph == None:
            return 0.0
        res = self.snap_graph.GetBfsEffDiamAll(10, True)
        self.eff_diam = res[0]
        self.avg_spl = res[3]
        return self.avg_spl

    def get_assortativity_coefficient(self) -> float:
        if self.assort_coef != None:
            return self.assort_coef
        if self.nx_graph == None:
            return 0.0
        try:
            self.assort_coef = nx.degree_assortativity_coefficient(self.nx_graph)
        except:
            self.assort_coef = -2
        return self.assort_coef

    def get_clustering_coefficient(self) -> float:
        if self.cc != None:
            return self.cc
        if self.nx_graph == None:
            return 0.0
        self.cc = nx.average_clustering(self.nx_graph)
        return self.cc
