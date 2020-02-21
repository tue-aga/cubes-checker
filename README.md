This is a simple script that verifies that a certain construction is correct.

For more details and background, see:

> Tillmann Miltzow, Irene Parada, Willem Sonke, Bettina Speckmann, and Jules Wulms, *Hiding sliding cubes: Why reconfiguring modular robots is not easy*, 2020 (in preparation).


## How to run

The construction is given in `path.txt` as a list of (*x*, *y*, *z*)-coordinates of the occupied cubes. Run `python3 cubes-checker.py` to perform the verification. This will read `path.txt` and check (1) if it is a path, and (2) if its endpoint (0, 0, 2) is indeed on the inside.

The expected output is:

```
Test results:
(1) construction is a path
(2) endpoint is inside
```

The code is simple and should be easy to check for correctness.


## Acknowledgements

We thank Tim Ophelders for his help with implementing this script.
