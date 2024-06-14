from modules.file import FileRegexCollector


patter = r"\b\w{5}\b"
path = "./exmpl.txt"
collector = FileRegexCollector(path, patter)
print(collector.collect())