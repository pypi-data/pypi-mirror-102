import tldextract

class JobUtils:

    def __init__(self):
        self.tld_extractor = tldextract.TLDExtract(cache_file='../tld_lists.txt')

    def parse(self, record):
        ext = self.tld_extractor(record)
        return ext
