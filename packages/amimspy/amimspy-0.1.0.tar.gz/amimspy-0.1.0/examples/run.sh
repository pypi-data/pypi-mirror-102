#!/usr/bin/env bash

#Process scans
amimspy process-scans --input ../tests/data/testData1.mzML ../tests/data/testData2.mzML \
--metascans ../tests/data/testData1.txt ../tests/data/testData2.txt --output ../tests/results/peaklists \
--failed-wells ../tests/results/failed_wells.txt --processed_scans ../tests/results/processed_scans.txt \
--snr-threshold 3 --min-scans 2 --min-fraction 0.5 --ppm 20 --metalist ../tests/data/SampleMetadata.txt 

# hdf5 peaklist to txt
amimspy hdf5-pls-to-txt --input ../tests/results/peaklists.hdf5 --output ../tests/results

#Prcoess samples
amimspy process-samples --input ../tests/results/peaklists.hdf5 --output ../tests/results/peakmatrix.hdf5 \
--ppm 20 --min-fraction 0.5

# hdf5 peak matrix to txt
amimspy hdf5-pm-to-txt --input ../tests/results/peakmatrix.hdf5 --output ../tests/results/peakmatrix.txt \
--attribute_name intensity --representation-samples columns --comprehensive
