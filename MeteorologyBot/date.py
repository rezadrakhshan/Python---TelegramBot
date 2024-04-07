from hijri_converter import convert
import jdatetime
from datetime import datetime

persian_month = {
    "1": "فروردین",
    "2": "اردیبهشت",
    "3": "خرداد",
    "4": "تیر",
    "5": "مرداد",
    "6": "شهریور",
    "7": "مهر",
    "8": "آبان",
    "9": "آذر",
    "10": "دی",
    "11": "بهمن",
    "12": "اسفند",
}

arabic_month = {
    "1": "محرم",
    "2": "صفر",
    "3": "ربیع الاول",
    "4": "ربیع الثانی",
    "5": "جمادی‌الاول",
    "6": "جمادی الثانی",
    "7": "رجب",
    "8": "شعبان",
    "9": "رمضان",
    "10": "شوال",
    "11": "ذیقعده",
    "12": "ذیحجه",
}

english_month = {
    "1": "ژانویه",
    "2": "فوریه",
    "3": "مارس",
    "4": "آوریل",
    "5": "می",
    "6": "ژوئن",
    "7": "ژوئیه",
    "8": "اوت",
    "9": "سپتامبر",
    "10": "اکتبر",
    "11": "نوامبر",
    "12": "دسامبر",
}
now = datetime.now()

hijri_date = convert.Gregorian(now.year, now.month, now.day).to_hijri()

s = jdatetime.datetime.now()



digits_map = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}



def convert_numbers_to_persian(text):
    return "".join([digits_map[char] if char in digits_map else char for char in text])



def mytime():
    for i in persian_month.keys():
        if str(s.month) == str(i):
            persian_date = f"{s.day} {persian_month[i]} {s.year}"
            persian = convert_numbers_to_persian(persian_date)
            break
    for j in arabic_month.keys():
        if str(hijri_date.month) == str(j):
            arabic_date = f"{hijri_date.day} {arabic_month[j]} {hijri_date.year}"
            arabic = convert_numbers_to_persian(arabic_date)
            break
    for e in english_month.keys():
        if str(now.month) == str(e):
            english_date = f"{now.day} {english_month[e]} {now.year}"
            english = convert_numbers_to_persian(english_date)
            break
    return f"""امروز {english}
{persian}
{arabic}"""
