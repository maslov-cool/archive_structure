from zipfile import ZipFile


def human_read_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    n = size
    i = 0
    while n // 1024:
        i += 1
        n //= 1024
    return str(round(size / 1024 ** i)) + sizes[i]


with ZipFile('input.zip') as myzip:
    info = myzip.infolist()
for i in info:
    if i.orig_filename[-1] == '/':
        print((i.orig_filename.count('/') - 1) * '  ' + i.orig_filename.split('/')[-2])
    else:
        print(i.orig_filename.count('/') * '  ' + i.orig_filename.split('/')[-1] + ' ' +
              str(human_read_format(i.file_size)))

