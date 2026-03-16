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

        for i in range(1,len(directories)):
            cur = "/".join(directories[:i]) or "/"   

            if cur not in self.paths or directories[i] not in self.paths[cur]:
                bisect.insort(self.paths[cur], directories[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        if filePath not in self.files: 
            self.mkdir(filePath)
        
        self.files[filePath] += content #appending content to the file

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath] #this will be filename with its path i.e, /a/b/c.txt


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
