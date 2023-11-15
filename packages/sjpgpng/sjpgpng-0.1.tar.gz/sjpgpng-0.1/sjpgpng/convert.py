def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def jpg_to_png(input_path, output_path):
    jpg_data = read_file(input_path)

    # Marqueur de début JPG
    jpg_start_marker = b'\xFF\xD8'
    # Marqueur de fin JPG
    jpg_end_marker = b'\xFF\xD9'

    # Trouver le marqueur de début et de fin JPG dans les données brutes
    start_index = jpg_data.find(jpg_start_marker)
    end_index = jpg_data.find(jpg_end_marker)

    if start_index == -1 or end_index == -1:
        raise ValueError("Le fichier n'est pas au format JPG")

    # Les données JPG à partir du marqueur de début
    jpg_data = jpg_data[start_index:end_index + 2]

    # Enregistrez les données au format PNG
    write_file(output_path, jpg_data)

    print(f"Conversion réussie : {input_path} -> {output_path}")

def png_to_jpg(input_path, output_path):
    png_data = read_file(input_path)

    # Enregistrez les données au format JPG
    write_file(output_path, png_data)

    print(f"Conversion réussie : {input_path} -> {output_path}")
