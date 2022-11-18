import struct

from entryDirectory import DirectoryEntry
from fileInfos import FileInfos


class Fat16Reader:

    _attributes = {
        0x01: "read_only",
        0x02: "hidden",
        0x04: "system",
        0x08: "volume_id",
        0x10: "directory",
        0x20: "archive",
    }

    _fat_16_notable_values = {
        0x0000: "cluster clear",
        0x0001: "not allowed",
        0xFFF7: "one/more bad sectors in cluster",
        0xFFF8: "end of file",
        0xFFFF: "end of file"
    }
    _entry_size = 32
    _fat_cluster_read_start = 2

    def __init__(self, file_path: str, do_print_on_commands: bool = False):
        self.do_print_on_commands = do_print_on_commands
        with open(file_path, "rb") as f:
            self.image = f.read()
        self.volume_id = ""
        self._read_boot_sector()
        self._current_root = self._root_directory_offset
        self._current_entries = self._read_directory(self._current_root)

    def _read_boot_sector(self):
        self._reserved_sectors = self._read_ushort(14)
        self._sector_size = self._read_ushort(11)
        self._cluster_size = self.image[13]  # expressed in sectors
        self._fat_offset = self._reserved_sectors * self._sector_size
        self._fat_size = self._read_ushort(22)
        self._fat_copies = self.image[16]
        self._root_directory_offset = self._fat_offset +\
            (self._fat_size * self._fat_copies * self._sector_size)
        self._root_directory_entries = self._read_ushort(17)
        self._root_directory_size = self._root_directory_entries * self._entry_size
        self._clusters_offset = self._root_directory_offset + self._root_directory_size

    def _read_directory(self, offset) -> list[DirectoryEntry]:
        entry_offset = offset
        entries = []
        while self.image[entry_offset] != 0x00:
            entries.append(self._read_entry(entry_offset))
            entry_offset += self._entry_size
        return entries

    def _read_entry(self, byte_offset) -> DirectoryEntry:
        name = self.image[byte_offset:byte_offset + 8]
        extension = self.image[byte_offset + 8:byte_offset+11]
        entry_filename = name.decode("utf-8").strip()
        entry_extension = extension.decode("utf-8").strip()
        attributes_byte = self.image[byte_offset+11]
        entry_attributes = []

        for attribute in self._attributes:
            if attributes_byte & attribute:
                entry_attributes.append(self._attributes[attribute])

        creation_time = self._read_ushort(byte_offset + 14)
        creation_date = self._read_ushort(byte_offset + 16)
        cluster_number = self._read_ushort(byte_offset + 26)
        filesize = struct.unpack(
            "<I", self.image[byte_offset + 28:byte_offset + 32])[0]
        return DirectoryEntry(
            entry_filename, entry_extension, entry_attributes, creation_date,
            creation_time, cluster_number, filesize)

    def _check_next_in_fat(self, cluster_number):
        fat_16_value = self._read_ushort(self._fat_offset + cluster_number * 2)
        has_next_cluster = True

        if fat_16_value in self._fat_16_notable_values:
            has_next_cluster = False

        return (has_next_cluster, fat_16_value)

    def _read_ushort(self, offset):
        return struct.unpack("<H", self.image[offset:offset + 2])[0]

    def _get_clusters_list(self, entry: DirectoryEntry) -> list[int]:
        if (entry.cluster_number == 0):
            return []
        clusters_list = [entry.cluster_number]
        next_cluster_tuple = self._check_next_in_fat(entry.cluster_number)
        while next_cluster_tuple[0]:
            clusters_list.append(next_cluster_tuple[1])
            next_cluster_tuple = self._check_next_in_fat(next_cluster_tuple[1])
        return clusters_list

    def _cd_set_current_entries(self, linked_list):
        self._current_entries = []
        for cluster in linked_list:
            cluster_start = self._clusters_offset +\
                self._cluster_size * self._sector_size *\
                (cluster - self._fat_cluster_read_start)
            self._current_entries.extend(self._read_directory(cluster_start))

    def _compose_file(self, clusters_list, entry: DirectoryEntry):
        file = FileInfos(entry.filename, entry.extension, entry.filesize, b'')
        bytes = entry.filesize
        file_bytes = []
        cluster_bytes = self._cluster_size * self._sector_size
        for cluster in clusters_list:
            cluster_start = self._clusters_offset +\
                self._cluster_size * self._sector_size *\
                (cluster - self._fat_cluster_read_start)

            if bytes >= cluster_bytes:
                file_bytes.append(self.image[cluster_start:cluster_start + cluster_bytes])
                bytes -= cluster_bytes
            else:
                file_bytes.append(self.image[cluster_start:cluster_start+bytes])

        file.bytes = file_bytes[0]
        return file

    # Prompt Commands
    def ls(self):
        if self.do_print_on_commands:
            print("MODE\t\t\t\tSIZE\t\t\tNAME")
            for entry in self._current_entries:
                if "archive" in entry.attributes or "read_only" in entry.attributes:
                    print(f"{entry.attributes}\t\t\t", end="")
                    print(f"{entry.filesize}\t\t\t", end="")
                    print(f"{entry.filename}.{entry.extension}\t\t\t")
                else:
                    print(f"{entry.attributes}\t\t\t", end="")
                    print(f"{entry.filesize}\t\t\t", end="")
                    print(f"{entry.filename}\t\t\t")

        return self._current_entries

    def cd(self, directory_name) -> list[DirectoryEntry]:
        found = False

        for entry in self._current_entries:
            if "directory" in entry.attributes and entry.filename == directory_name:
                clusters_linked_list = self._get_clusters_list(entry)
                if len(clusters_linked_list) > 0:
                    self._cd_set_current_entries(clusters_linked_list)
                else:
                    self._current_entries = self._read_directory(
                        self._root_directory_offset)
                found = True

        if not found and self.do_print_on_commands:
            print("There is no such directory")
            return None
        elif not found and not self.do_print_on_commands:
            raise self.NotADirectoryException()

        return self._current_entries

    def open_file(self, filename):
        found = False
        for entry in self._current_entries:
            if entry.filename == filename:
                found = True
                if "archive" in entry.attributes or "read_only" in entry.attributes:
                    clusters_list = self._get_clusters_list(entry)
                    file = self._compose_file(clusters_list, entry)

        if not found and self.do_print_on_commands:
            print("File not found!")
            return None

        if not found and not self.do_print_on_commands:
            raise self.NotAFileException()

        if self.do_print_on_commands:
            print(f"{file.filename}.{file.extension} content =\n" +
                  str(file.bytes, "utf-8"))

        return file
