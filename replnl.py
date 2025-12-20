#!/usr/bin/env python3
import sys
sys.path.insert(0, './pbp/kernel')
import kernel0d as zd


def handler (eh, mev):
    text = mev.datum.v
    zd.send (eh, "", text.replace ('~', '\n'), mev)

def instantiate (reg,owner,name, arg, template_data):
    name_with_id = zd.gensymbol ( "Replace NLs")
    return zd.make_leaf ( name_with_id, owner, None, arg, handler)

# define template
def install (reg):
    zd.register_component (reg, zd.mkTemplate ("Replace NLs", None, instantiate))

