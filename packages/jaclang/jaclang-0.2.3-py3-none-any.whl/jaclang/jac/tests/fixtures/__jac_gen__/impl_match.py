from __future__ import annotations
from jaclang import jac_import as __jac_import__
from jaclang.jac.features import JacFeature as __JacFeature
__jac_import__(target='impl_match_impl', base_path=__file__)
from impl_match_impl import *
import impl_match_impl

@__JacFeature.make_architype('obj')
class Check:

    def run(self):
        1 / 0
Check().run()