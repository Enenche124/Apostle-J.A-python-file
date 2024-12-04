user_input = int(input("Enter five-digit integer: "))

extract_first = user_input % 10


extract_second = extract_first  % 10


extract_third =  extract_second % 10



extract_fourth = extract_third % 10

extract_fifth = extract_fourth % 10



print(extract_first, extract_second, extract_third,extract_fourth, extract_fifth)
pass



