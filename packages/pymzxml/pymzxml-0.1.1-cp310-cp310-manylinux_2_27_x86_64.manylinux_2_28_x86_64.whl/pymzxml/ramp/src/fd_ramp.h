#ifndef _FDRAMP_H
#define _FDRAMP_H

#include "ramp.h"

extern "C" {
  ramp_fileoffset_t getIndexOffsetFd(int fd);
  ramp_fileoffset_t *readIndexFd(int fd,
				 ramp_fileoffset_t indexOffset,
				 int *iLastScan);
  void readHeaderFd(int fd,
		    ramp_fileoffset_t lScanIndex,
		    struct ScanHeaderStruct *scanHeader);
  int  readMsLevelFd(int fd,
		     ramp_fileoffset_t lScanIndex);
  double readStartMzFd(int fd,
		       ramp_fileoffset_t lScanIndex);
  double readEndMzFd(int fd,
		     ramp_fileoffset_t lScanIndex);
  int readPeaksCountFd(int fd,
		       ramp_fileoffset_t lScanIndex);
  RAMPREAL *readPeaksFd(int fd,
		      ramp_fileoffset_t lScanIndex);
  void readRunHeaderFd(int fd,
		       ramp_fileoffset_t *pScanIndex,
		       struct RunHeaderStruct *runHeader,
		       int iLastScan);
  void readMSRunFd(int fd,
		   struct RunHeaderStruct *runHeader);
  InstrumentStruct* getInstrumentStructFd(int fd);
  int getLastScanFd(int fd);
  void freeInstrumentStruct(struct InstrumentStruct *instrumentStruct);
}

#endif
