#Exception in Detail with different example

while True:
    try:
        number = int(input("What's your fav number ?\n"))
        print(number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")