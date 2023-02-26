def get_phone(país, area , primeiro, segundo):
    return f"{país}-{area}-{primeiro}-{segundo}"
phone_num = get_phone(país=55, area=31, primeiro=99999, segundo=9999)
print(phone_num)