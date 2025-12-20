import sys
sys.path.insert (0, './pbp/kernel')
import kernel0d as zd


class Counter:
    def __init__ (self):
        self.max = 5
        self.count = 1
        
    def reset (self):
        self.count = 1
        
    def inc (self):
        self.count += 1
        
def handler (eh, mev):
    self = eh.instance_data
    print (f'count={self.count}', file=sys.stderr)
    if self.count < self.max:
        self.inc ()
        zd.send (eh, "less", mev.datum.v, mev)
    else:
        zd.send (eh, "final", mev.datum.v, mev)
        self.reset ()
        
def instantiate (reg, owner, name, arg, template_data):
    name_with_id = zd.gensymbol ("Count")
    self = Counter ()
    return zd.make_leaf (name_with_id, owner, self, arg, handler)

def install (reg):
    zd.register_component (reg, zd.mkTemplate ("Count", None, instantiate))
    
        
# zd.mkTemplate (<name>, <template descriptor>, <template instantiator function>)
# zd.make_leaf (<name with id>, <owner>, <instance (self)>, <arg==name of part as a string (used for implementing JIT parts in the kernel)>, <handler>) where the signature of handler is `handler (eh, mev)`, i.e. a part desriptor ("eh") and the triggering mevent (mev). Note that handler is /not/ a Python method, hence, is not given a "self" argument. Instance-specific data can be gleaned from `eh.instance_data` which must be set up during `instantiate` and passed in as the 3rd arg to `instantiate` (if needed, else None)
