#!/usr/bin/python
import sys
from os import path
from DTMFdetector import DTMFdetector

# Python-based wave audio file based DTMF detector
# Using public domain DTMF library code from
# http://johnetherton.com/projects/pys60-dtmf-detector

# This project code is multi OSS licensed. Select the one that best suites you
# GPL, LGPL, GPL v3, LGPL v3
# See project website for details
# http://sourceforge.net/projects/fbdtmfdetector/

# History:
#   10/24/2010 - David Luu, v1.0, initial release

def usage():
  print ""
  print "DetectDtmfFromFile, v1.0 10/24/2010"
  print "Wave audio file based DTMF detector"
  print "Outputs DTMF digits detected from wave audio file"
  print ""
  print "Usage:"
  print ""
  print "DetectDtmfFromFile -i pathToWavFile [-f frequency] [-d] [-h] [-?]"
  print "                      [-ss sample size] [-ch channels] [-e encoding]"
  print ""
  print "Notes:"
  print "       parameters in brackets are optional"
  print ""
  print "       filepath to wave audio file may be relative or absolute"
  print ""
  print "       Default supported & tested audio file formats are"
  print "       16-bit, mono, 8kHz, PCM encoding (default format)"
  print "       16-bit, mono, 16kHz, PCM encoding (doesn't work well)"
  print ""
  print "       For other sample sizes, frequencies, and encoding formats,"
  print "       you will have to modify the source code to support them."
  print ""
  print "       For now, the code/tool will ignore unsupported sample sizes,"
  print "       frequencies, encodings, etc. when you supply them as inputs."
  print ""
  print "       NOTE: If you try and supply a wave audio file w/ unsupported"
  print "       audio file format, code/tool will likely return an error or"
  print "       unreliable results."
  print ""
  print "       Best suggestion for using audio files in other formats is to"
  print "       use converter to get them into supported format for DTMF"
  print "       detection. For command line/automation processing, suggest"
  print "       Sox - http://sox.sourceforge.net"
  print ""
  print "       frequency = 8000, 16000, 11025, 22050, 44100, etc."
  print "       sample size, in bits = 8, 16"
  print "       channels = 1 for mono, 2 for stereo"
  print "       encoding = PCM, ADPCM, mu-Law, a-Law, etc."
  print ""
  print "       -d = enable debug mode:"
  print "            outputs additional info for DTMF detection analysis"
  print "       -h or -? = print this help contents"
  print ""

##check cmd line params
#argv[0] = script name
if len(sys.argv) < 2:
  usage()
  sys.exit(2)

##initialize params & define defaults
wavfile = ""
debugFlag = False
#default, supported/tested audio format of 16-bits, mono, 8kHz
freq = 8000

#unused/unsupported parameters for now...
samplesize = 16
channels = 1
encoding = "PCM"

##parse cmd line params
for i in range(len(sys.argv)):
  if sys.argv[i] == '-h':
    usage()                     
    sys.exit()                  
  elif sys.argv[i] == '-?':
    usage()                     
    sys.exit()
  elif sys.argv[i] == '-i':
    wavfile = sys.argv[i+1]
  elif sys.argv[i] == '-f':
    freq = sys.argv[i+1]
  elif sys.argv[i] == '-d':
    debugFlag = True
  elif sys.argv[i] == '-ss':
    samplesize = sys.argv[i+1]
  elif sys.argv[i] == '-ch':
    channels = sys.argv[i+1]
  elif sys.argv[i] == '-e':
    encoding = sys.argv[i+1]

if not path.exists(wavfile):
  print ""
  print "Wave audio file does not exist. Please verify file."
  print "Run \"DetectDtmfFromFile -h\" for usage info."
  print ""
  sys.exit(2)

#dtmf = DTMFdetector() #original call for default audio format
dtmf = DTMFdetector(freq,debugFlag)
data = dtmf.getDTMFfromWAV(wavfile)
print data