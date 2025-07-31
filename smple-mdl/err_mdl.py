def chkNum(a):
    if int(a) < 100:
        raise NameError("Number should be 100 or more.")
    else:
        print("Number is greater than 100.")