import sys, os

def checkOS():
    _osProb = {
        "win" : 0,
        "*nix" : 0
    }
    try:
        sys.getwindowsversion()
        _osProb["win"] += 1
    except:
        _osProb["*nix"] += 1

    if (os.environ["PROCESSOR_ARCHITECTURE"] == "x86" or os.environ["PROCESSOR_ARCHITECTURE"] == "x64"):
        _osProb["win"] += 1
