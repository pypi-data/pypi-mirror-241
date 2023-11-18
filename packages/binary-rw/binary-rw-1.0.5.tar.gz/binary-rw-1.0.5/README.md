# binary-rw

Simple library for reading binary files. 
I wrote this library to help myself with working with binary files written with c#.

## Examples
Write text to file.
```python
>>> import binary_rw
>>> file = binary_rw.BinaryWriter("test")
>>> file.write_string("Example text")
>>> file.close()
```

Read byte from file.
```python
>>> import binary_rw
>>> file = binary_rw.BinaryReader("test")
>>> file.read_byte()
>>> file.close()
```

Use BinaryReader with with
```python
import binary_rw
with BinaryReader("test") as file:
    #code
```

## Installation
```
pip install binary-rw
```

## License
[MIT](LICENSE) © Filip K.
