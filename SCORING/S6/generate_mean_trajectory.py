
def combine_means(design_name, N_means):
    with open("{}_mean_trajectory.dat".format(design_name) , "w") as f_out:
        for i in range(1, N_means+1):
            with open("{}_mean_{}.conf".format(design_name, i), "r") as f_in:
                lines = f_in.readlines()
                f_out.writelines(lines)
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and type(sys.argv[1]) is str and type(int(sys.argv[2])) == int:
        combine_means(sys.argv[1], int(sys.argv[2]))
    else:
        print("Arguments:")
        print("Design name (str)")
        print("Number of means to combine (int)")
