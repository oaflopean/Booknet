from rake_nltk import Rake
from summarize import summarize
import json
page_text=str(open("/home/oaflopean/PycharmProjects/copypasta-october/texts/theotherfellowsshoes.txt", mode='r').read())
pg = {}

pg["keywords"] = []
r = Rake()
r.extract_keywords_from_text(page_text)
print("processing keywords")
phrases = r.get_ranked_phrases()
for phrase in phrases[:10]:
    pg["keywords"].extend(phrase.split(" "))
unique=set(pg["keywords"])
pg["keywords"]=list(unique)
summary = summarize(page_text, sentence_count=1, language='english')
pg["summary"] = summary

file = open("data/theotherfellowsshoes.json", mode="w")
json.dump(pg, file, indent=4, ensure_ascii=True)
