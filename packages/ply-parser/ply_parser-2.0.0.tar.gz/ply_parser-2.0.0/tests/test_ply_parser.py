import unittest
from ply_parser import *


class TestPLYParsing(unittest.TestCase):
    def test_parse_ply_data_with_vertices_and_faces(self):
        data = """ply
    format ascii 1.0
    comment Some comment
    element vertex 3
    property float x
    property float y
    property float z
    element face 1
    end_header
    1.0 2.0 3.0
    4.0 5.0 6.0
    7.0 8.0 9.0
    3 0 1 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(faces), 1)
        self.assertEqual(len(colors), 0)

    def test_parse_ply_data_with_vertices_colors_and_faces(self):
        data = """ply
    format ascii 1.0
    element vertex 3
    property float x
    property float y
    property float z
    property uchar red
    property uchar green
    property uchar blue
    element face 1
    property list uchar int vertex_indices
    end_header
    1.0 2.0 3.0 255 0 0
    4.0 5.0 6.0 0 255 0
    7.0 8.0 9.0 0 0 255
    3 0 1 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(faces), 1)
        self.assertEqual(len(colors), 3)

    def test_distinguish_and_count_lines_for_vertices_and_faces(self):
        data = """ply
format ascii 1.0
element vertex 3
property float x
property float y
property float z
element face 3
property list uchar int vertex_indices
end_header
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
3 2 1 2
3 2 2 3
3 1 2 3"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(vertices, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(len(faces), 3)
        self.assertEqual(faces, [[2, 1, 2], [2, 2, 3], [1, 2, 3]])
        self.assertEqual(len(colors), 0)

    def test_handle_face_lines_starting_with_4(self):
        data = """ply
    format ascii 1.0
    element vertex 3
    property float x
    property float y
    property float z
    element face 3
    property list uchar int vertex_indices
    end_header
    1.0 2.0 3.0
    4.0 5.0 6.0
    7.0 8.0 9.0
    4 2 1 2 2
    4 2 2 3 1
    4 1 2 3 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(vertices, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(len(faces), 3)
        self.assertEqual(faces, [[2, 1, 2, 2], [2, 2, 3, 1], [1, 2, 3, 2]])
        self.assertEqual(len(colors), 0)

    def test_parse_ply_data_with_no_vertices_or_faces(self):
        data = """ply
format ascii 1.0
element vertex 0
element face 0
end_header"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 0)
        self.assertEqual(len(faces), 0)
        self.assertEqual(len(colors), 0)

    def test_handle_invalid_ply_format(self):
        invalid_format_data = """ply
format binary 1.0
element vertex 3
property float x
property float y
property float z
end_header
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0"""

        with self.assertRaises(ValueError) as context:
            parse_ply_file_data(invalid_format_data.splitlines())
        self.assertEqual(str(context.exception), 'File format is not ascii! It is: binary')

    def test_handle_incomplete_vertex_data(self):
        incomplete_vertex_data = """ply
    format ascii 1.0
    element vertex 3
    property float x
    property float y
    property float z
    end_header
    1.0 2.0 3.0
    4.0 5.0 6.0"""

        with self.assertRaises(ValueError) as context:
            parse_ply_file_data(incomplete_vertex_data.splitlines())
        self.assertEqual(str(context.exception), 'Error: total vertices read: 2 does not match expected vertices: 3')

    def test_parse_ply_colors_data_if_described_in_header(self):
        data = """ply
format ascii 1.0
element vertex 3
property float x
property float y
property float z
property uchar red
property uchar green
property uchar blue
element face 1
end_header
1.0 2.0 3.0 255 0 0
4.0 5.0 6.0 0 255 0
7.0 8.0 9.0 0 0 255
3 0 1 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(faces), 1)
        self.assertEqual(len(colors), 3)
        self.assertEqual(colors, [[255, 0, 0], [0, 255, 0], [0, 0, 255]])

    def test_not_parse_colors_if_color_property_not_described(self):
        data = """ply
format ascii 1.0
element vertex 3
property float x
property float y
property float z
element face 1
end_header
1.0 2.0 3.0 255 0 0
4.0 5.0 6.0 0 255 0
7.0 8.0 9.0 0 0 255
3 0 1 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(faces), 1)
        self.assertEqual(len(colors), 0)

    def test_parse_ply_data_with_negative_coordinates(self):
        data = """ply
format ascii 1.0
element vertex 3
property float x
property float y
property float z
element face 1
end_header
-1.0 -2.0 -3.0
-4.0 -5.0 -6.0
-7.0 -8.0 -9.0
3 0 1 2"""

        result = parse_ply_file_data(data.splitlines())
        vertices, faces, colors = result[0], result[1], result[2]
        self.assertEqual(len(vertices), 3)
        self.assertEqual(len(faces), 1)
        self.assertEqual(len(colors), 0)

    def test_handle_incomplete_face_data(self):
        incomplete_face_data = """ply
format ascii 1.0
element vertex 3
element face 2
end_header
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
3 0 1 2"""

        with self.assertRaises(ValueError) as context:
            parse_ply_file_data(incomplete_face_data.splitlines())
        self.assertEqual(str(context.exception), 'Error: total faces read: 1 does not match expected faces: 2')


if __name__ == '__main__':
    unittest.main()
