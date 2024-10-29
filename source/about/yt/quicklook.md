---
file_format: mystnb
kernelspec:
  display_name: Python 3
  name: python3
---
# yt


## quick look 

```{code-cell} ipython3
import yt 
ds = yt.load_sample("IsolatedGalaxy")
yt.SlicePlot(ds, 'x', ('gas', 'density'))
```

