def MenuShowControl():
    try:
        choose_menu = int(input('''Mời bạn chọn
        1. Thoát
        2. Đổi từ kg -> gam
        3. Đổi từ m -> mm
        >  '''))
    except ValueError:
        return 'Bạn nhập sai menu'

    # Create Dictionary Key value Menu. Syntax 'key': 'lambda function': 'function convert'
    dict_function_menu = {
        1: lambda: exit(),
        2: lambda: convertMenu('kg', 'g'),  # Function small to run Convert (Function big)
        3: lambda: convertMenu('m', 'mm')
    }

    try:
        result_menu = dict_function_menu[choose_menu]()  # Dictionary[key] and '()' run function
        return result_menu
    except ValueError:
        return 'Menu không hợp lệ'


def convertMenu(from_unit, to_unit):
    try:
        number_input = float(input(f"Nhập số {from_unit} chuyển đổi: ") or 0)
        result_number_convert = number_input * 1000  # Convert
        return f'{number_input} {from_unit} bằng {result_number_convert}{to_unit}'
    except ValueError:
        return "Bạn nhập số không hợp lệ"


print(MenuShowControl())
