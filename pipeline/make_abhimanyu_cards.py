import sys, shutil, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import dl_cards as D, abhimanyu_content as L
from _guard import preflight
preflight()
R = pathlib.Path(__file__).resolve().parent.parent
D.shot(D.hook_card(chip=L.CHIP, head_lines=L.HEAD, body_lines=L.BODY, pill=L.PILL),
       D.OUT / "ab_1_hook.png")
D.shot(D.verse_card(n=1, total=2, **L.V1), D.OUT / "ab_2_verse1.png")
D.shot(D.verse_card(n=2, total=2, **L.V2), D.OUT / "ab_3_verse2.png")
D.shot(D.reflection_card("YOUR TURN", L.TURN), D.OUT / "ab_4_turn.png")
shutil.copy(R / "images" / "gita_grief" / "04_cta.png", D.OUT / "ab_5_cta.png")
print("cards done")
