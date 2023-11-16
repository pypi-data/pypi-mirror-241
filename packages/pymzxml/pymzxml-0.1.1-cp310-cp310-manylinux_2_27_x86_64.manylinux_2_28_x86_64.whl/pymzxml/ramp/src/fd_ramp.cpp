#include "fd_ramp.h"


ramp_fileoffset_t getIndexOffsetFd(int fd)
{
  ramp_fileoffset_t indexOffset;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  indexOffset = getIndexOffset(result);
  free(result);

  return indexOffset;
}


ramp_fileoffset_t *readIndexFd(int fd,
			       ramp_fileoffset_t indexOffset,
			       int *iLastScan)
{
  ramp_fileoffset_t *pScanIndex;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  pScanIndex = readIndex(result,
			 indexOffset,
			 iLastScan);
  free(result);

  return pScanIndex;
}


void readHeaderFd(int fd,
		  ramp_fileoffset_t lScanIndex,
		  struct ScanHeaderStruct *scanHeader)
{
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  readHeader(result,
	     lScanIndex,
	     scanHeader);
  free(result);
}


int  readMsLevelFd(int fd,
		   ramp_fileoffset_t lScanIndex)
{
  int msLevel;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  msLevel = readMsLevel(result,
			lScanIndex);
  free(result);

  return msLevel;
}


double readStartMzFd(int fd,
		     ramp_fileoffset_t lScanIndex)
{
  double startMz;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  startMz = readStartMz(result,
			lScanIndex);
  free(result);

  return startMz;
}


double readEndMzFd(int fd,
		   ramp_fileoffset_t lScanIndex)
{
  double endMz;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  endMz = readEndMz(result,
			lScanIndex);
  free(result);

  return endMz;
}


int readPeaksCountFd(int fd,
		     ramp_fileoffset_t lScanIndex)
{
  int peaksCount;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  peaksCount = readPeaksCount(result,
			      lScanIndex);
  free(result);

  return peaksCount;
}


RAMPREAL *readPeaksFd(int fd,
		      ramp_fileoffset_t lScanIndex)
{
  RAMPREAL *pPeaks;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  pPeaks = readPeaks(result,
		     lScanIndex);
  free(result);

  return pPeaks;
}


void readRunHeaderFd(int fd,
		     ramp_fileoffset_t *pScanIndex,
		     struct RunHeaderStruct *runHeader,
		     int iLastScan)
{
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  readRunHeader(result,
		pScanIndex,
		runHeader,
		iLastScan);
  free(result);
}


void readMSRunFd(int fd,
		 struct RunHeaderStruct *runHeader)
{
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  readMSRun(result,
	    runHeader);

  free(result);
}


int getLastScanFd(int fd)
{
  int lastScan;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  lastScan = getLastScan(result);
  free(result);

  return lastScan;
}


InstrumentStruct* getInstrumentStructFd(int fd)
{
  InstrumentStruct* output;
  RAMPFILE *result = (RAMPFILE *)calloc(1,sizeof(RAMPFILE));

  result->fileHandle = fdopen(fd, "r");
  output = getInstrumentStruct(result);
  free(result);
  return output;
}


void freeInstrumentStruct(struct InstrumentStruct *instrumentStruct)
{
  free(instrumentStruct);
}
