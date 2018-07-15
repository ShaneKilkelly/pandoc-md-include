# md-include, for pandoc

A pandoc filter which adds an `include` directive, to include the __parsed__
contents of another file.



## Example

main.md:
```markdown
# Test

This is a test:

<!-- %include("./list.md") -->

And this bit comes after.
```

list.md:
```markdown
- one
- two
- three
```

And then run:
```
pandoc main.md --filter ./pandoc-md-include.py -t html -s
```


Result (with `head` removed for clarity):
```html
<html>
<body>
  <h1 id="test">Test</h1>
  <p>This is a test:</p>
  <ul>
    <li>one</li>
    <li>two</li>
    <li>three</li>
  </ul>
  <p>And this bit comes after.</p>
</body>
</html>

```
