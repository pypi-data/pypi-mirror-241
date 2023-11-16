Distributed_compy is a distributed computing library that offers multi-node (hybrid -- more than one machine)
and heterogeneous (CPU + mult-GPU), and multi-threading paradigms to leverage the processing power of a cluster.
Cython is used to generate glue code for the core C/C++ functions and provide wrappers to call from Python.
Requires numpy, CUDA toolkit>=2.0, OpenMP, and OpenMPI. Note: this library does not use the popular mpi4py library for
internode communication.

Features:
* Get/set/configure bandwidths of local node or entire cluster whether by supplied numpy array or from binary data files
* Code generator to write temporary binary data files or python files that are to be executed on each node
* Execute mpirun command from master node with default env var or configurable hostfile
* Reduction sum with functionality scaling such as python naive sum, multi-thread reduction sum,
  multi-gpu reduction sum, heterogeneous reduction sum, and hybrid heterogeneous reduction sum.

Additional features such as other reduction operations, dot product, matrix multiplication, image processing kernels, neural networks
and finite element method functions are being considered for future releases.