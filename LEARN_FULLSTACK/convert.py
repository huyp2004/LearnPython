def menu_convert():
    try:
        menu_choose = int(input('''Menu chọn
        1. Thoát
        2. Đổi từ kg -> gam
        3. Đổi từ m -> mm
        >  '''))
    except ValueError:
        return 'Bạn nhập sai menu'

    if menu_choose == 1:
        return "Chương trình đã thoát"

    elif menu_choose == 2:
        try:
            kg = float(input("Mời bạn nhập số kg: ") or 0)
            gam = convert_to_gam(kg)
            return f'{kg}kg bằng {gam} gam'
        except ValueError:
            return "Bạn nhập số kg không hợp lệ"

    elif menu_choose == 3:
        try:
            m = int(input("Mời bạn nhập số mét: ") or 0)
            mm = convert_to_mm(m)
            return f'{m}m bằng {mm}mm'
        except ValueError:
            return "Bạn nhập số mét không hợp lệ"

    else:
        return "Không có chức năng này trong danh sách"


def convert_to_gam(kg):
    gam = kg * 1000
    return gam


def convert_to_mm(m):
    mm = m * 1000
    return mm


print(menu_convert())
