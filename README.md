# pyflvmeta

A naive Python wraper for [flvmeta](https://flvmeta.com/). For both Linux and Windows.
Used to extract, check, or update the metadata in *.flv video file.

## Installation
```
pip install py-flvmeta
```
Require Python >= 3.7

## Quickstart
Get MetaData tag in *.flv video file.
```Python
from pyflvmeta import flvmeta_dump
rtncode, out_or_err = flvmeta_dump("Video_path")

#Or requires a JSON format
rtncode, out_or_err = flvmeta_dump("Video_path", option = "-j")
```

Update MetaData tag in *.flv video file.
```Python
from pyflvmeta import flvmeta_update
rtncode, out_or_err = flvmeta_update("Video_path")
```


## API reference
https://flvmeta.com/flvmeta.1.html

- ```flvmeta_dump(input, options = "")```: flvmeta -D|--dump [options] INPUT_FILE
- ```flvmeta_fulldump(input, options = "")```: flvmeta -F|--full-dump [options] INPUT_FILE
- ```flvmeta_check(input, options = "")```: flvmeta -C|--check [options] INPUT_FILE
- ```flvmeta_update(input, options = "", output = "")```: flvmeta -U|--update [options] INPUT_FILE [OUTPUT_FILE]

