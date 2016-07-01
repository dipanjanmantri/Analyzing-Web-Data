import xml.etree.ElementTree as ET


data='''
<commentinfo>
<note>
This file contains the actual data for your assignment - good luck!
</note>
<comments>
<comment>
<name>Carlo</name>
<count>99</count>
</comment>
<comment>
<name>Ana</name>
<count>96</count>
</comment>
<comment>
<name>Dyllon</name>
<count>94</count>
</comment>
<comment>
<name>Neil</name>
<count>93</count>
</comment>
<comment>
<name>Susie</name>
<count>93</count>
</comment>
<comment>
<name>Collette</name>
<count>90</count>
</comment>
<comment>
<name>Saffron</name>
<count>87</count>
</comment>
<comment>
<name>Jazz</name>
<count>87</count>
</comment>
<comment>
<name>Caelinn</name>
<count>86</count>
</comment>
<comment>
<name>Oona</name>
<count>84</count>
</comment>
<comment>
<name>Taddy</name>
<count>83</count>
</comment>
<comment>
<name>Naomi</name>
<count>82</count>
</comment>
<comment>
<name>Marcy</name>
<count>78</count>
</comment>
<comment>
<name>Jayden</name>
<count>77</count>
</comment>
<comment>
<name>Murdina</name>
<count>73</count>
</comment>
<comment>
<name>Melice</name>
<count>69</count>
</comment>
<comment>
<name>Nyla</name>
<count>68</count>
</comment>
<comment>
<name>Luka</name>
<count>68</count>
</comment>
<comment>
<name>Carl</name>
<count>64</count>
</comment>
<comment>
<name>Rhyse</name>
<count>62</count>
</comment>
<comment>
<name>Muhammad</name>
<count>62</count>
</comment>
<comment>
<name>Sonniva</name>
<count>61</count>
</comment>
<comment>
<name>Darl</name>
<count>61</count>
</comment>
<comment>
<name>Aayat</name>
<count>59</count>
</comment>
<comment>
<name>Syed</name>
<count>58</count>
</comment>
<comment>
<name>Triniti</name>
<count>56</count>
</comment>
<comment>
<name>Karyn</name>
<count>54</count>
</comment>
<comment>
<name>Jonatan</name>
<count>53</count>
</comment>
<comment>
<name>Ceridwen</name>
<count>46</count>
</comment>
<comment>
<name>Aman</name>
<count>46</count>
</comment>
<comment>
<name>Kaleena</name>
<count>45</count>
</comment>
<comment>
<name>Miku</name>
<count>44</count>
</comment>
<comment>
<name>Anmol</name>
<count>44</count>
</comment>
<comment>
<name>Binod</name>
<count>41</count>
</comment>
<comment>
<name>Maximus</name>
<count>38</count>
</comment>
<comment>
<name>Aurea</name>
<count>37</count>
</comment>
<comment>
<name>Mhurain</name>
<count>36</count>
</comment>
<comment>
<name>Edison</name>
<count>31</count>
</comment>
<comment>
<name>Marc</name>
<count>30</count>
</comment>
<comment>
<name>Pele</name>
<count>28</count>
</comment>
<comment>
<name>Bully</name>
<count>26</count>
</comment>
<comment>
<name>Sera</name>
<count>26</count>
</comment>
<comment>
<name>Adil</name>
<count>26</count>
</comment>
<comment>
<name>Martina</name>
<count>25</count>
</comment>
<comment>
<name>Hadasah</name>
<count>19</count>
</comment>
<comment>
<name>Alyssa</name>
<count>13</count>
</comment>
<comment>
<name>Morris</name>
<count>11</count>
</comment>
<comment>
<name>Dearbhla</name>
<count>10</count>
</comment>
<comment>
<name>Isadora</name>
<count>9</count>
</comment>
<comment>
<name>Chala</name>
<count>5</count>
</comment>
</comments>
</commentinfo>
'''
input=ET.fromstring(data)
lst=input.findall('commentinfo/comments/')


s=0

for item in lst:
    x=item.find('count').text
    y=int(x)
    print (y)


