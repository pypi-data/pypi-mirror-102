# -*- coding: utf-8 -*-
import pyfastsgg as pysgg

import os
import json
import traceback
from typing import List, Tuple
from json.decoder import JSONDecodeError

from .schema import Schema
from .utils import NaiveImpl, SnapImpl, NXImpl, HeatMap, IntegratedImpl


class PyFastSGG(object):
    """Python Wrapper for C++ implementation of FastSGG"""
    def __init__(self, filename: str, b_running_mode: bool=True) -> None:
        '''
        @param  filename    JSON filename
        '''
        # super(PyFastSGG, self).__init__()
        self.is_running_mode = b_running_mode
        self.set_json_file(filename)

    def __get_schema_obj__(self) -> None:
        if os.path.exists(self.filename):
            try:
                self.schema_obj = json.load(open(self.filename, 'r'))
                self.graph_name = self.schema_obj[Schema.GraphName]
                self.node_cnt_map = dict()
                for _ in self.schema_obj[Schema.NodeName]:
                    self.node_cnt_map[_[Schema.NodeLabel]] = _[Schema.NodeAmount]
                self.subdir_map = dict()
                self.node_info_map = dict()
                self.subgraph_metric_impl = dict()
                for _ in self.schema_obj[Schema.EdgeName]:
                    self.subdir_map[_[Schema.EdgeLabel]] = {
                        'source': _[Schema.EdgeSourceNode],
                        'target': _[Schema.EdgeTargetNode],
                        'amount': _[Schema.EdgeAmount],
                        'n_source': self.node_cnt_map[_[Schema.EdgeSourceNode]],
                        'n_target': self.node_cnt_map[_[Schema.EdgeTargetNode]]
                    }
                    if Schema.CommunityName in _:
                        self.subdir_map[_[Schema.EdgeLabel]]['communities'] = _[Schema.CommunityName][Schema.CommunityAmount]
                    self.subgraph_metric_impl[_[Schema.EdgeLabel]] = {
                        'snap': None,
                        'nx': None,
                        'heat': None
                    }
                for _ in self.schema_obj[Schema.NodeName]:
                    self.node_info_map[_[Schema.NodeLabel]] = {
                        'amount': _[Schema.NodeAmount]
                    }
                self.all_actual_nodes = None
                self.all_actual_edges = None
            except JSONDecodeError:
                traceback.print_exc()
                self.schema_obj = None

    def set_json_file(self, filename: str) -> None:
        self.filename = filename
        if os.path.exists(filename):
            self.sgg_ptr = pysgg.get_generation_ptr(filename)
        else:
            self.sgg_ptr = None
        self.b_start_run = False
        self.b_stop_gen = False
        self.schema_obj = None
        self.whole_impl = None
        self.__get_schema_obj__()

    def run(self) -> bool:
        if self.sgg_ptr == None:
            return False
        pysgg.start_generate(self.sgg_ptr)
        self.b_start_run = True
        return self.has_generation_start()

    def get_graph_name(self) -> str:
        if self.schema_obj == None:
            return ''
        return self.schema_obj[Schema.GraphName]

    def get_all_node_names(self) -> List[str]:
        if self.schema_obj == None:
            return []
        return [_[Schema.NodeLabel] for _ in self.schema_obj[Schema.NodeName]]

    def get_all_edge_names(self) -> List[str]:
        if self.schema_obj == None:
            return []
        return [_[Schema.EdgeLabel] for _ in self.schema_obj[Schema.EdgeName]]

    def get_num_nodes(self, node_label: str='') -> int:
        if self.schema_obj == None:
            return 0
        if node_label in self.node_info_map:
            return self.node_info_map[node_label][Schema.NodeAmount]
        elif node_label == '':
            if self.all_actual_nodes:
                return self.all_actual_nodes
            all_nodes = self.get_all_node_names()
            ans = 0
            for _ in all_nodes:
                ans += self.node_info_map[_][Schema.NodeAmount]
            self.all_actual_nodes = ans
            return ans
        return 0

    def get_num_edges(self, edge_label: str='') -> int:
        self.__update_status__()
        if self.b_stop_gen:
            all_edges = self.get_all_edge_names()
            if edge_label in all_edges:
                return pysgg.get_actual_num_edges(self.sgg_ptr, edge_label)
            elif edge_label == '':
                if self.all_actual_edges:
                    return self.all_actual_edges
                ans = 0
                for _ in all_edges:
                    ans += pysgg.get_actual_num_edges(self.sgg_ptr, _)
                self.all_actual_edges = ans
                return ans
            return 0
        return 0

    def get_num_communities(self, edge_label: str) -> int:
        if self.schema_obj == None:
            return 0
        if edge_label in self.subdir_map and 'communities' in self.subdir_map[edge_label]:
            return self.subdir_map[edge_label]['communities']
        return 0

    def get_an_edge_ends(self, edge_label: str) -> Tuple[str]:
        if self.schema_obj == None:
            return ('', '')
        if edge_label in self.subdir_map:
            return (self.subdir_map[edge_label]['source'], self.subdir_map[edge_label]['target'])
        return ('', '')

    def current_generation_tag(self) -> str:
        if not self.b_start_run:
            return ''
        res = pysgg.get_current_gentag(self.sgg_ptr)
        return res

    def current_generation_progress(self) -> float:
        if not self.b_start_run:
            return 0
        res = pysgg.get_current_progress(self.sgg_ptr)
        return res

    def is_generation_done(self) -> bool:
        if not self.b_start_run:
            return False
        res = pysgg.is_generation_done(self.sgg_ptr)
        return res

    def has_generation_start(self) -> bool:
        if not self.b_start_run:
            return False
        res = pysgg.has_generation_start(self.sgg_ptr)
        return res

    def __update_status__(self):
        if not self.b_start_run:
            self.b_stop_gen = False
        res = pysgg.get_current_progress(self.sgg_ptr)
        if res == 1.0:
            self.b_stop_gen = True

    def __check_whole__(self):
        if self.whole_impl == None and \
           ((self.is_running_mode and self.b_stop_gen) or (not self.is_running_mode)):
            self.whole_impl = IntegratedImpl(self.graph_name, self.subdir_map)

    def __check_subgraph__(self, edge_label: str):
        if edge_label not in self.subgraph_metric_impl:
            return
        if ((self.is_running_mode and self.b_stop_gen) or (not self.is_running_mode)) and \
            (self.subgraph_metric_impl[edge_label]['snap'] == None and \
             self.subgraph_metric_impl[edge_label]['nx'] == None and \
             self.subgraph_metric_impl[edge_label]['heat'] == None):
            num_src_nodes = self.subdir_map[edge_label]['n_source']
            num_tgt_nodes = self.subdir_map[edge_label]['n_target']
            src_tag = self.subdir_map[edge_label]['source']
            tgt_tag = self.subdir_map[edge_label]['target']
            self.subgraph_metric_impl[edge_label]['snap'] = SnapImpl(
                os.path.join(self.graph_name, edge_label), num_src_nodes=num_src_nodes,
                num_tgt_nodes=num_tgt_nodes, src_tag=src_tag, tgt_tag=tgt_tag
            )
            self.subgraph_metric_impl[edge_label]['nx'] = NXImpl(
                os.path.join(self.graph_name, edge_label), num_src_nodes=num_src_nodes,
                num_tgt_nodes=num_tgt_nodes, src_tag=src_tag, tgt_tag=tgt_tag
            )
            self.subgraph_metric_impl[edge_label]['heat'] = HeatMap(
                os.path.join(self.graph_name, edge_label),
                num_src_nodes=num_src_nodes, num_tgt_nodes=num_tgt_nodes
            )

    # ========== Get metrics ==========
    # edge_label == '' => The metric of the whole graph
    def get_in_out_deg_hist(self, edge_label: str) -> Tuple[List[List]]:
        '''
        ans[0]: in-degree list:  [[degree, #nodes]]
        ans[1]: out-degree list: [[degree, #nodes]]
        '''
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return ([], [])
        if edge_label == '':
            self.__check_whole__()
            if self.whole_impl != None:
                return self.whole_impl.get_in_out_degree_histogram()
        else:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['snap'] != None:
                return self.subgraph_metric_impl[edge_label]['snap'].get_in_out_degree_histogram()
        return ([], [])

    def get_eff_diam(self, edge_label: str) -> float:
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return 0.0
        if edge_label == '':
            self.__check_whole__()
            if self.whole_impl != None:
                return self.whole_impl.get_effective_diameter()
        if edge_label in self.subgraph_metric_impl:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['snap'] != None:
                return self.subgraph_metric_impl[edge_label]['snap'].get_effective_diameter()
        else:
            return 0.0

    def get_avg_spl(self, edge_label: str) -> float:
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return 0.0
        if edge_label == '':
            self.__check_whole__()
            if self.whole_impl != None:
                return self.whole_impl.get_average_path_length()
        if edge_label in self.subgraph_metric_impl:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['snap'] != None:
                return self.subgraph_metric_impl[edge_label]['snap'].get_average_path_length()
        return 0.0

    def get_assort_coeff(self, edge_label: str) -> float:
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return 0.0
        if edge_label == '':
            self.__check_whole__()
            if self.whole_impl != None:
                return self.whole_impl.get_assortativity_coefficient()
        if edge_label in self.subgraph_metric_impl:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['nx'] != None:
                return self.subgraph_metric_impl[edge_label]['nx'].get_assortativity_coefficient()
        return 0.0

    def get_cc(self, edge_label: str) -> float:
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return 0.0
        if edge_label == '':
            self.__check_whole__()
            if self.whole_impl != None:
                return self.whole_impl.get_clustering_coefficient()
        if edge_label in self.subgraph_metric_impl:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['nx'] != None:
                return self.subgraph_metric_impl[edge_label]['nx'].get_clustering_coefficient()
        return 0.0

    def get_heat_map(self, edge_label: str) -> List[List[int]]:
        if self.is_running_mode:
            self.__update_status__()
            if not self.b_stop_gen:
                return []
        if edge_label in self.subgraph_metric_impl:
            self.__check_subgraph__(edge_label)
            if self.subgraph_metric_impl[edge_label]['heat'] != None:
                return self.subgraph_metric_impl[edge_label]['heat'].get_heat()
        return []
