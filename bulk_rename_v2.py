import os, pathlib, zipfile, re

def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower()
            for text in _nsre.split(s)]

def main():
    path = pathlib.Path().resolve()

    for root, dirs, files in os.walk(path):
        print('\nWorking in path: \n' + root + '\n')
        for c, f_name in enumerate(dirs,1):
            c = format(c,'03d')
            sauce = path / f_name
            print(sauce, end = ' --> ')
            target = path / c
            print(target)
            os.rename(sauce, target)

    for root, dirs, files in os.walk(path):
        count = 1
        # files.sort()
        files.sort(key=natural_sort_key) #sorting in natural selection
        for file in files:
            if file.endswith(('.jpg', '.png')):
                src = path / root / file
                print(src, end = ' --> ')
                count = format(count, '03d')
                file_name = "P" + count + ".png"
                dest = path / root / file_name
                print(dest)
                os.rename(src, dest)
                count = int(count) + 1

    for folder in os.listdir():
        if os.path.isdir(folder):
            new_path = path / folder
            for root, dirs, files in os.walk(new_path):
                i = 1
                print('\nArchiving:')
                for file in files:
                    print(i, end = ';', flush = True)
                    i += 1
                    with zipfile.ZipFile(folder + '.zip', 'a') as zips:
                        zips.write(os.path.relpath(os.path.join(root, file), os.path.join(folder, '..')), file)

if __name__ == '__main__':
    main()
