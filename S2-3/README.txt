CALIBRATION OF DEFAULT PARAMETERS

DESIGNS

AutoMod was used to generate split ring (R=20nm) designs in square and honeycomb lattices. The target crossover density was kept constant while sweeping over a series of effective length change values.

Program internal state files for AutoMod are provided for full reproducibility. Random seed 0 was used for the generation of all designs.

The same scaffold routing was used for all comparable designs. Scaffold routing was imposed with CaDNAno v2.4.13.

SIMULATIONS

Short oxDNA protocol was used.

Initial gradient descent was performed on CPU (13th Gen Intel Core i5-13400 × 16) on a Linux workstation (Linux 6.17.0-1032-oem, 64-bit, Ubuntu 24.04.4 LTS). OxDNA version v3.7.0 was compiled with GCC 11.2.0. and CMake 3.28.3. Random seed 0 was used for all initial minimizations, even though a deterministic steepest descent was used.

An ensemble of N=5 simulation repeats was performed for each structure. Random seeds 1-5 were used, respectively.

MD simulations were performed on GPUs (NVIDIA H200, H100, A100, V100) using oxDNA version v3.7.0 compiled with GCC 13.3.0, CMake 3.30.5 and CUDA 12.6.2.

Mean conformations were computed with oxDNA analysis tools v2.6.5, using Python 3.12.9.

The Aalto University high-performance computing cluster, Triton, was used to run the MD simulations in parallel.
