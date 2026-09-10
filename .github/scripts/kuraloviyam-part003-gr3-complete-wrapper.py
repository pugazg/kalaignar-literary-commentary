from pathlib import Path

path=Path('.github/scripts/kuraloviyam-part003-gr3-complete.py')
code=path.read_text(encoding='utf-8')
for old in [
"g=must_replace(g,'| அவர்வயின்விதும்பல் | Longing for His Return |','| அவர்வயின்விதும்பல் / அவர் வயின் விதும்பல் | Longing for His Return |','chapter 127 variant',1)\n",
"g=must_replace(g,'| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் / கனவுநிலை உரைத்தல் | Speaking of the Dream State |','| கனவு நிலையுரைத்தல் / கனவுநிலையுரைத்தல் / கனவுநிலை உரைத்தல் / கனவு நிலை உரைத்தல் | Speaking of the Dream State |','chapter 122 variant',1)\n",
"g=must_replace(g,'| ஆள்வினையுடைமை | Diligent Effort |','| ஆள்வினையுடைமை / ஆள்வினை உடைமை | Diligent Effort |','chapter 62 variant',1)\n",
]:
    if old not in code:
        raise SystemExit('wrapper precondition missing variant line')
    code=code.replace(old,'')
old="addition=anchor+'\\n| துறவு | Renunciation | Chapter 35 label on scan 289. |\\n| சுற்றந் தழால் | Cherishing Kindred | Chapter 53 label on scan 293. |'"
new="addition=anchor+'\\n| துறவு | Renunciation | Chapter 35 label on scan 289. |\\n| சுற்றந் தழால் | Cherishing Kindred | Chapter 53 label on scan 293. |\\n| அவர் வயின் விதும்பல் | Longing for His Return | Chapter 127 source-form variant on scans 291 and 295; maps to the established controlled label. |\\n| கனவு நிலை உரைத்தல் | Speaking of the Dream State | Chapter 122 source-form variant on scan 299; maps to the established controlled label. |\\n| ஆள்வினை உடைமை | Diligent Effort | Chapter 62 source-form variant on scan 302; maps to the established controlled label. |'"
if old not in code:
    raise SystemExit('wrapper precondition missing addition line')
code=code.replace(old,new)
exec(compile(code,str(path),'exec'))
