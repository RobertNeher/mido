import mido
from mido import MidiFile

mid = MidiFile('The-Avengers.mid')
outport = mido.open_output()

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        outport.send(msg)