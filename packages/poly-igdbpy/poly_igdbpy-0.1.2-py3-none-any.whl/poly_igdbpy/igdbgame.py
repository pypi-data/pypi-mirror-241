import time


class IgdbGame:
    name: str
    image: str
    summary: str
    year: int
    developer: str
    imageid: str

    def getImage(self, size: str):
        return f"http://images.igdb.com/igdb/image/upload/t_{size}/{self.imageid}.jpg"

    def __init__(self, igdb: dict):
        # companies = igdb.get('involved_companies')
        self.name = igdb.get("name", "No Name")
        self.imageid = igdb.get("cover").get("image_id")
        self.image = self.getImage("cover_big")
        self.developer = igdb.get("developer", "No Developer")
        self.summary = igdb.get("summary", "No Description").replace("\n", "")
        self.year = time.gmtime(igdb.get("first_release_date", 0)).tm_year

    def validate(self):
        imageid = self.imageid
        print(f"Name: {self.name}")
        print(f"Description: {self.summary}")
        print(f"Year: {self.year}")
        print(f"ImageID: {imageid}")
        print(f"ImageThumb: {self.getImage('cover_small')}")
        print(f"ImageThumb: {self.getImage('cover_big')}")
        print(f"ImageThumb: {self.getImage('screenshot_med')}")
        print(f"Logo: {self.getImage('logo_med')}")
