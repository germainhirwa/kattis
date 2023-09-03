d = [
    ['Logn', 0.3],
    ['Andvari', 1.6],
    ['Kul', 3.4],
    ['Gola', 5.5],
    ['Stinningsgola', 8.0],
    ['Kaldi', 10.8],
    ['Stinningskaldi', 13.9],
    ['Allhvass vindur', 17.2],
    ['Hvassvidri', 20.8],
    ['Stormur', 24.5],
    ['Rok', 28.5],
    ['Ofsavedur', 32.7],
    ['Farvidri', 201]
]
s = float(input())
for n, l in d:
    if s < l: print(n); break