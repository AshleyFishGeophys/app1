import zipfile as zf
import pathlib


def make_archive(filepaths, destination_dir):
    destination_path = pathlib.Path(destination_dir, "compressed_2.zip")
    with zf.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)  # this line is missing
            archive.write(filepath, arcname=filepath.name)


# Test to see if the code is working
if __name__ == '__main__':
    make_archive(filepaths=['../files/a.txt', '../files/b.txt'], destination_dir='../files')
