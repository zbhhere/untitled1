import json
import re
from pyquery import PyQuery as py

txt='''<li><a href="/Business_Etiquette_1.html">Business Etiquette</a></li>
<li><a href="/Words_And_Idioms_1.html">Words And Idioms</a></li>
<li><a href="/American_English_Mosaic_1.html">American English Mosaic</a></li>
<li><a href="/Popular_American_1.html">Popular American</a></li>
<li><a href="/Sports_English_1.html">Sports English</a></li>
<li><a href="/Go_English_1.html">Go English</a></li>
<li><a href="/Word_Master_1.html">Wordmaster</a></li>
<li><a href="/American_Cafe_1.html">American Cafe</a></li>
<li><a href="/Intermediate_American_English_1.html">Intermediate American Enlish</a></li>
</ul>
</div>

<div id="right_box">
<div id="title"><h1>Health Disaster Looms as Gaza Struggles to Treat Wounded</h1></div>
<div id="Content_VOA">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:inline-block;width:336px;height:280px"
     data-ad-client="ca-pub-3585518775245612"
     data-ad-slot="4281465902"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

<div id="playbar">
<script language="javascript" type="text/javascript">
    Player("/201408/health-disaster-looms-as-gaza-struggles-to-treat-wounded.mp3");
</script></div>
<div id="menubar">
<a id="mp3" href="http://downdb.51voa.com/201408/health-disaster-looms-as-gaza-struggles-to-treat-wounded.mp3" title="鼠标右键点击下载"></a><a id="help" href="/intro/help.html" target=_blank></a><BR></div>
<div id="content"><span class=byline>Scott Bobb</span><br><span class=datetime>Aug-usté：? 06,2014</span><br><br><strong>AL-SHIFA HOSPITAL, GAZA — The (United) Nations has warned that Gaza faces a health disaster, following the four-week long conflict with Israel that began with an Israeli –operation to destroy Hamas rockets and infiltration tunnels. Many hospitals and clinics were damaged in the fighting. All are overwhelmed with wounded, including Gaza's largest hospital, al-Shifa.<br><br></strong>Officials say al-Shifa now treats only the wounded from the conflict.
<div class=contentImage><img src="/images/201408/da8ed138-f40a-4dcd-b0c5-936a785ea97e_tv_w268_h360.jpg" alt="Health Disaster Looms as Gaza Struggles to Treat Wounded"></div>Routine illnesses and surgeries are referred to other facilities.<br><br>Wounded lie in beds in departments once dedicated to gynecology and internal medicine. Some wait on gurneys in the hallways, others on the floor.<br><br>The pediatric ward is full. One girl was hit by shrapnel from a shell. Her mother, Om Suhair Khalifa, says her sister and two brothers are in critical condition in intensive care.<br><br>"Their father asked them to sleep next to us. But they refused. They wanted to sleep with their dolls. We worried all night. Suddenly we heard something land on our house. We thought it had happened to our neighbors. Then we saw smoke everywhere," recalls Khalifa.<br><br>Student nurse Ragda Samour has been volunteering at the hospital since the conflict began. She works two eight-hour shifts a day, like everybody else.<br><br>“The majority of the cases have head injuries, brain damage. Others have amputated hands or legs. We have martyrs [reference to the dead], God have mercy on them. But the injuries are very, very hard to bear,” says Samour.<br><br>Some of the wounded are being sent home early. There are not enough beds, supplies or staff, says pediatrician Basel Baker.<br><br>"But this is not the biggest part of our suffering. The biggest part is the psychological part. We see children. We see babies with injuries, totally disabled. Those who live will be disabled. It's a disaster. You can't [bear] to see…," says Baker.<br><br>The United Nations says one-third of Gaza’s hospitals and clinics have been damaged. A dozen health workers have been killed or wounded in the conflict.<br><br>As a result, humanitarian groups say Gaza’s medical system will need outside support for a very long time.</div>
<div id="Bottom_VOA">
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3585518775245612"
     data-ad-slot="2911046368"></ins>
'''
# pattern=re.compile(r'["]+[\s]*["]+',re.S)
#
# if re.match(pattern,txt):
# print("hehe")
doc=py(txt)
pattern3 = re.compile(r'[\s]*', re.S)
pattern2=re.compile(r'[\u4e00-\u9fa5\/\\‘’！？，。“”…—–‐：|\\\"\[\]\n]+',re.S)
content = doc('p').text()
# print(content)
result=re.match(pattern3, content)
# print(result)
if re.match(pattern3, content):
    content=doc('div').filter('#content').text()
    content=re.sub(pattern2,'',content)
    with open('cnn.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False))



    key = 'hello python'
    key = align(key, True)
    key = key.encode('utf-8')
    aes = pyaes.AESModeOfOperationCTR(key)




    decrypted_filename = aes.decrypt(a2b_hex(in_filename)).decode('utf-8')
    out_filename = 'VOA/' + decrypted_filename
    print(out_filename)
    print(in_filename)
    in_filename='encryp_files/'+in_filename
    ff = open(in_filename, 'r')
    ciphertext = ff.read()
    ff.close()


    decrypted = aes.decrypt(a2b_hex(ciphertext)).decode('utf-8')
    print(decrypted)
    fw = open(out_filename, 'wb')
    fw.write(decrypted)
    fw.close()