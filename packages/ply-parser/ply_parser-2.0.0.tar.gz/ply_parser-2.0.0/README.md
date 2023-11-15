### PLY File Parser
This Python module provides a simple PLY (Polygon File Format) file parser. It includes a class PLYObject for storing PLY file data and a function parse_ply_file for reading PLY files and creating PLYObject instances.

### Usage
### PLYObject Class
The PLYObject class represents a PLY object with attributes:

`name`: Name of the PLY object.

`vertices`: List of vertex coordinates.

`faces`: List of face indices.

`colors`: List of RGB color values for vertices.


#### parse_ply_file Function
The parse_ply_file function takes a PLY file as input and returns a PLYObject instance. It reads the file, extracts vertex and face information, and handles color properties. If any inconsistencies or errors are detected in the PLY file, appropriate error messages are displayed.
```
file = "data/cube_colors.ply"
parsed_object = parse_ply_file(file)
if parsed_object:
    print("name:", parsed_object.name)
    print("total_vertices:", len(parsed_object.vertices))
    print("total_faces:", len(parsed_object.faces))
    print("total_colors:", len(parsed_object.colors))
```

### Requirements
`Python 3.11.x`

### PLY File Format Support
This parser currently supports PLY files with the following characteristics:

`ASCII format`

`Vertex coordinates (X, Y, Z)`

`Face indices (triangles and quads)`

`Vertex colors`

### Testing
```
python3 -m unittest tests/test_ply_parser.py -v
```

### Limitations
The parser assumes the input PLY file follows the standard specifications.
It may not handle non-standard or corrupted PLY files gracefully.


### Contribution
Feel free to contribute by opening issues or submitting pull requests. Bug reports, suggestions, and improvements are welcome.

### License
This PLY file parser is licensed under the MIT License. See the LICENSE file for details.