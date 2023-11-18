## Usage

Once installed usage is straight forward, to search for files with the defaults, looking in the current directory for
`jpg` files and outputting to `YYYY-mm-dd` directory structure in the current directory just invoke `mvdate`. the
`ctime` (creation time) of a file, which is immutable, is extracted and used as a basis for creating directories.

Thus, given a directory with the following files...

```bash
❱ l
drwxrwx--- syncthing syncthing 4.0 KB Sun Jan 29 07:04:17 2023  .
drwxrwxrwx neil      users     4.0 KB Mon Sep  4 21:38:15 2023  ..
.rw-rw---- syncthing syncthing 2.5 MB Fri Oct 23 08:57:20 2020  IMG_20201023_085720.jpg
.rw-rw---- syncthing syncthing 2.5 MB Fri Oct 23 08:57:24 2020  IMG_20201023_085725.jpg
.rw-rw---- syncthing syncthing 2.4 MB Fri May 20 07:51:04 2022  IMG_20210115_091528.jpg
.rw-rw---- syncthing syncthing 2.4 MB Fri May 20 07:51:04 2022  IMG_20210115_091530.jpg
.rw-rw---- syncthing syncthing 2.6 MB Fri Apr  1 10:35:44 2022  IMG_20220401_093544.jpg
.rw-rw---- syncthing syncthing 2.6 MB Fri Apr  1 10:35:46 2022  IMG_20220401_093546.jpg
.rw-rw---- syncthing syncthing 2.5 MB Sun Jan 29 05:21:28 2023  IMG_20220729_085918.jpg
.rw-rw---- syncthing syncthing 2.4 MB Sun Jan 29 05:21:28 2023  IMG_20220729_085951.jpg
.rw-rw---- syncthing syncthing 2.7 MB Sun Jan 29 05:24:40 2023  IMG_20221021_085226.jpg
.rw-rw---- syncthing syncthing 2.5 MB Sun Jan 29 05:24:40 2023  IMG_20221021_085231.jpg
```

To move them to `YYYY-mm-dd` directory just invoke `mvdate` as the default file extensions is `jpg` and the method used
is `exif` which extracts the `Created date` from the Exif data.

```bash
mvdate
2023-11-04 09:12:12.887 | INFO     | Created target directory : 2020/10/23
2023-11-04 09:12:12.888 | INFO     | Created target directory : 2022/04/01
2023-11-04 09:12:12.888 | INFO     | Created target directory : 2022/05/20
2023-11-04 09:12:12.889 | INFO     | Created target directory : 2023/01/29
```

### Options

| Option (Short) | Option (Long) | Description                                                                                                                                                                                                                       |
|----------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-v`           | `--version`   | Print out the version and exit.                                                                                                                                                                                                   |
| `-b`           | `--base`      | The base directory under which files are searched for.                                                                                                                                                                            |
| `-l`           | `--log_file`  | File to save log output to.                                                                                                                                                                                                       |
| `-m`           | `--method`    | Method used to extract date/time of file. Currently three options `exif` (default) which uses the `Created Date` field of Exif data of image files. For non-image files use either `ctime` or `mtime` for created/modified times. |
| `-n`           | `--nesting`   | Level of nesting to move files to, should be a single letter, 'Y'ear, 'm'onth, 'd'ay (default), 'H'our, 'M'inutes.                                                                                                                |
| `-q`           | `--quiet`     | Execute quietly and suppress all output.                                                                                                                                                                                          |
| `-s`           | `--single`    | Whether to have a single directory of the form `YYYY-mm[-dd[-HH[-MM]]]` rather than a nested structure.                                                                                                                           |
