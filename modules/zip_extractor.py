import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive(r'C:\Users\ayaner\PycharmProjects\Python_Mega_Course\app1\files\compressed.zip', r'C:\Users\ayaner\PycharmProjects\Python_Mega_Course\app1\files')