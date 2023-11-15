#!/usr/bin/env python3
# Krishna Bhattarai
# Nov 23
import re


class PLYObject:
    def __init__(self, vertices, faces, colors, name=None):
        self.name = name
        self.vertices = vertices
        self.faces = faces
        self.colors = colors


def get_file_data(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data


def parse_ply_file_data(lines):
    expected_faces = None
    expected_vertices = None
    vertices, faces, colors = [], [], []

    vertex_count = 0
    faces_count = 0

    property_red = 0
    property_blue = 0
    property_green = 0

    for x in range(0, len(lines)):
        line = lines[x].strip()
        if not line or line == '':
            continue
        if line.startswith("format"):
            file_format = line.strip().split()[1]
            if file_format.lower() != "ascii":
                # print("File format is not ascii! It is: %s" % file_format)
                raise ValueError("File format is not ascii! It is: %s" % file_format)

        if line.startswith("comment"):
            continue

        if "element vertex" in line:
            expected_vertices = int(re.match(r'^element\s+vertex\s+(\d+)', line).group(1))
            continue

        if "property uchar red" in line:
            property_red += 1
            continue

        if "property uchar green" in line:
            property_green += 1
            continue

        if "property uchar blue" in line:
            property_blue += 1
            continue

        if re.match(r'^element\s+face\s+\d+', line):
            expected_faces = int(re.match(r'^element\s+face\s+(\d+)', line).group(1))
            continue

        elif "end_header" in line:
            continue

        if re.match(r'^([-|\d]+(\.\d+)?)\s+([-|\d]+(\.\d+)?)\s+([-|\d]+(\.\d+)?)', line) and vertex_count != expected_vertices:
            vertex_count += 1

            if property_red and property_green and property_blue:
                vertex = line.strip().split()[0:6]
                vertices.append([float(vertex[0]), float(vertex[1]), float(vertex[2])])
                colors.append([float(vertex[3]), float(vertex[4]), float(vertex[5])])
            else:
                vertex = line.strip().split()[0:3]
                vertices.append([float(vertex[0]), float(vertex[1]), float(vertex[2])])

        if re.match(r'^[34]\s+\d+\s+\d+\s\d+', line) and faces_count != expected_faces:
            faces_count += 1
            if line[0].startswith('3'):
                face = line.strip().split()[1:4]
                faces.append([int(face[0]), int(face[1]), int(face[2])])
            elif line[0].startswith('4'):
                face = line.strip().split()[1:5]
                faces.append([int(face[0]), int(face[1]), int(face[2]), int(face[3])])

    if len(vertices) != expected_vertices:
        # print("Error: total vertices read: %s does not match expected vertices: %s" % (len(vertices), expected_vertices))
        raise ValueError("Error: total vertices read: %s does not match expected vertices: %s" % (len(vertices), expected_vertices))

    if len(faces) != expected_faces:
        # print("Error: total faces read: %s does not match expected faces: %s" % (len(faces), expected_faces))
        raise ValueError("Error: total faces read: %s does not match expected faces: %s" % (len(faces), expected_faces))

    return [vertices, faces, colors]


def parse_ply_file(file_name):
    file_data_lines = get_file_data(file_name)
    parsed_data = parse_ply_file_data(file_data_lines)
    if parsed_data:
        v, f, c = parsed_data[0], parsed_data[1], parsed_data[2]
        return PLYObject(v, f, c, file_name.strip())
