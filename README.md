# Voynich manuscript research tools

## Introduction

This repository contains some functionality to load Voynich manuscript (VMS) transliterations from file and perform some research on it.

Analysis and testing of hypotheses is provided as a set of independent tests. They can be run be executing `pytest` from the repository root directory.

## Word distribution

This is the output of the word distribution test operating on the Takeshi Takahashi (TT) transliteration:

```
Found 8530 unique words out of 36377 total words

#times    #words    words     
------------------------------
805       1         daiin     
525       1         ol        
495       1         chedy     
456       1         aiin      
424       1         shedy     
380       1         chol      
348       1         or        
344       1         ar        
339       1         chey      
308       1         qokeey    
301       1         qokeedy   
297       1         dar       
277       1         qokain    
276       1         shey      
265       1         qokedy    
262       1         qokaiin   
253       1         al        
243       1         dal       
226       1         dy        
209       1         okaiin    
205       1         chor      
189       1         dain      
188       1         qokal     
174       3         shol, okeey, cheey
166       1         cheol     
154       1         otedy     
150       1         otaiin    
149       1         qokar     
148       1         qol       
143       1         chdy      
142       1         sheey     
141       1         okain     
139       2         qoky, otar
137       1         otal      
136       2         chy, saiin
135       1         oteey     
134       1         chckhy    
133       1         okal      
124       1         okar      
121       1         sho       
119       1         lchedy    
116       1         okedy     
113       1         sheol     
111       1         dol       
110       1         oty       
105       2         cthy, qokey
103       1         okeedy    
102       1         qokol     
100       1         dair      
99        1         oteedy    
98        1         cheor     
95        1         otain     
93        1         shy       
92        1         shor      
91        1         qotedy    
90        1         chody     
89        1         dam       
88        1         oky       
87        2         am, ain   
86        1         cheody    
83        2         sar, sheedy
82        1         qoty      
81        1         otol      
78        2         okol, chcthy
75        2         qotaiin, raiin
74        1         qoteedy   
73        1         air       
71        1         char      
70        1         dor       
68        1         qokchy    
67        1         sol       
66        1         sain      
65        3         kaiin, cheo, okeol
64        1         qotain    
63        2         cheky, qotar
62        2         qotchy, okey
61        1         cho       
59        1         cheedy    
58        1         qotal     
57        3         odaiin, cthol, otey
56        1         qokchdy   
55        1         shckhy    
54        3         sal, ykeey, sor
53        1         keedy     
52        3         shody, kar, olaiin
51        1         sheor     
50        2         oly, qokeol
49        3         sheody, opchedy, lkaiin
48        1         chear     
47        4         sheo, qotol, otam, tol
46        3         chal, kain, checkhy
45        2         otchy, lchey
44        4         ykaiin, cthey, shdy, kedy
43        5         keey, lol, ody, tar, lor
42        6         cthor, otor, qoteey, tedy, lshedy, olkeedy
41        8         oteol, qodaiin, chaiin, taiin, ytaiin, aiiin, lkeedy, lkeey
40        1         olkeey    
39        3         chodaiin, choky, qokchedy
38        2         oraiin, oteody
37        3         kol, ckhy, olchedy
36        4         choty, okeody, ches, dshedy
35        5         sheky, qokor, chos, sheckhy, lkain
34        2         okchy, pchedy
33        5         okor, ykar, cheos, tchedy, olkain
32        7         shar, oiin, okchey, chees, chedaiin, otchedy, qopchedy
31        6         ckhey, shcthy, otchey, qokeody, olor, olkaiin
30        5         qokchey, cheal, chckhey, chedar, lkar
29        6         os, qo, qotor, opchey, olchey, aly
28        5         oteos, kchy, checthy, lkedy, daly
27        6         dchy, sair, okeeey, ykeedy, olkedy, yteedy
26        6         kor, ytar, okam, otchdy, qokeeey, rain
25        8         otchol, she, oaiin, qokam, yteey, orain, dchedy, okchedy
24        11        odar, dchor, pol, chety, yty, tchy, cheeky, oldy, chedal, ary, qotchedy
23        9         ycheey, qokeeo, tor, qotey, chl, aiir, kal, ched, qotchdy
22        13        tchey, ky, shodaiin, ckhol, qoaiin, sy, daiir, okeor, qor, keody, ldy, dary, okaly
21        10        kchey, om, ytedy, qokeor, okair, olky, kchedy, otair, rar, olshedy
20        13        shaiin, shear, keol, kchor, cham, dchol, rol, kchol, shecthy, teey, okchdy, chdar, qoeedy
19        15        cthar, tchor, ykchy, soiin, chockhy, qotchey, ols, ydaiin, sheal, ykedy, chedain, opchdy, otaly, tal, olkar
18        17        yky, okchor, ytchy, chky, chkaiin, qokchol, doiin, cthody, olol, dl, ytal, qockhy, odain, chdal, shed, qockhey, lshey
17        14        chocthy, ychor, kchdy, dchey, qody, daldy, okeeol, chain, sheos, ory, qokair, ror, ral, lky
16        10        dan, daiiin, otchor, oar, chokaiin, ty, chdaiin, tain, cheeo, lkchedy
15        17        ykal, sh, ykeody, chs, dshey, tchdy, ycheo, qopchdy, okody, qokeed, teol, qokaly, orol, aral, qoeey, okeeo, lchdy
14        22        kair, cphy, do, chom, ytor, cphol, sheeol, chokchy, ctho, ychey, choly, ram, qotchor, opchy, ycheol, cheeor, okeo, okees, shal, key...
13        27        chodar, yteody, qotchol, odal, qokechy, chkeey, okchol, choy, choiin, ockhy, ctheey, aldy, shes, keeol, chckhdy, laiin, shky, chkal, teedy, shee...
12        28        yshey, ytain, pchor, ychol, qoar, dcheey, cheeody, ry, tchol, shocthy, chkain, dshor, lr, oteor, okeos, chekal, ykeol, aram, arody, ytam...
11        38        shckhey, qotcho, pcheol, qokchor, qoteol, qodar, okary, cheodaiin, qopchy, chkar, otody, chcphy, okeal, rchedy, pchedar, olar, oral, keeey, fchedy, pchey...
10        43        shod, chokain, ro, ykol, chan, sam, qokshy, ytchey, chory, keor, qokcho, sheod, ytey, chty, ykor, ytchor, qopchey, ctheol, cheockhy, tey...
9         57        cthaiin, shos, chotey, otcho, ckhor, chr, ycheor, cthom, octhy, qokody, shokchy, sheeor, shees, okoiin, oees, chotchy, keeo, cheeey, sheaiin, ot...
8         55        sholdy, teody, dalor, shain, shoky, ochey, chotaiin, sos, tchody, dsheey, doiir, paiin, dsho, ksho, oeees, oko, okos, da, dshy, keeor...
7         82        cthal, tody, qoy, olsheey, qot, okom, cphaiin, qocthy, qoeeey, opy, ykey, shcthey, chodal, olchy, chod, okear, ykair, daram, olcheol, ykeor...
6         109       shory, cfhol, chodain, okaiir, an, ochor, otchody, qopol, cphor, daiidy, ees, ytaly, chocthey, choaiin, tcheey, kshey, schol, chary, cfhy, shoiin...
5         134       okan, cphey, kshy, ycho, pshol, yto, shok, chok, dchaiin, kcho, schey, okeom, opchol, qoteeol, kcheol, otcham, daiim, chopchy, chokeody, otan...
4         206       sory, chtaiin, cphar, oksho, shodain, rchy, shoaiin, ckho, kechy, cholaiin, shan, chyky, shty, qoteeey, shom, eeor, shkaiin, ksheo, kshody, qotcheo...
3         385       ckhar, cthes, sa, ydain, kodaiin, dchar, far, chokody, lchody, chotchey, ypchol, ychain, lshy, cholo, damo, ysheor, sols, qodair, qopchor, koaiin...
2         907       daraiin, cphoy, okchoy, kos, shoshy, shoy, oldain, kchom, cthols, cpho, okay, kokaiin, koshey, chtor, cfhar, chokeo, otoaiin, chodo, darshol, sshor...
1         6091      fachys, ataiin, cthres, are, syaiir, cthoary, ooiin, roloty, cth*ar, cfhaiin, ydaraishy, oydar, cfhoaiin, shodary, oschy, cphesaiin, cphodales, kshoy, otairin, sckhey...
```

## Acknowledgements

- [VMS transliteration by Takeshi Takahashi](http://www.voynich.com/pages/index.htm)