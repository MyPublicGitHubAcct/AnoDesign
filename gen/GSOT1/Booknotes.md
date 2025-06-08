# Book notes

Note: Only update this in subl, from the real folder for Max.

From _Generating Sound & Organizing Time_ by Wakefield and Taylor.

Other sources:

- [gen documentation](https://docs.cycling74.com/userguide/gen/_gen_overview/)
- [gen operator descriptions](https://docs.cycling74.com/userguide/gen/gen~_operators/)
- [gen video tutorials](https://cycling74.com/tutorials/gen-video-tutorial-series)
- [pytest](https://emimartin.me/pytest_best_practices)

## Python environment

Note: _pysound_ is not available yet, so _sounddevice_ and _soundfile_ are used to read and write files. They are not available through homebrew, so a virtual environment should be installed in the user's home directory.


```python
sudo python3 -m venv venv/
source venv/bin/activate
sudo python3 -m pip install numpy scipy matplotlib soundfile sounddevice jupyterlab pytest
deactivate
```

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

```python
jupyter lab
```

