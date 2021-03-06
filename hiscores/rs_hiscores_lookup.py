import urllib.request
import json


class HiscoresScraper(object):

    def __init__(self, name, account='normal', game='osrs'):
        self.name = name
        self.account = account
        self.game = game
        self.hiscores = {}
        self.url_starts = {
            'normal': 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=',
            'ironman': 'https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player=',
            'hardcore': 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player=',
            'ultimate': 'https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.ws?player=',
            'rs3normal': 'https://secure.runescape.com/m=hiscore/index_lite.ws?player=',
            'rs3ironman': 'https://secure.runescape.com/m=hiscore_ironman/index_lite.ws?player=',
            'rs3hardcore': 'https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player='

        }
        self.rs3skills = [
            'Total',
            'Attack',
            'Defence',
            'Strength',
            'Hitpoints',
            'Ranged',
            'Prayer',
            'Magic',
            'Cooking',
            'Woodcutting',
            'Fletching',
            'Fishing',
            'Firemaking',
            'Crafting',
            'Smithing',
            'Mining',
            'Herblore',
            'Agility',
            'Thieving',
            'Slayer',
            'Farming',
            'Runecrafting',
            'Hunter',
            'Construction',
            'Summoning',
            'Dungeoneering',
            'Divination',
            'Invention'
        ]
        self.osrsskills = [
            'Total',
            'Attack',
            'Defence',
            'Strength',
            'Hitpoints',
            'Ranged',
            'Prayer',
            'Magic',
            'Cooking',
            'Woodcutting',
            'Fletching',
            'Fishing',
            'Firemaking',
            'Crafting',
            'Smithing',
            'Mining',
            'Herblore',
            'Agility',
            'Thieving',
            'Slayer',
            'Farming',
            'Runecrafting',
            'Hunter',
            'Construction'
        ]
        self.refresh_hiscores()

    @staticmethod
    def fetch_hiscores(url):
        return urllib.request.urlopen(url).read().decode("utf-8")

    def refresh_hiscores(self):
        if self.game == 'osrs':
            if self.account not in self.url_starts:
                raise Exception('Invalid account type, should be normal, ironman, hardcore or ultimate')
            url = self.url_starts[self.account]+self.name
            page = HiscoresScraper.fetch_hiscores(url)
            page = page.split('\n')
            for i, skill in enumerate(self.osrsskills):
                line = page[i].split(',')
                self.hiscores[skill] = {
                    'rank': int(line[0]),
                    'level': int(line[1]),
                    'exp': int(line[2])
                }
        elif self.game == 'rs3':
            if 'rs3'+self.account not in self.url_starts:
                raise Exception('Invalid account type, should be normal, ironman or hardcore')
            url = self.url_starts['rs3'+self.account]+self.name
            page = HiscoresScraper.fetch_hiscores(url)
            page = page.split('\n')
            for i, skill in enumerate(self.rs3skills):
                line = page[i].split(',')
                self.hiscores[skill] = {
                    'rank': int(line[0]),
                    'level': int(line[1]),
                    'exp': int(line[2])
                }
        else:
            raise Exception('Invalid game mode, should be osrs or rs3')

    def get_skill(self, chosen_skill):
        return self.hiscores[chosen_skill]

    def json_hiscores(self):
        return json.dumps(self.hiscores)

    def json_get_skill(self, chosen_skill):
        return json.dumps(self.hiscores[chosen_skill])


