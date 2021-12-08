## Installation
python version at least 3.5 is required (test version is 3.8.3). If you download the package as a zip file from github, please rename the folder as AlphaFold_Eva.

1.  AlphaFold_Eva relies on keras with version 2.4.3

```
pip install keras==2.4.3
```

2. Add environment variables: 

For example add following lines in your ~/.bashrc  (or ~/.zshrc,, sometimes in macos system)
```
export PATH=PATH_TO_Alpha-Eva_FOLDER/AlphaFold_Eva.py:$PATH  
```
4. Open a new terminal, enter your working directory and run 
```
AlphaFold_Eva.py check
```

## Usage
1. Run One command to test one complex
```
AlphaFold_Eva.py One --total_surface [value] --contact_surface [value] --surface_ratio [value] --dimension_ratio [value] 
``` 
2. Run Multi command to test multi complexes
```
AlphaFold_Eva.py Multi [input file path]
```


<!---
xiong19912010/xiong19912010 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
