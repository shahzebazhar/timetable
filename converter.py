import pandas as pd
from json import load
from html2image import Html2Image
from PIL import Image
import numpy as np

data = load(open("TimeTable.json"))

indices = list(data.keys())
timings = list(data[indices[0]].keys())
newtimings = [f"{timings[i]} - {timings[i + 1]}" for i in range(len(timings) - 1)]
newtimings.append(timings[-1])


time_dict = {time:[data[idx][time] if data[idx][time] != None else np.nan for idx in indices] for time in timings}


df = pd.DataFrame(time_dict)

df["Days"] = indices
df.set_index("Days", inplace=True)
df.index.name = None

df.rename(columns=dict(zip(timings, newtimings)), inplace=True)
df.dropna(how='all', axis=1, inplace=True)

df.fillna("", inplace=True)

df.to_html("index.html")

hti = Html2Image()
htext_color = "#FFFFFF"
btext_color = "#000000"
bg_color = "#FFFFFF" # FEC5E5
time_color = "#006400" # A44CD3
day_color = "#3cb371" # E090DF
css = "table {background: %s;} th {color: %s;} td {color: %s;} thead {background: %s;} tbody > tr > th {background: %s;} tr {height: 60px;}" % (
    bg_color, htext_color, btext_color, time_color, day_color)
html = open("index.html", 'r').read()
html = html.replace("text-align: right;", "text-align: center;")

hti.screenshot(html_str=html, css_str=css, save_as="ttable.png", size=(1080, 445))

img = Image.open("ttable.png")
bbox = img.getbbox()
img = img.crop(bbox)
img.save("ttable.png") 

print("COMPLETED")