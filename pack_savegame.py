import pickle
import renpy
import zipfile
import os
import struct
import sys

version = os.getenv("YARPE_VERSION", "custom build")

if len(sys.argv) != 2 or sys.argv[1] not in ("PS4", "PS5"):
    print("Usage: python3 pack_savegame.py <PS4|PS5>")
    sys.exit(1)

console_kind = sys.argv[1]

SCRIPT = """
import sys
import os
import traceback

try:
    sys.path.insert(0, "/saves")
    os.environ["CONSOLE_KIND"] = "%s"

    import constants
    from constants import VERSION
    from utils_rp import log, log_exc

    constants.rp = renpy

    log("=== YET ANOTHER RENPY EXPLOIT " + VERSION + " ===")
    scope = dict(globals(), **locals())
    execfile("/saves/main.py")
except Exception as exc:
    exc_msg = traceback.format_exc()
    # notify vanishes on the crash screen, so keep a copy on disk
    try:
        open("/saves/yarpe_error.txt", "w").write(exc_msg)
    except Exception:
        pass
    renpy.notify("YARPE failed to start:\\n" + exc_msg)
""" % console_kind


class Yummy(object):
    def __reduce__(self):
        return renpy.python.py_exec, (SCRIPT,)


def list_files(start_path):
    all_files = []
    for root, _, files in os.walk(start_path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files


def scan_src_directory():
    files = []
    PREFIX = "./src"

    for entry in os.scandir(PREFIX):
        if not entry.is_file():
            continue

        filename = entry.path
        mod_time = int(os.path.getmtime(filename))
        rel_path = "/saves/" + os.path.basename(filename)

        files.append((rel_path, mod_time))

    files.sort(key=lambda x: x[0])
    return files


def scan_yarpe_autoload_directory():
    files = []
    PREFIX = "./yarpe_autoload"

    for filename in list_files(PREFIX):
        if os.path.dirname(filename) != PREFIX:
            raise ValueError("Autoload files must be in the yarpe_autoload root")

        mod_time = int(os.path.getmtime(filename))
        rel_path = "/saves/" + os.path.basename(filename)

        files.append((rel_path, mod_time))

    files.sort(key=lambda x: x[0])
    return files


def create_saveindex(files, output_path):
    with open(output_path, "wb") as f:
        f.write(struct.pack("<I", len(files)))

        for filepath, timestamp in files:
            f.write(struct.pack("<II", timestamp, 0))
            filename_bytes = filepath.encode("utf-8")
            f.write(struct.pack("<I", len(filename_bytes)))
            f.write(filename_bytes)
            f.write(b"\x00")


def main():
    with open("src/version.txt", "w") as f:
        f.write(version)

    src_files = scan_src_directory()
    autoload_files = scan_yarpe_autoload_directory()

    if not src_files:
        print("Error: no files found to index!")
        sys.exit(1)

    indexed_files = src_files + autoload_files
    indexed_paths = [filepath for filepath, _ in indexed_files]
    if len(indexed_paths) != len(set(indexed_paths)):
        print("Error: duplicate savedata filename found!")
        sys.exit(1)

    pickled = pickle.dumps(Yummy(), protocol=2)
    with open("savegame_container/log", "wb") as f:
        f.write(pickled)

    with zipfile.ZipFile("1-1-LT1.save", "w", compression=zipfile.ZIP_DEFLATED) as zip:
        zip.write("savegame_container/screenshot.png", "screenshot.png")
        zip.write("savegame_container/extra_info", "extra_info")
        zip.write("savegame_container/json", "json")
        zip.write("savegame_container/renpy_version", "renpy_version")
        zip.write("savegame_container/log", "log")

    save_files = indexed_files + [
        ("/saves/1-1-LT1.save", int(os.path.getmtime("1-1-LT1.save"))),
        ("/saves/persistent", 0),
    ]

    output_path = "-saveindex"
    create_saveindex(save_files, output_path)

    with zipfile.ZipFile("save.zip", "w") as zipf:
        zipf.write(output_path, "-saveindex")
        zipf.write("1-1-LT1.save", "1-1-LT1.save")
        for files, local_root in (
            (src_files, "src"),
            (autoload_files, "yarpe_autoload"),
        ):
            for filepath, _ in files:
                filename = filepath[len("/saves/") :]
                local_path = os.path.join(local_root, filename)
                zipf.write(local_path, filename)

    print(
        "Success: save.zip generated for %s (%d files, version %s)"
        % (console_kind, len(save_files), version)
    )


if __name__ == "__main__":
    main()
