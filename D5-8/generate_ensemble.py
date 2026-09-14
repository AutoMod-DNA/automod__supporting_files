
def generate_files(M, N, topology):
    for j in range(1, M+1):
        template = "input_{}.txt".format(j)
        with open(template, 'r') as f_src:
            fname_base = template.split(".")
            lines = f_src.readlines()
            for i in range(1, N+1):
                with open("{}__{}.txt".format(i, fname_base[0]), 'w') as f_out:
                    for line in lines:
                        if len(line.split("=")) == 2 and line.split("=")[0].find("topology") != -1:
                            key = line.split("=")[0]
                            val = topology
                            f_out.write("{} = {}\n".format(key, val))
                        elif len(line.split("=")) == 2 and line.split("=")[0].find("conf_file") != -1 and line.split("=")[0].find("lastconf_file") == -1:
                            key = line.split("=")[0]
                            if j == 1:
                                val = "start_1.conf"
                            else:
                                val = "{}__start_{}.conf".format(i, j)
                            f_out.write("{} = {}\n".format(key, val))
                        elif len(line.split("=")) == 2 and line.split("=")[0].find("seed") != -1:
                            key = line.split("=")[0]
                            val = i
                            f_out.write("{} = {}\n".format(key, val))
                        else:
                            f_out.write(line)
                    f_out.write("output_prefix = {}__\n".format(i))


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 4 and type(int(sys.argv[1])) is int and type(int(sys.argv[2])) is int and type(sys.argv[3]) is str:
        generate_files(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
    else:
        print("Arguments:")
        print("\t Number of input file templates (int). Naming must be 'input_i.txt' for each i.")
        print("\t Number of runs (int).")
        print("\t Name of the topology file.")
