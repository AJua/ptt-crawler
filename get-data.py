from PttWebCrawler.crawler import *
import json

c = PttWebCrawler(as_lib=True)

# boards = [ 'Gossiping', 'Kaohsiung', 'C_Chat', 'Stock', 'Baseball', 'Lifeismoney', 'NBA', 'HatePolitics', 'car', 'sex', 'Beauty', 'MobileComm', 'joke', 'WomenTalk', 'NSwitch', 'marriage', 'Tech_Job', 'LoL', 'Boy-Girl', 'KoreaDrama', 'ToS', 'home-sale', 'PlayStation', 'PC_Shopping', 'KoreaStar', 'movie', 'BabyMother', 'e-shopping', 'KR_Entertain', 'AllTogether', 'marvel', 'AnimalForest', 'Steam', 'japanavgirls', 'Tainan', 'creditcard', 'CVS', 'ONE_PIECE', 'CFantasy', 'TWICE', 'StupidClown', 'TaichungBun', 'iOS', 'MakeUp', 'BeautySalon', 'HardwareSale', 'Salary', 'Gamesale', 'PokemonGO', 'FATE_GO', 'Food', 'AC_In', 'Hsinchu', 'Japandrama', 'Elephants', 'biker', 'China-Drama', 'MuscleBeach', 'PCReDive', 'BuyTogether', 'cat', 'Japan_Travel', 'WOW', 'CarShop', 'EAseries', 'Option', 'YuanChuang', 'watch', 'nb-shopping', 'Headphone', 'MacShop', 'forsale', 'Isayama', 'mobilesales', 'SportLottery', 'Soft_Job', 'PuzzleDragon', 'Hearthstone', 'gay', 'Brand', 'E-appliance', 'Finance', 'studyteacher', 'Monkeys', 'TypeMoon', 'KoreanPop', 'Gov_owned', 'BB-Love', 'MLB', 'Military', 'TaiwanDrama', 'TW_Entertain', 'Examination', 'MobilePay', 'Palmar_Drama', 'Audiophile', 'Aviation', 'GBF', 'fastfood', 'part-time', 'DMM_GAMES', 'feminine_sex', 'Key_Mou_Pad', 'FITNESS', 'lesbian', 'DIABLO', 'AzurLane', 'PublicServan', 'Wanted', 'BabyProducts', 'MH', 'ShuangHe', 'Bank_Service', 'basketballTW', 'studyabroad', 'DC_SALE', 'PathofExile', 'Teacher', 'hypermall', 'facelift', 'Chiayi', 'LoveLive_Sip', 'CN_Entertain', 'cookclub', 'Foreign_Inv', 'Lions', 'ChungLi', 'Guardians']

boards = [ 'Gossiping', 'Kaohsiung', 'C_Chat', 'Stock', 'Baseball', 'Lifeismoney', 'NBA', 'HatePolitics', 'car', 'sex', 'Beauty', 'MobileComm', 'joke', 'WomenTalk', 'NSwitch', 'marriage', 'Tech_Job', 'LoL', 'Boy-Girl', 'KoreaDrama', 'ToS', 'home-sale', 'PlayStation', 'PC_Shopping', 'KoreaStar', 'movie', 'BabyMother', 'e-shopping', 'KR_Entertain', 'AllTogether', 'marvel', 'AnimalForest', 'Steam', 'japanavgirls', 'Tainan', 'creditcard', 'CVS', 'ONE_PIECE', 'CFantasy', 'TWICE', 'StupidClown', 'TaichungBun', 'iOS', 'MakeUp', 'BeautySalon', 'HardwareSale', 'Salary', 'Gamesale', 'PokemonGO', 'FATE_GO', 'Food', 'AC_In', 'Hsinchu', 'Japandrama', 'Elephants', 'biker', 'China-Drama', 'MuscleBeach', 'PCReDive', 'BuyTogether', 'cat', 'Japan_Travel', 'WOW', 'CarShop', 'EAseries', 'Option', 'YuanChuang', 'watch', 'nb-shopping', 'Headphone', 'MacShop', 'forsale', 'Isayama', 'mobilesales', 'SportLottery', 'Soft_Job']

for b in boards:
    lastPage = c.getLastPage(b)
    c.parse_articles(lastPage - 100, lastPage, b)

# c.parse_articles(1, c.getLastPage('Soft_Job'), 'Soft_Job')
# c.parse_articles(1, c.getLastPage('Tech_Job'), 'Tech_Job')
# c.parse_articles(1, 100, 'PublicServan')

