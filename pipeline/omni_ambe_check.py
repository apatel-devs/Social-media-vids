"""Re-render the exact reference post and diff its geometry against the
real video, so the rebuilt template can be verified rather than eyeballed."""
import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
import omni_kit as K
import numpy as np
from PIL import Image

REF = dict(
    struck="AMBE MA IS WEAK.",
    correction=["She is who they made", "after they lost."],
    reframe=["Mahishasura already had heaven.", "The gods had already run."],
    label="WHAT THE TEXT SAYS",
    paragraphs=[
        ["Shiva handed over his trident. Vishnu his discus.",
         "Indra the thunderbolt."],
        ["Not help. Their own weapons. They could not do it,",
         "so they built someone who could."],
    ],
    closing=["The name you say softest", "is the one they called last."],
    badge="DEVI MAHATMYAM 2",
)

TARGET = [(0, 9), (126, 171), (254, 321), (382, 445), (456, 519),
          (564, 615), (625, 676), (758, 777), (828, 863), (892, 927),
          (1022, 1071), (1088, 1133), (1189, 1235), (1248, 1295),
          (1346, 1417), (1462, 1487)]
NAMES = ["rule", "header", "struck", "corr1", "corr2", "refr1", "refr2",
         "label", "b1l1", "b1l2", "b2l1", "b2l2", "cl1", "cl2",
         "badge", "foot"]


def bands(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    d = np.abs(a - 255).sum(axis=2)
    rows = (d > 28).sum(axis=1)
    out, start = [], None
    for y, v in enumerate(rows):
        if v > 0 and start is None:
            start = y
        elif v == 0 and start is not None:
            if y - start > 4:
                out.append((start, y - 1))
            start = None
    if start is not None:
        out.append((start, len(rows) - 1))
    return out


if __name__ == "__main__":
    import omni_kit as K
    K.shot(K.page(**REF), K.OUT / "ambe_final.png", 9.0)
    got = bands(K.OUT / "ambe_final.png")
    for i, name in enumerate(NAMES):
        t = TARGET[i]; g = got[i] if i < len(got) else (0, 0)
        print(f"{name:8s} {str(t):>12s} {str(g):>12s}  "
              f"{g[0]-t[0]:+4d}/{g[1]-t[1]:+4d}")
