EVALUATION OF DESIGN ACCURACY WITH MORE COMPLEX SHAPES

DESIGNS

Designs corresponding to four target shapes (D5-8) with varying square lattice cross sections were generated with AutoMod (v0.0.7) and MagicDNA (v2.0.2 used with MATLAB R2024b).

For reproducing AutoMod designs, the internal state of the program prior to design export can be recovered for each design using the appropriate JSON file, which contains the states of the objects the program uses to represent the target shape, and the state of the random random generator. A python script "check_design_equality.py" is provided for fast command line checking of design equality using the TXT files that contain a brief description of the generated crossover pattern and are outputted by AutoMod in conjuction with every design output.

Random seed 0 and default settings were used for all AutoMod designs.

For reproducing MagicDNA designs, the text files containing node coordinates are provided.

In MagicDNA the extrude method was used for all designs, since it outperformed the sweep method in the accuracy comparison between these two methods (Supplementary Figure 3). Target shapes were inputted via the spline sketch function, reading in the text files containing node points. Bundle lengths were matched to the target shape, and default edge gradients were used. Bundles were connected from their ends utilizing all connections points, i.e., all helices continue from bundle to bundle. No spacer nucleotides were used since they resulted in decreased accuracy in the preliminary accuracy comparison (Supplementary Figure 3).

The default setting of minimum distances between crossovers being 8 nucleotides was used. Zigzag uncut staples were generated, i.e., long staples with crossovers. Only double crossovers were used in all AutoMod and MagicDNA designs.

Each design was completed with a minimal scaffold routing, i.e., no internal scaffold crossovers, and without introducing staple nicks. This is done to keep the focus of the accuracy comparison on the features most crucial for inducing curvature; namely, length differences between helices and the staple crossover pattern.

Start configuration for oxDNA simulations is a straight bundle for AutoMod designs. With MagicDNA designs the CaDNAno file was imported to oxView, and preliminary relaxation for the bundle connections was done with the rigid-body simulator.

The same scaffold routing was used for all comparable designs. Scaffold routing was imposed with CaDNAno v2.4.13.

D5:	planar figure 8
D6:	spiral with constant rise and radius of curvature
D7:	spiral with constant rise and varying curvature
D8:	planar spiral

SIMULATIONS

Long oxDNA protocol was used. Notebooks for generating start conformations are in subdirectories.

Initial gradient descent was performed on CPU (13th Gen Intel Core i5-13400 × 16) on a Linux workstation (Linux 6.17.0-1032-oem, 64-bit, Ubuntu 24.04.4 LTS). OxDNA version v3.7.0 was compiled with GCC 11.2.0. and CMake 3.28.3. Random seed 0 was used for all initial minimizations, even though a deterministic steepest descent was used.

An ensemble of N=10 simulation repeats was performed for each structure. Random seeds 1-10 were used, respectively.

MD simulations were performed on GPUs (NVIDIA H200, H100, A100, V100) using oxDNA version v3.7.0 compiled with GCC 13.3.0, CMake 3.30.5 and CUDA 12.6.2.

Mean conformations were computed with oxDNA analysis tools v2.6.5, using Python 3.12.9.

The Aalto University high-performance computing cluster, Triton, was used to run the MD simulations in parallel.



