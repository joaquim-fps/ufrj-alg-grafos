def get_floor():
    limit = 10**18

    while True:
        floor = int(input())

        if floor < limit:
            return floor

def find_offset(floor):
    total_offset   = 0
    power_10       = 10
    decimal_places = 1
    forbidden_nums = {1:1}

    while power_10 < floor:
        power_10    = power_10 * 10
        nums_with_4 = (power_10 // 10) + (9 * forbidden_nums.get(decimal_places, 0))
        
        decimal_places                 = decimal_places + 1
        forbidden_nums[decimal_places] = nums_with_4

    for ch_digit in str(floor):
        digit = int(ch_digit)

        if digit < 4:
            total_offset = total_offset + (digit * forbidden_nums.get(decimal_places - 1, 0))
        else:
            total_offset = total_offset + ((power_10 // 10) + ((digit - 1) * forbidden_nums.get(decimal_places - 1, 0)))

        decimal_places = decimal_places - 1
        power_10       = power_10 // 10

    return total_offset

def offset_floor():
    floor = get_floor()
    return floor + find_offset(floor)
