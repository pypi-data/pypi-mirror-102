from .cached_object import CachedObject

"""
{

    "url": "https://nookipedia.com/wiki/Ribbot",
    "name": "Ribbot",
    "alt_name": "",
    "title_color": "bfbfbf",
    "text_color": "5e5e5e",
    "id": "flg01",
    "image_url": "https://dodo.ac/np/images/9/94/Ribbot_NH.png",
    "species": "Frog",
    "personality": "Jock",
    "gender": "Male",
    "birthday": "February 13",
    "sign": "Aquarius",
    "quote": "Never rest, never rust.",
    "phrase": "zzrrbbit",
    "prev_phrases": 

[

    "toady"

],
"clothing": "Simple Parka",
"islander": false,
"debut": "DNM",
"appearances": 
[

    "DNM",
    "AC",
    "E_PLUS",
    "WW",
    "CF",
    "NL",
    "WA",
    "NH",
    "HHD",
    "PC"

],
"nh_details": 
{

    "image_url": "https://dodo.ac/np/images/9/94/Ribbot_NH.png",
    "photo_url": "https://dodo.ac/np/images/0/03/RibbotPicACNH.png",
    "icon_url": "https://dodo.ac/np/images/8/87/Ribbot_NH_Villager_Icon.png",
    "quote": "Never rest, never rust.",
    "sub-personality": "B",
    "catchphrase": "zzrrbbit",
    "clothing": "Simple Parka",
    "clothing_variation": "Light Blue",
    "fav_styles": 

[

    "Simple",
    "Active"

],
"fav_colors": 

        [
            "Blue",
            "Aqua"
        ],
        "hobby": "Fitness",
        "house_interior_url": "https://dodo.ac/np/images/8/86/House_of_Ribbot_NH.png",
        "house_exterior_url": "https://dodo.ac/np/images/4/42/House_of_Ribbot_NH_Model.png",
        "house_wallpaper": "Circuit-Board Wall",
        "house_flooring": "Future-Tech Flooring",
        "house_music": "K.K. Technopop",
        "house_music_note": ""
    }

}"""


class Villager(CachedObject):
    """
    Object representing a Villager.

    :param data: JSON from API endpoint as dict.

    :var self.message: message from nookipedia
    :var self.name: name of the villager
    :var self.image: url to the image of the villager
    :var self.quote:
    :var self.gender:
    :var self.personality:
    :var self.species:
    :var self.birthday:
    :var self.sign: villagers zodiac sign
    :var self.phrase:
    :var self.clothes:
    :var self.islander_favorite:
    :var self.islander_allergic:
    :var self.picture: url to an image of the villagers framed picture
    :var self.siblings:
    :var self.skill:
    :var self.goal:
    :var self.fear:
    :var self.fav_clothing:
    :var self.least_fav_clothing:
    :var self.fav_color:
    :var self.coffee_type:
    :var self.coffee_milk:
    :var self.coffee_sugar:
    :var self.link: url to the nookipedia page of the villager
    """

    def __init__(self, data: dict):

        super().__init__(data)
        # self.message = data.get("message")
        self.link = data.get("url")
        self.name = data.get("name")
        self.alt_name = data.get("alt_name")
        self.species = data.get("species")
        self.personality = data.get("personality")
        self.image = data.get("image_url")
        self.quote = data.get("quote")
        self.gender = data.get("gender")
        self.birthday = data.get("birthday")
        self.sign = data.get("sign")
        self.phrase = data.get("phrase")
        self.clothes = data.get("clothes")
        self.islander_favorite = data.get("islander-favorite")
        self.islander_allergic = data.get("islander-allergic")
        self.picture = data.get("picture")
        self.siblings = data.get("siblings")
        self.skill = data.get("skill")
        self.goal = data.get("goal")
        self.fear = data.get("fear")
        self.fav_clothing = data.get("favclothing")
        self.least_fav_clothing = data.get("leastfavclothing")
        self.fav_color = data.get("favcolor")
        self.coffee_type = data.get("coffee-type")
        self.coffee_milk = data.get("coffee-milk")
        self.coffee_sugar = data.get("coffee-sugar")

    @property
    def url(self) -> str:
        return self.link

    @property
    def image_url(self) -> str:
        return self.image
