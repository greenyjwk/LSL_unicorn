"""
Receiving a multi-channel time series from LSL
"""

from pylsl import StreamInlet, resolve_stream
from icecream import ic
# from Util import util


def main():
    # First resolve an eeg stream on the lab network
    ic("looking for a EEG Stream")

    # Discovering an available streams on the LSL network that matches a specific set of criteria.
    eeg_streams = resolve_stream('name', 'Unicorn')
    
    stream_names = []
    print("Stream Information: ")
    for stream in eeg_streams:
        stream_names.append(stream.name())
        print(stream.name())
        # print(util.obtain_stream_channel_names(stream))

    # Creating an inlet for the stream
    eeg_inlet = StreamInlet(eeg_streams[0])

    while True:
        # Getting a new sample with a time stamp
        sample, timestamp = eeg_inlet.pull_sample() # It doesn't put back the element, it removes the elements once it is called.
        ic(timestamp, sample)

if __name__ == '__main__':
    main()
