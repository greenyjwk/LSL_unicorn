"""
Sending multi-channel time series to LSL
"""

import sys
import time
from random import random as rand
from pylsl import StreamInfo, StreamOutlet, local_clock

def main(argv):
    srate = 280 #standard rate
    name = 'Unicorn'
    type = 'EEG'
    n_channels = 8

    # Create the stream Info
    # It defines the what kind of strems would be used in the LSL
    info = StreamInfo(name, type, n_channels, srate, 'float32', 'myuid1234')
 
    
    # Make a data outlet, it sends the data from python application to LSL
    outlet = StreamOutlet(info)

    # Begin the stream
    print("Sending data to LSL")
    start_time = local_clock()
    sent_samples = 0

    while True:
        elapsed_time = local_clock() - start_time
        required_samples = int(srate * elapsed_time) - sent_samples 
        for sample_ix in range(required_samples):
            #pylsl.vectorf
            mysample = [rand() for _ in range(n_channels)] # An array that has 8 random numbers.
            outlet.push_sample(mysample)    # Pushing random data into stream, the data from 
        sent_samples += required_samples
        #Send it and wait centisecond
        time.sleep(0.1)

if __name__ == '__main__':    
    main(sys.argv[1:])