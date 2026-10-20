import json,urllib.request,time,os,subprocess,imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
d=json.load(open("audio_meta.json"))
start={"liszt":0,"schubert":0,"tchaikovsky":0,"brahms":0}
for k,v in d.items():
    out=f"audio/{k}.mp3"
    if os.path.exists(out): continue
    raw="raw/"+k+os.path.splitext(v["file"])[1]
    if not os.path.exists(raw):
        for t in range(4):
            try:
                time.sleep(3)
                r=urllib.request.Request(v["url"],headers={"User-Agent":"classical-site-build/1.0 (mbayen@college.harvard.edu)"})
                open(raw,"wb").write(urllib.request.urlopen(r,timeout=120).read()); break
            except Exception as e: print(k,"retry",e); time.sleep(20)
    p=subprocess.run([ff,"-y","-loglevel","error","-ss",str(start.get(k,0)),"-t","80","-i",raw,"-af","afade=t=in:d=1.5,afade=t=out:st=77:d=3","-ac","2","-ar","44100","-b:a","80k",out],capture_output=True,text=True)
    print(k,os.path.getsize(out)//1000 if os.path.exists(out) else "FAIL",p.stderr[:200])
