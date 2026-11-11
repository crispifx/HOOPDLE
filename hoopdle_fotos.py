"""HOOPDLE - genera hoopdle_fotos.json con fotos de jugadores y logos de equipos.

Uso (en tu computadora, con internet):
    pip install nba_api pillow requests
    python hoopdle_fotos.py
Después, en HOOPDLE: Menú > "Cargar fotos reales" > elegí hoopdle_fotos.json
Las fotos son de cdn.nba.com (las mismas de nba.com/players): uso personal.
"""
import base64, io, json, re, time, unicodedata
import requests
from PIL import Image
from nba_api.stats.static import players, teams

EXTRA = ["LeBron James","Michael Jordan","Kobe Bryant","Stephen Curry","Kevin Durant","Giannis Antetokounmpo","Nikola Jokic","Shaquille O'Neal","Tim Duncan","Magic Johnson","Larry Bird","Kareem Abdul-Jabbar","Hakeem Olajuwon","Dirk Nowitzki","Dwyane Wade","Kawhi Leonard","Luka Doncic","Shai Gilgeous-Alexander","Jayson Tatum","Allen Iverson","Steve Nash","Chris Paul","Kevin Garnett","Scottie Pippen","Charles Barkley","Karl Malone","John Stockton","Patrick Ewing","David Robinson","Wilt Chamberlain","Bill Russell","Jerry West","Victor Wembanyama","Anthony Edwards","Joel Embiid","Damian Lillard","James Harden","Russell Westbrook","Klay Thompson","Jimmy Butler","Anthony Davis","Manu Ginobili"]
key = lambda s: re.sub(r"[^a-z]", "", unicodedata.normalize("NFD", s).lower())
extra = {key(n) for n in EXTRA}
want = {key(p["full_name"]): p["id"] for p in players.get_players() if p["is_active"] or key(p["full_name"]) in extra}
H = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.nba.com/"}
out = {}
for i, (k, pid) in enumerate(want.items(), 1):
    try:
        r = requests.get(f"https://cdn.nba.com/headshots/nba/latest/260x190/{pid}.png", headers=H, timeout=15)
        if r.status_code != 200:
            continue
        im = Image.open(io.BytesIO(r.content)).convert("RGBA")
        bg = Image.new("RGB", im.size, (226, 214, 190)); bg.paste(im, mask=im.split()[3])
        w, h = bg.size; l = (w - h) // 2
        bg = bg.crop((l, 0, l + h, h)).resize((96, 96))
        buf = io.BytesIO(); bg.save(buf, "JPEG", quality=72)
        out[k] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception as e:
        print("skip", k, e)
    if i % 50 == 0: print(f"{i}/{len(want)}")
    time.sleep(0.12)
for t in teams.get_teams():
    try:
        r = requests.get(f"https://cdn.nba.com/logos/nba/{t['id']}/global/L/logo.svg", headers=H, timeout=15)
        if r.status_code == 200:
            out["team" + t["abbreviation"]] = "data:image/svg+xml;base64," + base64.b64encode(r.content).decode()
    except Exception as e:
        print("skip logo", t["abbreviation"], e)
json.dump(out, open("hoopdle_fotos.json", "w"))
print("Listo:", len(out), "fotos ->", "hoopdle_fotos.json")
