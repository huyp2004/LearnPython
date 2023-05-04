def menu_convert():
    # Menu
    try:
        menu_choose = int(input('''Menu chọn
        1. Thoát
        2. Đổi từ kg -> gam
        3. Đổi từ m -> mm
        >  '''))
    except ValueError:
        return 'Bạn nhập sai menu'

    # Create Dictionary Key value Menu. Syntax 'key': 'lambda function': 'function convert'
    menu_function = {
        1: lambda: exit(),
        2: lambda: run_convert('kg', 'g'),  # Function small to run Convert (Function big)
        3: lambda: run_convert('m', 'mm')
    }

    # Assign Number Menu to Dictionary and Create variable 'result' assign all
    try:
        result = menu_function[menu_choose]()  # Dictionary[key] and '()' run function
        return result
    except ValueError:
        return 'Menu không hợp lệ'


# From_unit: 'kg' or 'm', To_unit: 'g' or 'mm'
def run_convert(from_unit, to_unit):
    try:
        num_convert = float(input(f"Nhập số {from_unit} chuyển đổi: ") or 0)
        result_convert = num_convert * 1000  # Convert
        return f'{num_convert} {from_unit} bằng {result_convert}{to_unit}'
    except ValueError:
        return "Bạn nhập số không hợp lệ"


print(menu_convert())
