import xml.etree.ElementTree as ET
import yaml

# OPML読み込み
tree = ET.parse("dynalist-2025-11-22_chapt2.opml")
root = tree.getroot()

sql_list = []

def traverse_outline(outline):
    note = outline.attrib.get('_note')
    text = outline.attrib.get('text')
    if note:
        sql_list.append({'question': text, 'sql': note.strip()})
    for child in outline.findall('outline'):
        traverse_outline(child)

# body 内の outline から開始
body = root.find('body')
for top_outline in body.findall('outline'):
    traverse_outline(top_outline)

# YAMLに変換して保存
with open("output.yaml", "w", encoding="utf-8") as f:
    yaml.dump(sql_list, f, allow_unicode=True)