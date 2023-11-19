import requests
import json
from .igdbgame import IgdbGame

def get_first( items, predicate):
    if len(items) == 0:
        return None
    for item in items:
        if predicate(item):
            return item
    return items[0]

def _getIgdbIdFromSlug(core: str) -> str:
    platforms = {
        "3do": "50",  # 3DO Interactive Multiplayer
        "actionmax": "9999",  #
        "amiga": "16",  # Amiga
        "amigacd32": "114",  # Amiga CD32
        "amstradcpc": "25",  # Amstrad CPC
        "arcade": "52",  # Arcade
        "arcade_chd": "52",  # Arcade
        "apple2": "75",  # Apple II
        "astrocade": "91",  # Bally Astrocade
        "atari2600": "59",  # Atari 2600
        "atari5200": "66",  # Atari 5200
        "atari7800": "60",  # Atari 7800
        "atari800": "65",  # Atari 8-bit
        "atarijaguar": "62",  # Atari Jaguar
        "atarijaguarcd": "410",  # Atari Jaguar CD
        "atarilynx": "61",  # Atari Lynx
        "atarist": "63",  # Atari ST/STE
        "c64": "15",  # Commodore C64/128/MAX
        "cdi": "117",  # Philips CD-i
        "channelf": "127",  # Fairchild Channel F
        "coleco": "68",  # ColecoVision
        "creativision": "",  #
        "crvision": "",  #
        "daphne": "52",  # Arcade
        "dos": "13",  # DOS
        "dreamcast": "23",  # Dreamcast
        "famicom": "51",  # Family Computer Disk System
        "fairchild": "127",  # Fairchild Channel F
        "fba": "52",  # Arcade
        "fds": "",  #
        "fmtowns": "118",  # FMTowns
        "gameandwatch": "307",  # Game & Watch
        "gamecube": "21",  # Nintendo GameCube
        "gamegear": "35",  # Sega Game Gear
        "gb": "33",  # Game Boy
        "gba": "24",  # Game Boy Advance
        "gbah": "24",  # Game Boy Advance
        "gbc": "22",  # Game Boy Color
        "gbh": "33",  # Game Boy
        "genh": "29",  # Sega Mega Drive/Genesis
        "ggh": "",  #
        "intellivision": "67",  # Intellivision
        "jaguar": "62",  # Atari Jaguar
        "genesis": "29",  # Sega Mega Drive/Genesis
        "megadrive": "29",  # Sega Mega Drive/Genesis
        "megadrive-japan": "29",  # Sega Mega Drive/Genesis
        "model123": "52",  # Arcade
        "msdos": "13",  # DOS
        "msx": "27",  # MSX
        "msx2": "53",  # MSX2
        "nds": "20",  # Nintendo DS
        "n3ds": "37",  # Nintendo 3DS
        "n64": "4",  # Nintendo 64
        "naomi": "52",  # Arcade
        "neogeo": "80",  # Neo Geo AES
        "neogeocd": "136",  # Neo Geo CD
        "nes": "18",  # Nintendo Entertainment System
        "nesh": "",  #
        "ngp": "119",  # Neo Geo Pocket
        "ngpc": "120",  # Neo Geo Pocket Color
        "nswitch": "130",  # Nintendo Switch
        "odyssey2": "",  #
        "pc": "13",  # DOS
        "pcfx": "274",  # PC-FX
        "pico": "",  #
        "ports": "",  #
        "ps1": "7",  # PlayStation
        "ps2": "8",  # PlayStation 2
        "ps3": "9",  # PlayStation 3
        "ps4": "48",  # PlayStation 4
        "ps5": "167",  # PlayStation 5
        "psp": "38",  # PlayStation Portable
        "vita": "46",  # PlayStation Vita
        "saturn": "32",  # Sega Saturn
        "Scumm": "13",  # DOS
        "scummvm": "13",  # DOS
        "sega32x": "30",  # Sega 32X
        "segacd": "78",  # Sega CD
        "segapico": "339",  # Sega Pico
        "sfc": "58",  # Super Famicom
        "sg-1000": "84",  # SG-1000
        "sgfx": "128",  # PC Engine SuperGrafx
        "mastersystem": "64",  # Sega Master System/Mark III
        "sms": "64",  # Sega Master System/Mark III
        "snes": "19",  # Super Nintendo Entertainment System
        "snesh": "19",  # Super Nintendo Entertainment System
        "pce": "86",  # TurboGrafx-16/PC Engine
        "pcengine": "86",  # TurboGrafx-16/PC Engine
        "pcenginecd": "150",  # Turbografx-16/PC Engine CD
        "tg16": "86",  # TurboGrafx-16/PC Engine
        "tg16cd": "150",  # Turbografx-16/PC Engine CD
        "ti99": "129",  # Texas Instruments TI-99
        "vectrex": "70",  # Vectrex
        "vg5000": "",  #
        "videopac": "",  #
        "virtualboy": "87",  # Virtual Boy
        "wii": "5",  # Wii
        "wiiu": "41",  # Wii U
        "wiiware": "",  #
        "wonderswan": "57",  # WonderSwan
        "wonderswancolor": "123",  # WonderSwan Color
        "x68000": "121",  # Sharp X68000
        "xbox": "11",  # Xbox
        "Zinc": "",  #
        "zmachine": "",  #
        "zxspectrum": "26",  # ZX Spectrum
    }
    return platforms.get(core.lower(), "")


