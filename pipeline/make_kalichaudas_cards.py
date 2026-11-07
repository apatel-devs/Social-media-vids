import sys, shutil, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_cards as D, kalichaudas_content as L
from _guard import preflight
preflight()
R = pathlib.Path(__file__).resolve().parent.parent
D.shot(D.hook_card(chip=L.CHIP, head_lines=L.HEAD, body_lines=L.BODY, pill=L.PILL),
       D.OUT / "kc_1_hook.png")
D.shot(D.verse_card(n=1, total=2, **L.V1), D.OUT / "kc_2_verse1.png")
D.shot(D.verse_card(n=2, total=2, **L.V2), D.OUT / "kc_3_verse2.png")
D.shot(D.reflection_card("YOUR TURN", L.TURN), D.OUT / "kc_4_turn.png")
shutil.copy(R / "images" / "gita_grief" / "04_cta.png", D.OUT / "kc_5_cta.png")
print("cards done")
