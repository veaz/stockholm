# Stockholm v0.1 

### Created during a Cybersecurity Bootcamp at 42 Barcelona

Stockholm is a cybersecurity tool designed for educational purposes. It simulates the behavior of ransomware by targeting specific file extensions, similar to the infamous Wannacry ransomware.

> **Disclaimer**: This tool is intended for educational and research purposes only. Do not use it for malicious intent or on any system without explicit permission.

## Features:

- Targets the "infection" folder and its subfolders in the user's root directory `~/infection`.
- Searches for and "infects" files with specific extensions.
- Generates a "key.key" file to store the decryption key. If this file already exists, the program will utilize the existing key.

## Usage:

1. **Encryption**: 
   ```bash
   python stockholm.py
    ```

2. **Decryption with a specified key**:
    ```bash
   python stockholm.py -r KEY
    ```

3. **Decryption using the key in "key.key"**:
    ```bash
   python stockholm.py -rk
    ```

## Flags:
- -h : Display help message.
- -k : Generate a new key.
- -r : Decrypt all encrypted files.
- -rk : Decrypt files using the key stored in "key.key".
- -s : Run the program silently (no output).
- -v : Display program version.

## Targeted Extensions:
```
.der, .pfx, .key, .cr, .csr, .p12, .pem, .od, .o, .sxw, .stw, .uo, .3ds, .max, .3dm, .txt, .ods, .ots, .sxc, .stc, .dif, .slk, .wb2, .odp, .otp, .sxd, .std, .uop, .odg, .otg, .sxm, .mml, .lay, .lay6, .asc, .sqlite3, .sqlitedb, .sql, .accdb, .mdb, .db, .dbf, .odb, .frm, .myd, .myi, .ibd, .mdf, .ldf, .sln, .suo, .cs, .c, .cpp, .pas, .h, .asm, .js, .cmd, .ba, .ps1, .vbs, .vb, .pl, .dip, .dch, .sch, .brd, .jsp, .php, .asp, .rb, .java, .jar, .class, .sh, .mp3, .wav, .swf, .fla, .wmv, .mpg, .vob, .mpeg, .asf, .avi, .mov, .mp4, .3gp, .mkv, .3g2, .flv, .wma, .mid, .m3u, .m4u, .djvu, .svg, .ai, .psd, .nef, .tiff, .tif, .cgm, .raw, .gif, .png, .bmp, .jpg, .jpeg, .vcd, .iso, .backup, .zip, .rar, .7z, .gz, .tgz, .tar, .bak, .tbk, .bz2, .PAQ, .ARC, .aes, .gpg, .vmx, .vmdk, .vdi, .sldm, .sldx, .sti, .sxi, .602, .hwp, .sn, .onetoc2, .dwg, .pdf, .wk1, .wks, .123, .rtf, .csv, .tx, .vsdx, .vsd, .edb, .eml, .msg, .os, .ps, .potm, .potx, .ppam, .ppsx, .ppsm, .pps, .po, .pptm, .pptx, .pp, .xltm, .xltx, .xlc, .xlm, .xl, .xlw, .xlsb, .xlsm, .xlsx, .xls, .dotx, .dotm, .do, .docm, .docb, .docx, .doc

```
