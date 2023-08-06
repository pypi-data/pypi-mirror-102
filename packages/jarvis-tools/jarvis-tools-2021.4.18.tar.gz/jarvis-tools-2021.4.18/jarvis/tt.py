# !pip install jarvis-tools, and restart runtime in the notebook if you haven't installed it yet
from jarvis.db.figshare import get_jid_data
from jarvis.core.graphs import Graph
from jarvis.core.atoms import Atoms
a=Atoms.from_dict(get_jid_data('JVASP-76299')['atoms'])
g=Graph.atom_dgl_multigraph(a,include_prdf_angles=True)
print (g.ndata['atom_features'].shape)
g=Graph.atom_dgl_multigraph(a)
print (g.ndata['atom_features'].shape)
