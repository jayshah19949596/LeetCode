class FileSystem:

    def __init__(self):
        self.paths = collections.defaultdict(list) #we store paths as key and its sub directory as value e.g. '/':['a'], '/a':['b'], '/a/b':['c']
        self.files = collections.defaultdict(str) #we store file (with its path) as key and its content as value

    def ls(self, path: str) -> List[str]:
        if path in self.files:
            return [path.split("/")[-1]]
        else:
            return self.paths[path]

    def mkdir(self, path: str) -> None:
        directories = path.split("/")

        # Start from 1 because index 0 is the empty string before the first "/"
        for i in range(1, len(directories)):
            parent_path = "/".join(directories[:i])
            if parent_path == "": parent_path = "/"
            current_dir = directories[i]
            if current_dir not in self.paths[parent_path]:
                bisect.insort(self.paths[parent_path], current_dir)


    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files: 
            self.mkdir(filePath)
        
        self.files[filePath] += content #appending content to the file

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath] #this will be filename with its path i.e, /a/b/c.txt



