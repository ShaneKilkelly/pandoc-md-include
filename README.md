# md-include, for pandoc

```
pandoc -t json main.md | ./raw-filter.py  | pandoc -f json -t latex -s
```
