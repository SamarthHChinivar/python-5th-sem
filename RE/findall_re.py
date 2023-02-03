import re

string = '''[<a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/greengini-kolkata/?pos=1&amp;kwd=vermicompost&amp;tags=A||||9120.144|Price|proxy|" target="_blank"><span>Green Gini</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.rachanaagrotech.co.in/?pos=2&amp;kwd=vermicompost&amp;tags=A||||7613.566|Price|proxy|" target="_blank"><span>Rachana Guild Private Limited</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.amplefarmtech.com/?pos=3&amp;kwd=vermicompost&amp;tags=A||||7423.2134|Price|proxy|" target="_blank"><span>Ample Farm Tech</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/sgsorganic/?pos=4&amp;kwd=vermicompost&amp;tags=A||||8256.911|Price|proxy|" target="_blank"><span>SGS Organics LLP</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/nexfarm-products-india-limited/?pos=5&amp;kwd=vermicompost&amp;tags=A||||8038.904||bl|" target="_blank"><span>Nexfarm Products India Private Limited</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/progressworks/?pos=6&amp;kwd=vermicompost&amp;tags=A||||8276.28|Price|proxy|" target="_blank"><span>Progress Works (OPC) Private Limited</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.laxmiorganics.com/?pos=7&amp;kwd=vermicompost&amp;tags=A||||8042.3813|Price|proxy|" target="_blank"><span>Laxmi Organics</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/panchamiorganics/?pos=8&amp;kwd=vermicompost&amp;tags=A||||7867.1333|Price|proxy|" target="_blank"><span>Panchami Organics</span></a>, <a class="clr3 fs12 
fwn rsrc" href="https://www.indiamart.com/elitechemicals/?pos=9&amp;kwd=vermicompost&amp;tags=A||||8243.7295|Price|proxy|" target="_blank"><span>Elite Chemicals</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/ashokasalesjalandhar/?pos=10&amp;kwd=vermicompost&amp;tags=A||||8181.124|Price|proxy|" target="_blank"><span>Ashoka Sales</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/saidharma/?pos=11&amp;kwd=vermicompost&amp;tags=A||||7867.1333|Price|proxy|" target="_blank"><span>Sai Dharma</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.greenriseagro.com/?pos=12&amp;kwd=vermicompost&amp;tags=A||||7614.3447|Price|proxy|" target="_blank"><span>Green Rise Agro Industries</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/hariom-vermicompost/?pos=13&amp;kwd=vermicompost&amp;tags=A||||8327.788|Price|proxy|" target="_blank"><span>Hari Om Vermicompost</span></a>, <a class="clr3 fs12 fwn rsrc" href="https://www.indiamart.com/jaishree-organics-jaipur/?pos=14&amp;kwd=vermicompost&amp;tags=A||||8042.3813|Price|proxy|" target="_blank"><span>Jai Shree Organics</span></a>]'''

x = re.findall('a',string)
y = re.findall('.span',string)

if(x != []):
    print(x)
else:
    print('not found')

if(y != []):
    print('Wildcard search: ',y)
else:
    print('not found')