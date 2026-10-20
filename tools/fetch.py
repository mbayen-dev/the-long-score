import json,urllib.request,urllib.parse,base64,os,io
def get(u,raw=False):
    r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (classical-timeline-build)"})
    d=urllib.request.urlopen(r,timeout=40).read()
    return d if raw else json.loads(d)
names=["Vivaldi","Bach","Handel","Haydn","Mozart","Beethoven","Schubert","Berlioz","Chopin","Schumann","Liszt","Verdi","Wagner","Brahms","Tchaikovsky","Dvořák","Grieg","Mahler"]
art={"Vivaldi":111074,"Bach":95998,"Handel":100356,"Haydn":51577,"Mozart":16485,"Beethoven":109938,"Schubert":25806,"Berlioz":81505,"Chopin":56905,"Schumann":81512,"Liszt":76571,"Verdi":84076,"Wagner":90048,"Brahms":81521,"Tchaikovsky":18951,"Dvořák":25865,"Grieg":146701,"Mahler":154235}
eras={"Baroque":60755,"Classical":51130,"Romantic":879}
out={"composers":[],"eras":{}}
def artinfo(i):
    a=get(f"https://api.artic.edu/api/v1/artworks/{i}?fields=id,title,artist_title,artist_display,date_display,medium_display,image_id,place_of_origin,credit_line,dimensions")["data"]
    img=get(f"https://www.artic.edu/iiif/2/{a['image_id']}/full/700,/0/default.jpg",True)
    a["img"]="data:image/jpeg;base64,"+base64.b64encode(img).decode()
    return a
for n in names:
    c=get("https://api.openopus.org/composer/list/search/"+urllib.parse.quote(n)+".json")["composers"]
    c=[x for x in c if x["name"].lower()==n.lower()] or c
    c=c[0]
    w=get(f"https://api.openopus.org/work/list/composer/{c['id']}/genre/Recommended.json").get("works",[])
    pop=[x for x in w if x.get("popular")=="1"] 
    works=[{"title":x["title"],"sub":x.get("subtitle",""),"genre":x["genre"]} for x in (pop+[x for x in w if x not in pop])[:8]]
    port=get(c["portrait"].replace("\\/","/"),True)
    c["portrait_data"]="data:image/jpeg;base64,"+base64.b64encode(port).decode()
    c["works"]=works
    c["art"]=artinfo(art[n])
    out["composers"].append(c); print(n,c["id"],c["epoch"],len(works),len(port))
for e,i in eras.items(): out["eras"][e]=artinfo(i)
json.dump(out,open("data.json","w"),ensure_ascii=False)
print(os.path.getsize("data.json"))
