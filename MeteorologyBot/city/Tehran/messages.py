import timme
from . import req


now = req.temps[timme.hour]
h00 = req.temps[0]
h01 = req.temps[1]
h02 = req.temps[2]
h03 = req.temps[3]
h04 = req.temps[4]
h05 = req.temps[5]
h06 = req.temps[6]
h07 = req.temps[7]
h08 = req.temps[8]
h09 = req.temps[9]
h10 = req.temps[10]
h11 = req.temps[11]
h12 = req.temps[12]
h13 = req.temps[13]
h14 = req.temps[14]
h15 = req.temps[15]
h16 = req.temps[16]
h17 = req.temps[17]
h18 = req.temps[18]
h19 = req.temps[19]
h20 = req.temps[20]
h21 = req.temps[21]
h22 = req.temps[23]
h23 = req.temps[23]
msg = f"""<b>وضعیت دما در شهر تهران:</b>
دما هم اکنون = <code>17.1</code> درجه سانتی‌گراد

<b>دما در ساعت های مختلف:</b>
۰۰:۰۰ = {h00}
۰۱:۰۰ = {h01}
۰۲:۰۰ = {h02}
۰۳:۰۰ = {h03}
۰۴:۰۰ = {h04}
۰۵:۰۰ = {h05}
۰۶:۰۰ = {h06}
۰۷:۰۰ = {h07}
۰۸:۰۰ = {h08}
۰۹:۰۰ = {h09}
۱۰:۰۰ = {h10}
۱۱:۰۰ = {h11}
۱۲:۰۰ = {h12}
۱۳:۰۰ = {h13}
۱۴:۰۰ = {h14}
۱۵:۰۰ = {h15}
۱۶:۰۰ = {h16}
۱۷:۰۰ = {h17}
۱۸:۰۰ = {h18}
۱۹:۰۰ = {h19}
۲۰:۰۰ = {h20}
۲۱:۰۰ = {h21}
۲۲:۰۰ = {h22}
۲۳:۰۰ = {h23}

⚠️<i>توجه: این آمار برای امروز می‌باشد!!</i>
"""
