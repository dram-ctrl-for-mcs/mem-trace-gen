# mem-trace-gen
Memory trace generator



# included libraries

Mälardalen WCET benchmark http://www.mrtc.mdh.se/projects/wcet/benchmarks.html

MiBench benchmark http://wwweb.eecs.umich.edu/mibench/



# tools required
gem5 architectural simulator http://www.gem5.org/

hg clone http://repo.gem5.org/gem5-stable

cd gem5-stable

scons build/ARM/gem5.opt

install gcc-arm-linux-gnueabi to run arm-linux-gnueabi-gcc



# for OS X users
port select --list gcc

sudo port select --set gcc mp-gcc48


# Building benchmakrs
wcet - 

cd wcet_bench

make -i
