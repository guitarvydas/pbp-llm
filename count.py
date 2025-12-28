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
    
        
