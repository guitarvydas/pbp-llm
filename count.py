import sys
sys.path.insert (0, './pbp/kernel')
import kernel0d as zd

def install (reg):
    zd.register_component (reg, zd.mkTemplate ("Count", None, instantiate))
    
def instantiate (reg, owner, name, arg, template_data):
    name_with_id = zd.gensymbol ("Count")
    return zd.make_leaf (name_with_id, owner, None, arg, handler)

max = 3
count = 1

def reset_count ():
    global count
    count = 0

def inc_count ():
    global count
    count += 1

def handler (eh, mev):
    global count
    print (f'count handler count={count}', file=sys.stderr)
    if count < max:
        inc_count ()
        zd.send (eh, "less", mev.datum.v, mev)
    else:
        zd.send (eh, "final", mev.datum.v, mev)
        reset_count ()
        
