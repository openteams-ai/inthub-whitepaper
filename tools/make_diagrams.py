#!/usr/bin/env python3
"""Regenerate the whitepaper figures.

Source of truth for media/image1.png (architecture overview), media/image2.png
(validation lifecycle), and media/image3.png (the AI stack). Run from the repository root:

    python tools/make_diagrams.py

Requires Pillow (`pip install Pillow`). Colors match the whitepaper palette.
"""
import os
from PIL import Image, ImageDraw, ImageFont

NAVY = (27, 42, 74)        # 1b2a4a
TEAL = (14, 124, 123)      # 0e7c7b
LIGHT = (213, 232, 240)    # d5e8f0
GRAY = (244, 246, 249)     # f4f6f9
INK = (34, 34, 34)         # 222222
WHITE = (255, 255, 255)
BORDER = NAVY

OUT_DIR = 'media'
ARCH_OUT = os.path.join(OUT_DIR, 'image1.png')       # architecture overview
LIFECYCLE_OUT = os.path.join(OUT_DIR, 'image2.png')  # validation lifecycle

# Font discovery: first match wins (Linux DejaVu, macOS system fonts).
_BOLD_CANDIDATES = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial Bold.ttf',
]
_REG_CANDIDATES = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/System/Library/Fonts/Supplemental/Arial.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial.ttf',
]

