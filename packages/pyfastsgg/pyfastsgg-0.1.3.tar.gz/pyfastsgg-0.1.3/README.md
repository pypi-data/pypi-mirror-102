# PyFastSgg

Usage:

```python
from PyFastSgg import PyFastSGG

# set a JSON filename
gen_ins = PyFastSGG(json_filename)

# start generating ...
gen_ins.run()

# Is the generation done?
gen_ins.is_generation_done()

# After generation
# 1. get all node labels
label_list = gen_ins.get_all_node_names()

# 2. get the number of all nodes
n_nodes = gen_ins.get_num_nodes()

# 3. get the number of nodes with label 'lbl'
lbl_n_nodes = gen_ins.get_num_nodes('lbl')
```

