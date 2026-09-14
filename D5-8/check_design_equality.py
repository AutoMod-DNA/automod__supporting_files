def check_equality(fname1, fname2):
    with open(fname1, 'r') as f1:
        with open(fname2, 'r') as f2:
            line1 = f1.readline()
            line2 = f2.readline()
            while line1 == line2 and line1 and line2:
                line1 = f1.readline()
                line2 = f2.readline()
            if not line1 and not line2:
                print("Designs are the same!")
            else:
                print("Designs are different!")
                print(line1)
                print(line2)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        check_equality(sys.argv[1], sys.argv[2])
    else:
        print("Give two files as arguments.")
