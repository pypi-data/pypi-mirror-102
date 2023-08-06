# -*- coding: utf-8 -*-


class Schema(object):
    GraphName = 'graph'
    # node schema
    NodeName = 'node'
    NodeLabel = 'label'
    NodeAmount = 'amount'
    # edge schema
    EdgeName = 'edge'
    EdgeLabel = 'label'
    EdgeAmount = 'amount'
    EdgeSourceNode = 'source'
    EdgeTargetNode = 'target'
    # community schema
    CommunityName = 'community'
    CommunityAmount = 'amount'
    # streaming
    GenerationRate = 'gr'
    # format
    StorageFormat = 'store_format'
    FormatADJ = 'ADJ'
    FormatCSR = 'CSR'
    FormatTSV = 'TSV'
