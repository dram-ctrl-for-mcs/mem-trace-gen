#! /usr/bin/env python

import os
import ntpath

ROOT = '../../'
GEM5 = ROOT + 'gem5-stable/build/ARM/gem5.opt'
BENCH_DIR = ROOT + 'benchmarks/wcet_bench/'
GEM5_OPTS = '--outdir=' + ROOT + 'traces/wcet_bench/'
#DEBUG_FLAGS = '--debug-flags=Bus,MemoryAccess --debug-file='
DEBUG_FLAGS = '--debug-flags=MemoryAccess --debug-file='
PY_SCRIPT = ROOT + 'gem5-stable/configs/example/se.py'
PY_OPTS = '--caches --l1d_size=4kB --l1i_size=4kB -m'
TRACE_DIR = ROOT + 'traces/wcet_bench/'

maxCycles = 1 * 1000 * 1000
bm_list = []
# automotive

obj_files = [ f for f in os.listdir(BENCH_DIR) if os.path.isfile(os.path.join(BENCH_DIR,f)) and f.endswith('.o') ]

os.system('mkdir -p ' + TRACE_DIR)

for obj_file in obj_files:
  obj = obj_file[:-2]
  command = GEM5
  command += ' ' + GEM5_OPTS
  command += obj + '.out'
  command += ' ' + DEBUG_FLAGS
  command += 'cerr'
  command += ' ' + PY_SCRIPT
  command += ' ' + PY_OPTS
  command += ' ' + str(maxCycles * 500)
  command += ' -c ' + BENCH_DIR + obj_file
  command += ' &> ' + TRACE_DIR + obj + '.mem'
  print '\n##### Trace Generation of ' + obj + ' #####'
  os.system(command)

