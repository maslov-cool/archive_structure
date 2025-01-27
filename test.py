from zipfile import ZipFile


with ZipFile(input('введите архив')) as myzip:
    info = myzip.infolist()
for i in info:
    if i.orig_filename[-1] == '/':
        print((i.orig_filename.count('/') - 1) * '  ' + i.orig_filename.split('/')[-2])
    else:
        print(i.orig_filename.count('/') * '  ' + i.orig_filename.split('/')[-1])