def _first(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    raise SystemExit('No usable font found; edit the candidate lists in tools/make_diagrams.py')

FB = _first(_BOLD_CANDIDATES)
FR = _first(_REG_CANDIDATES)

def font(path, size):
    return ImageFont.truetype(path, size)

def ctext(d, xy, text, f, fill):
    """Draw text centered on xy."""
    bb = d.textbbox((0, 0), text, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text((xy[0] - w / 2 - bb[0], xy[1] - h / 2 - bb[1]), text, font=f, fill=fill)

os.makedirs(OUT_DIR, exist_ok=True)

# ================================================================ Figure 1: architecture
W, H = 1890, 940
img = Image.new('RGB', (W, H), WHITE)
d = ImageDraw.Draw(img)
f_title = font(FB, 44)
f_sub = font(FR, 36)

bx0, bx1 = 60, 1400
layers = [
    ('LAYER 3 — ECONOMY', 'The Marketplace: discover, exchange, monetize'),
    ('LAYER 2 — EXECUTION', 'Frames  ·  Cogs  ·  Ops'),
    ('LAYER 1 — INFRASTRUCTURE', 'Intelligence Hub  ·  Nebari  ·  Nebi'),
]
box_h, gap, top = 250, 60, 40
for i, (t, s) in enumerate(layers):
    y0 = top + i * (box_h + gap)
    d.rounded_rectangle([bx0, y0, bx1, y0 + box_h], radius=18, fill=LIGHT, outline=BORDER, width=4)
    ctext(d, ((bx0 + bx1) / 2, y0 + box_h / 2 - 40), t, f_title, NAVY)
    ctext(d, ((bx0 + bx1) / 2, y0 + box_h / 2 + 42), s, f_sub, TEAL)
    if i < 2:
        cx = (bx0 + bx1) / 2
        d.line([cx, y0 + box_h + 6, cx, y0 + box_h + gap - 6], fill=TEAL, width=6)

# accountability plane bar
px0, px1 = 1520, 1830
d.rounded_rectangle([px0, top, px1, top + 3 * box_h + 2 * gap], radius=18, fill=NAVY)
for i in range(3):
    y = top + i * (box_h + gap) + box_h / 2
    d.line([bx1 + 4, y, px0 - 4, y], fill=TEAL, width=6)
    d.polygon([(px0 - 4, y), (px0 - 26, y - 12), (px0 - 26, y + 12)], fill=TEAL)

def vtext(text, f, fill):
    bb = ImageDraw.Draw(Image.new('RGB', (10, 10))).textbbox((0, 0), text, font=f)
    ti = Image.new('RGBA', (bb[2] - bb[0] + 20, bb[3] - bb[1] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(ti).text((10 - bb[0], 10 - bb[1]), text, font=f, fill=fill)
    return ti.rotate(90, expand=True)

t1 = vtext('ACCOUNTABILITY  PLANE', font(FB, 46), WHITE)
t2 = vtext('Guards  ·  Gates  ·  Tracks', font(FR, 38), LIGHT)
cy = top + (3 * box_h + 2 * gap) / 2
img.paste(t1, (int((px0 + px1) / 2 - t1.width / 2 - 28), int(cy - t1.height / 2)), t1)
img.paste(t2, (int((px0 + px1) / 2 - t2.width / 2 + 46), int(cy - t2.height / 2)), t2)
img.save(ARCH_OUT)

# ================================================================ Figure 2: lifecycle
W2, H2 = 1890, 760
img2 = Image.new('RGB', (W2, H2), WHITE)
d2 = ImageDraw.Draw(img2)
f_st = font(FB, 40)
f_sc = font(FR, 28)
f_gate = font(FB, 26)
f_bar = font(FB, 36)
f_loop = font(FR, 30)

d2.rounded_rectangle([60, 30, 1830, 100], radius=14, fill=GRAY, outline=TEAL, width=3)
ctext(d2, (945, 65), 'GUARDS — verification checks run at every stage', font(FB, 32), TEAL)

stages = [('PRE-FLIGHT', 'Is this Op allowed?'),
          ('IN-FLIGHT', 'Within policy?'),
          ('POST-RUN', 'Ready for action?'),
          ('CONTINUOUS', 'Is quality holding?')]
sw, sh, sy = 380, 210, 160
sx = [60, 523, 987, 1450]
for i, ((t, s), x) in enumerate(zip(stages, sx)):
    d2.rounded_rectangle([x, sy, x + sw, sy + sh], radius=16, fill=LIGHT, outline=BORDER, width=4)
    ctext(d2, (x + sw / 2, sy + sh / 2 - 34), t, f_st, NAVY)
    ctext(d2, (x + sw / 2, sy + sh / 2 + 38), s, f_sc, INK)
    if i < 3:
        x0, x1 = x + sw, sx[i + 1]
        ymid = sy + sh / 2
        d2.line([x0 + 6, ymid, x1 - 30, ymid], fill=NAVY, width=6)
        d2.polygon([(x1 - 8, ymid), (x1 - 34, ymid - 14), (x1 - 34, ymid + 14)], fill=NAVY)
        gx = (x0 + x1) / 2
        r = 34
        d2.polygon([(gx, ymid - r), (gx + r, ymid), (gx, ymid + r), (gx - r, ymid)], fill=NAVY)
        ctext(d2, (gx, ymid + r + 26), 'Gate', f_gate, NAVY)

ly = sy + sh + 60
d2.line([sx[3] + sw / 2, sy + sh + 4, sx[3] + sw / 2, ly], fill=TEAL, width=5)
d2.line([sx[0] + sw / 2, ly, sx[3] + sw / 2, ly], fill=TEAL, width=5)
d2.line([sx[0] + sw / 2, ly, sx[0] + sw / 2, sy + sh + 30], fill=TEAL, width=5)
d2.polygon([(sx[0] + sw / 2, sy + sh + 6), (sx[0] + sw / 2 - 14, sy + sh + 32),
            (sx[0] + sw / 2 + 14, sy + sh + 32)], fill=TEAL)
ctext(d2, (945, ly + 32),
      'learning loop — Tracks feed Organizational Memory; Frames, Cogs, Ops, and Guards improve',
      f_loop, TEAL)

d2.rounded_rectangle([60, H2 - 100, 1830, H2 - 30], radius=14, fill=NAVY)
ctext(d2, (945, H2 - 65), 'TRACK — evidence recorded across the entire lifecycle', f_bar, WHITE)
img2.save(LIFECYCLE_OUT)

print(f'wrote {ARCH_OUT} {img.size} and {LIFECYCLE_OUT} {img2.size}')

# ================================================================ Figure 1: the AI stack (image3)
STACK_OUT = os.path.join(OUT_DIR, 'image3.png')
AMBER = (196, 132, 24); PALE_AMBER = (252, 240, 214); DARK_AMBER = (120, 78, 10); MID_AMBER = (150, 100, 20)
MUTED = (107, 114, 128); MID = (170, 190, 205)
FI = _first(['/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', '/System/Library/Fonts/Supplemental/Arial Italic.ttf', FR])
def ltext(d, xy, text, f, fill):
    bb = d.textbbox((0, 0), text, font=f)
    d.text((xy[0] - bb[0], xy[1] - (bb[3]-bb[1])/2 - bb[1]), text, font=f, fill=fill)

def make_stack():
    W, H = 2000, 1640
    img = Image.new('RGB', (W, H), WHITE)
    d = ImageDraw.Draw(img)

    layers = [  # bottom -> top
        ('COMPUTE',        'chips, accelerators, networking, storage',
         'Open ecosystem', 'GPUs · CPUs · cloud, on-prem, edge', 'ecosystem'),
        ('INFRASTRUCTURE', 'orchestration, identity, secrets, observability',
         'Open source contributions', 'Nebari · NIC · Kubernetes-native packs — many contributors', 'contribute'),
        ('DATA',           'collect, store, prepare; retrieval',
         'Shared abstraction: Frames', 'owned context · Organizational Memory · connectors', 'shared'),
        ('MODELS',         'develop, fine-tune, serve',
         'Open source contributions', 'open weights · model serving · inference gateway', 'contribute'),
        ('WORK',           'agents, tools, runtimes',
         'Shared abstraction: Cogs', 'agent runtime · tools · Nebi packaging', 'shared'),
        ('APPLICATION',    'agentic apps and workflows',
         'Shared abstraction: Ops', 'horizontal Ops (many industries) · vertical Ops (one org’s SOPs)', 'shared'),
        ('OUTCOMES',       'the work of the organization',
         'Owned by the organization', 'closed books · onboarded customers · vendors reviewed', 'ecosystem'),
    ]
    style = {
        'ecosystem':  dict(fill=GRAY,  outline=MID,   t=MUTED, s=MUTED),
        'contribute': dict(fill=LIGHT, outline=NAVY,  t=NAVY,  s=TEAL),
        'shared':     dict(fill=NAVY,  outline=NAVY,  t=WHITE, s=LIGHT),
        'products':   dict(fill=PALE_AMBER, outline=AMBER, t=DARK_AMBER, s=MID_AMBER),
    }

    LX0, LX1 = 130, 830
    RX0, RX1 = 890, 1560
    box_h, gap, top = 138, 20, 170
    n = len(layers)
    f_ind = font(FB, 38); f_indsub = font(FR, 24)
    f_part = font(FB, 30); f_ex = font(FR, 20)

    ctext(d, (W/2, 52), 'THE AI STACK — AND THE SHARED ABSTRACTIONS OF A DISTRIBUTED AI ECONOMY', font(FB, 40), NAVY)
    ctext(d, ((LX0+LX1)/2, 118), 'The stack as commonly described in industry', font(FI, 26), MUTED)
    ctext(d, ((RX0+RX1)/2, 118), 'What the ecosystem shares and builds', font(FI, 26), MUTED)

    def layer_y(idx): return top + (n - 1 - idx) * (box_h + gap)

    for idx, (name, desc, part, ex, role) in enumerate(layers):
        y = layer_y(idx); st = style[role]
        d.rounded_rectangle([LX0, y, LX1, y + box_h], radius=14, fill=GRAY, outline=MID, width=3)
        ctext(d, ((LX0+LX1)/2, y + 48), name, f_ind, NAVY)
        ctext(d, ((LX0+LX1)/2, y + 96), desc, f_indsub, MUTED)
        d.rounded_rectangle([RX0, y, RX1, y + box_h], radius=14, fill=st['fill'], outline=st['outline'], width=3)
        ctext(d, ((RX0+RX1)/2, y + 46), part, f_part, st['t'])
        ctext(d, ((RX0+RX1)/2, y + 94), ex, f_ex, st['s'])
        d.line([LX1 + 6, y + box_h/2, RX0 - 6, y + box_h/2], fill=MID, width=3)

    # accountability plane (spans INFRASTRUCTURE..APPLICATION)
    px0, px1 = 1620, 1790
    p_top = layer_y(5); p_bot = layer_y(1) + box_h
    d.rounded_rectangle([px0, p_top, px1, p_bot], radius=16, fill=NAVY)
    t1 = vtext('ACCOUNTABILITY PLANE', font(FB, 32), WHITE)
    t2 = vtext('Guards · Gates · Tracks  —  the industry’s observability & governance', font(FR, 22), LIGHT)
    cy = (p_top + p_bot) / 2
    img.paste(t1, (int((px0+px1)/2 - t1.width/2 - 24), int(cy - t1.height/2)), t1)
    img.paste(t2, (int((px0+px1)/2 - t2.width/2 + 26), int(cy - t2.height/2)), t2)

    # products & services band (spans INFRASTRUCTURE..OUTCOMES)
    qx0, qx1 = 1820, 1960
    q_top = layer_y(6); q_bot = layer_y(1) + box_h
    d.rounded_rectangle([qx0, q_top, qx1, q_bot], radius=16, fill=PALE_AMBER, outline=AMBER, width=3)
    u1 = vtext('PRODUCTS & SERVICES', font(FB, 26), DARK_AMBER)
    u2 = vtext('open & commercial — built by many, integrated into owned Hubs', font(FR, 20), MID_AMBER)
    cy2 = (q_top + q_bot) / 2
    img.paste(u1, (int((qx0+qx1)/2 - u1.width/2 - 20), int(cy2 - u1.height/2)), u1)
    img.paste(u2, (int((qx0+qx1)/2 - u2.width/2 + 24), int(cy2 - u2.height/2)), u2)

    # left bracket: an organization's Intelligence Hub spans INFRASTRUCTURE..APPLICATION
    hb_top = layer_y(5); hb_bot = layer_y(1) + box_h
    bx = 92
    d.line([bx, hb_top + 6, bx, hb_bot - 6], fill=TEAL, width=6)
    d.line([bx, hb_top + 6, bx + 20, hb_top + 6], fill=TEAL, width=6)
    d.line([bx, hb_bot - 6, bx + 20, hb_bot - 6], fill=TEAL, width=6)
    vt = vtext('AN ORGANIZATION’S INTELLIGENCE HUB', font(FB, 24), TEAL)
    img.paste(vt, (bx - 44, int((hb_top + hb_bot)/2 - vt.height/2)), vt)

    # examples strip
    ly = layer_y(0) + box_h + 34
    d.rounded_rectangle([LX0, ly, qx1, ly + 124], radius=14, fill=PALE_AMBER, outline=AMBER, width=2)
    ctext(d, ((LX0+qx1)/2, ly + 26), 'Products & services in the economy — examples, open and commercial, built by many', font(FB, 24), DARK_AMBER)
    ctext(d, ((LX0+qx1)/2, ly + 62),
          'Hub experience apps (e.g., a desktop/web application)  ·  compute & model management  ·  Track stores & audit  ·  Gate & review consoles',
          font(FR, 21), MID_AMBER)
    ctext(d, ((LX0+qx1)/2, ly + 96),
          'Op & Cog builders  ·  Guard libraries  ·  specialized Ops built for a segment or an organization  ·  integration & operations services',
          font(FR, 21), MID_AMBER)

    # legend
    ly2 = ly + 124 + 30
    sw = 28
    items = [('ecosystem', 'Open ecosystem'), ('contribute', 'Open source contributions'),
             ('shared', 'Shared abstractions'), ('products', 'Products & services (open & commercial)')]
    x = LX0; f_leg = font(FR, 23)
    for role, label in items:
        st = style[role]
        d.rounded_rectangle([x, ly2, x + sw, ly2 + sw], radius=6, fill=st['fill'], outline=st['outline'], width=2)
        ltext(d, (x + sw + 12, ly2 + sw/2), label, f_leg, INK)
        x += sw + 12 + d.textbbox((0, 0), label, font=f_leg)[2] + 56
    ctext(d, (W/2, ly2 + sw + 42),
          'Layer names draw on common industry framings of the AI stack (for example, IBM’s); this paper learns from them without following any one literally.',
          font(FI, 21), MUTED)

    img.save(STACK_OUT)
    print(f'wrote {STACK_OUT} {img.size}')


make_stack()

