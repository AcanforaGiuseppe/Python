class DirectoryEntry:

    def __init__(self, filename, extension, attributes, creation_time,
                 creation_date, cluster_number, filesize):
        self.filename = filename
        self.extension = extension
        self.attributes = attributes
        self.creation_time = creation_time
        self.creation_date = creation_date
        self.cluster_number = cluster_number
        self.filesize = filesize
