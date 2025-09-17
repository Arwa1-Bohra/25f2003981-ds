def division():
    try:
        a = int(input("Enter the numerator:"))
        b = int(input("Enter the denominator:"))
        res = a//b
        print(res)
    except Exception as e:
        print(f"Error: {str(e)}")