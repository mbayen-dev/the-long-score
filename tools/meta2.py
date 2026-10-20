import re
import json,urllib.request,urllib.parse,time,os
files={
"vivaldi":"Vivaldi - Four Seasons 1 Spring mvt 1 Allegro - John Harrison violin.oga",
"bach":"Bach - Cello Suite no. 1 in G major, BWV 1007 - I. Prélude.ogg",
"handel":"Handel's Water Music - 12. Alla hornpipe - Chamber Orchestra - United States Marine Band.opus",
"haydn":"Haydn; Symphony No. 94 \"Surprise\", 2. Andante.ogg",
"mozart":"W. A. Mozart - Andante from Piano Concerto K 467 b. 1-23 fading.ogg",
"beethoven":"Ludwig van Beethoven - symphony no. 5 in c minor, op. 67 - i. allegro con brio.ogg",
"schubert":"Schubert Symphony No. 8 'Unfinished' - 1- Allegro moderato in B minor.ogg",
"berlioz":"Hector Berlioz - Symphonie fantastique, op. 14 - 4. Marche au supplice (Igor Markevitch, Orchestre Lamoureux, 1962).ogg",
"chopin":"Chopin Nocturne Op 9 No 2.ogg",
"schumann":"Schumann; Carnaval.ogg",
"liszt":"Hungarian Rhapsody No 2.ogg",
"verdi":"La Traviata - Act 1 - Libiamo ne' lieti calici.ogg",
"wagner":"Richard Wagner - Ride of the Valkyries.ogg",
"brahms":"Brahms, Symphony No. 4 in E Minor, Op. 98 - I. Allegro Non Troppo.ogg",
"tchaikovsky":"Peter Ilyich Tchaikovsky- Swan Lake- Extract from Act 2.ogg",
"dvorak":"Antonin Dvorak - symphony no. 9 in e minor 'from the new world', op. 95 - ii. largo.ogg",
"grieg":"Musopen - In the Hall Of The Mountain King.ogg",
"mahler":"Mahler Symphony No. 5, IV. Adagietto.ogg"}

out=json.load(open("audio_meta.json")) if os.path.exists("audio_meta.json") else {}
for k,f in files.items():
    if k in out: continue
    time.sleep(4)
    u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","titles":"File:"+f,"prop":"imageinfo","iiprop":"url|size|extmetadata","format":"json"})
    r=urllib.request.Request(u,headers={"User-Agent":"classical-site-build/1.0 (mbayen@college.harvard.edu)"})
    try: p=list(json.load(urllib.request.urlopen(r))["query"]["pages"].values())[0]
    except Exception as ex:
        print(k,"ERR",ex); time.sleep(30); continue
    if "imageinfo" not in p: print(k,"MISSING"); continue
    ii=p["imageinfo"][0];m=ii["extmetadata"]
    out[k]={"file":f,"url":ii["url"],"size":ii["size"],"lic":m.get("LicenseShortName",{}).get("value"),"artist":re.sub("<[^>]+>","",m.get("Artist",{}).get("value",""))[:90].strip(),"page":ii["descriptionurl"]}
    json.dump(out,open("audio_meta.json","w"),ensure_ascii=False)
    print(k,ii["size"]//1000,"KB",out[k]["lic"],"|",out[k]["artist"][:60])