class IgdbClient:
    enabled: bool

    def __init__(self, client_id, client_secret):
        if client_id == "" or client_secret == "":
            self.enabled = False
            return
        self._client_id = client_id
        self._client_secret = client_secret
        self._token = None
        self._client = requests.Session()
        self._client.headers.update(
            {"Client-ID": client_id, "Accept": "application/json"}
        )

    @property
    def is_authenticated(self):
        return self._token is not None

    async def set_auth_token(self):
        if not self.is_authenticated:
            url = f"https://id.twitch.tv/oauth2/token?client_id={self._client_id}&client_secret={self._client_secret}&grant_type=client_credentials"
            result = self._client.post(url)
            response = result.json()
            self._token = response.get("access_token")
            print(self._token)
        return self._token

    async def post(self, url, query):
        # print(f"Query: {query}")
        # Form content for the request
        print(query)
        string_content = query

        headers = {
            "Content-Type": "application/json",  # Adjust content type as needed
            "Custom-Header": "Header-Value",  # Add custom headers here
            "Authorization": f"Bearer {self._token}",
            "Client-ID": self._client_id,
        }

        # Send POST request
        response = requests.post(url, data=string_content, headers=headers)

        if response.status_code == 200:
            response_content = ""
            try:
                response_content = response.text 
                return json.loads(response_content)
            except Exception as ex:
                print(ex)

        else:
            print("Request failed: " + response.reason)

        return None

    async def getRawGame(self, name, platform):
        if not self.is_authenticated:
            await self.set_auth_token()
        platformId = _getIgdbIdFromSlug(platform)
        platformSearch = f"where platforms = ({platformId});"
        content = f'search "{name}";{platformSearch} fields  age_ratings,aggregated_rating,aggregated_rating_count,alternative_names.*,artworks.*,bundles,category,checksum,collection.*,cover.*,created_at,dlcs,expanded_games,expansions,external_games.*,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies.*,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots.*,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes.*,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;limit 20;'
        url = f"https://api.igdb.com/v4/games"
        result = await self.post(url, content)
        return result

    async def getCompany(self, id):
        if not self.is_authenticated:
            await self.set_auth_token()
        content = f" fields  *; where id = {id};"
        url = f"https://api.igdb.com/v4/companies"
        result = await self.post(url, content)
        return result[0]
    

 
    async def getGame(self, name, platform):
        igdbgames = await self.getRawGame(name, platform)
        first = get_first(igdbgames, lambda x: x.get("name") == name)
        if first:
            companies = first.get("involved_companies")
            company = ""
            if companies:
                for co in companies:
                    if co.get("developer"):
                        company = await self.getCompany(co.get("company"))
                        first["developer"] = company.get("name", "No Developer")
                        break
            if igdbgames:
                game = IgdbGame(first)
                return game
        print(f"Game {name} not found on platform {platform}")
        return None

    async def getPlatformData(self):
        if not self.is_authenticated:
            await self.set_auth_token()
        content = "fields  id,abbreviation,alternative_name,category,checksum,created_at,generation,name,platform_family,platform_logo,slug,summary,updated_at,url,versions,websites;limit 500;sort name asc;"
        url = f"https://api.igdb.com/v4/platforms"
        result = await self.post(url, content)
        return result
