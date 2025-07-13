# Book notes

Note: Only update this in subl, from the real folder for Max.

From _Generating Sound & Organizing Time_ by Wakefield and Taylor.

Other sources:

- [gen documentation](https://docs.cycling74.com/userguide/gen/_gen_overview/)
- [gen for beginners](https://cycling74.com/tutorials/gen~-for-beginners-part-1-a-place-to-start)
- [gen operator descriptions](https://docs.cycling74.com/userguide/gen/gen~_operators/)
- [gen video tutorials](https://cycling74.com/tutorials/gen-video-tutorial-series)
- [pytest](https://emimartin.me/pytest_best_practices)


## Useful Ideas and Formulas


Rhythym are patterns of events, with space between the 'beats'. The book considers each beat as being a point in time defined by the length of ramps between them. For example, straight eighth notes are surrounded by ramps of the same size, but a 'clave son' (below) will use different sizes between pulses.

1 + 2 + 3 + 4 + 1 + 2 + 3 + 4 + 
x     x     x       x   x

Cyclic ramp functions provide a precise way to represent the passage of time. The term _phase_ describes the current location of on the timeline, mostly between beats. The slope of the ramp determines the _tempo_.

_Phase increment_ = Frequency in Hertz / Sample Rate
_BPM to Frequency_ = BPM / 60

Using a phasor to move around sample playback (_bpm-sample-loop.gendsp_) and a beat slicer (_bpm-sample-beat-slicer.gendsp_) are in __g4b-001.maxpat__.


### A phasor as a clock source

__g4b-005-Clock-Source.maxpat__ includes a clock source made with a simple ramp whose speed is defined as (integer) BPM / 60.

_Ramp multiplication_ can be used to derive multiple, related clocks (subdivisions such as measures, beats, polyrhythms, ratchets, etc.) from a common source. Multiplying by a number smaller than one will restrict time vertically (increasing the rate, or slope of the ramp), whereas multiplying by a number larger than one will stretch time.

One negative of this method is that the subdivisions will reset once the clock source goes back to zero.

__Note__: _Ratcheting_ is splitting a single pulse into more than on equal parts.  This is often used with probability to create an effect often heard in, for example, Tangerine Dream's early work. Examples [here](https://youtu.be/ntjE9EguxO0?si=43a3nFV3nDiGi3ms).


### Ramps to Steps

If a ramp is run through a _floor_ operator, it will split the ramp into a step function (0 or 1).


### Phase Rotation

Delaying the phase of a ramp can be accomplished by subtracting an amount (presumably 0 to 1) from the ramp and wrapping the result to be between 0 and 1. As phase is a circular concept, the result can be viewed as, for example, 25% delayed or 75% ahead. 


# ---------------------- STOPPED AT PAGE 41 ----------------------


## Python environment

Note: _pysound_ is not available yet, so _sounddevice_ and _soundfile_ are used to read and write files. They are not available through homebrew, so a virtual environment should be installed in the user's home directory.


### Using UV

```python
uv add numpy scipy matplotlib soundfile sounddevice jupyterlab pytest
```


### Using Stock Python

```python
sudo python3 -m venv venv/
source venv/bin/activate
sudo python3 -m pip install numpy scipy matplotlib soundfile sounddevice jupyterlab pytest
deactivate
```


## Jupyter Lab

Notebooks can be run directly in PyCharm or VS Code. If it needs to be run in a browser, the following may help.

To ensure that Jupyter Lab works, you need to install the LTS version of Node.js, which can be done [here](https://nodejs.org/en/download/package-manager).  The commands to run will be similar to this:


```bash
# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
# download and install Node.js (you may need to restart the terminal)
nvm install 22
# verifies the right Node.js version is in the environment
node -v # should print `v22.11.0`
# verifies the right npm version is in the environment
npm -v # should print `10.9.0`
```


To load Jupyter lab:


```zsh
uv run --with jupyter jupyter lab

```



```python
jupyter lab
```

