#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@author: Frank 
@contact: frank.chang@shoufuyou.com
@file: book.py
@time: 2018/11/3 下午3:27


view_model 层


统一结构, 调整数据 .




返回缺少的数据, 添加数据,
组合 数据
转换数据

"""

from urllib.parse import unquote, quote

from pprint import pprint


class __BookViewModel:
    """
    描述 特征   类变量,实例变量
    行为  (方法)


    面向过程
    """

    def __init__(self, data, keyword, total=0):

        self.keyword = keyword
        self.data = data
        self.total = total
        self.returned = {
            'books': [],
            'total': 0,
            'keyword': unquote(keyword)
        }

    def package_single(self):
        """

        :param data:  原始数据
        :param keyword: 关键字
        :return:
        """
        try:

            book = self.data[0]
        except IndexError  as e:
            print(e)
            pass
        else:
            self.returned['total'] = 1
            self.returned['books'] = [self.__cut_book_data(book)]

        return self.returned

    def package_collection(self):

        books = self.data

        if books:
            self.returned['total'] = self.total
            self.returned['books'] = [self.__cut_book_data(book) for book in books]

        return self.returned

    @staticmethod
    def __cut_book_data(data):
        """
        裁剪数据

        处理单本书籍,一本

        :param data: 原始数据
        :return:
        """

        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': ';'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book


class BookViewModel:

    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = ';'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.isbn = book.get('isbn', '')
        self.binding = book['binding']
        self.category = book['category']
        self.pubdate= book['pubdate']

    @property
    def introduce(self):
        # summary = filter(lambda x: len(x) > 0, [self.author, self.publisher, self.price])
        summary = filter(lambda x:  True if x else False , [self.author, self.publisher, self.price])

        return '/'.join(summary)


class BookCollection:

    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''
        pass

    def fill_books(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = unquote(keyword)
        self.books = [BookViewModel(book) for book in yushu_book.books]


def test_collection():
    data = {
        "books": [
            {
                "author": [
                    "[清] 曹雪芹 著",
                    "高鹗 续"
                ],
                "binding": "平装",
                "category": "小说",
                "id": 1057,
                "image": "https://img1.doubanio.com/lpic/s1070959.jpg",
                "images": {
                    "large": "https://img1.doubanio.com/lpic/s1070959.jpg"
                },
                "isbn": "9787020002207",
                "pages": "1606",
                "price": "59.70元",
                "pubdate": "1996-12",
                "publisher": "人民文学出版社",
                "subtitle": "",
                "summary": "《红楼梦》是一部百科全书式的长篇小说。以宝黛爱情悲剧为主线，以四大家族的荣辱兴衰为背景，描绘出18世纪中国封建社会的方方面面，以及封建专制下新兴资本主义民主思想的萌动。结构宏大、情节委婉、细节精致，人物形象栩栩如生，声口毕现，堪称中国古代小说中的经 典。\\n由红楼梦研究所校注、人民文学出版社出版的《红楼梦》以庚辰（1760）本《脂砚斋重评石头记》为底本，以甲戌（1754）本、已卯（1759）本、蒙古王府本、戚蓼生序本、舒元炜序本、郑振铎藏本、红楼梦稿本、列宁格勒藏本（俄藏本）、程甲本、程乙本等众多版本为参校本，是一个博采众长、非常适合大众阅读的本子；同时，对底本的重要修改，皆出校记，读者可因以了解《红楼梦》的不同版本状况。\\n红学所的校注本已印行二十五年，其间1994年曾做过一次修订，又十几年过去，2008年推出修订第三版，体现了新的校注成果和科研成果。\\n关于《红楼梦》的作者，原本就有多种说法及推想，“前八十回曹雪芹著、后四十回高鹗续”的说法只是其中之一，这次修订中校注者改为“前八十回曹雪芹著；后四十回无名氏续，程伟元、高鹗整理”，应当是一种更科学的表述，体现了校注者对这一问题的新的认识。\\n现在这个修订后的《红楼梦》是更加完善。",
                "title": "红楼梦",
                "translator": []
            },
            {
                "author": [
                    "蒋勋"
                ],
                "binding": "有声书",
                "category": "港台",
                "id": 8864,
                "image": "https://img3.doubanio.com/lpic/s4080621.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s4080621.jpg"
                },
                "isbn": "9780587900078",
                "pages": "160片CD",
                "price": "NT$ 44800",
                "pubdate": "2003-9-1",
                "publisher": "耕心藝術欣賞工作室",
                "subtitle": "",
                "summary": "http://twartline.myweb.hinet.net/\\n紅樓夢\\n一部大家又熟悉又陌生的「文學」作品，\\n「紅樓夢」是驚人的小說，它使人執迷不悟，\\n「紅樓夢」是可以讀一輩子的書，\\n我們不只是在讀「紅樓夢」，我們在閱讀自己的一生，\\n「紅樓夢」的作者引領我們去看各種不同形式的生命，\\n高貴的、卑賤的、善良的、殘酷的、富有的、貧窮的、美的、醜的，\\n「紅樓夢」的作者通過一個一個不同形式的生命，\\n使我們知道他們為什麼「上進」，為什麼「潔癖」，為什麼「愛」，為什麼「恨」，\\n生命是一種「因果」，\\n看到「因」和「果」的循環輪替，也就有了真正的「慈悲」，\\n「慈悲」其實是真正的「智慧」。\\n「紅樓夢」使讀者在不同的年齡領悟「慈悲」的意義，\\n今為完成大家讀紅樓夢的「心願」，\\n蔣勳教授將分享他讀紅樓夢四十年的心得，\\n陪著大家一起來讀紅樓夢。\\n以講座的方式舉辦，同步收音製作「紅樓夢」CD有聲書發行，\\n深入為您解析紅樓夢裡的每個人物，\\n個性及其背後的隱喻、老莊哲學思想及書中典故，帶領您觸動靈魂深處，\\n「紅樓夢」的閱讀，可以讓你不斷看到「自己」，紅樓夢\\n因此是一種學習「寬容」的過程\\n「紅樓夢」CD有聲書，將是中國第一部以聲音呈現的「文學經典」",
                "title": "细说红楼梦 1-80回",
                "translator": []
            },
            {
                "author": [
                    "西岭雪"
                ],
                "binding": None,
                "category": "杂文",
                "id": 10354,
                "image": "https://img3.doubanio.com/lpic/s4342226.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s4342226.jpg"
                },
                "isbn": "9787512600058",
                "pages": "336",
                "price": "29.80元",
                "pubdate": "2010-3",
                "publisher": "团结出版社",
                "subtitle": "",
                "summary": "《西岒雪探密红楼梦》：一部伤春悲秋，“怀金悼玉”的《红楼梦》，好不热闹地“你方唱罢我登场”，到头来却都是给她人做嫁衣裳；可见《红楼梦》中从来就没有小人物，只不过是一场镜花水月的集合。素有民间 “红学” 研究第一女性之称的西岭雪，以她那精致敏锐的灵性笔触为我们探秘“红楼36钗”人物，凭吊“红楼梦中人”的一场绝世宿命。本书由新版电视剧《红楼梦》制片人李小婉女士独家推荐！",
                "title": "西岭雪探秘红楼梦",
                "translator": []
            },
            {
                "author": [
                    "蔡义江"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12269,
                "image": "https://img3.doubanio.com/lpic/s2181013.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s2181013.jpg"
                },
                "isbn": "9787101028584",
                "pages": "547",
                "price": "38.00元",
                "pubdate": "2004-9",
                "publisher": "中华书局",
                "subtitle": "",
                "summary": "修订重排本的《红楼梦诗词曲赋评注》是在初版的基础上，增添篇目内容，加重艺术分析，改写而成的。书中全收了各种版本《红楼梦》中的诗、词、曲、赋、歌谣、古文、书札、谜语、酒令、联额、对句等体裁形式的文字，包括一般不易见到的脂评抄本中独存的诗作，收录十分齐全。为使读者加深理解，每首都加了“说明”、“注释”、“鉴赏”或“评说”，有的还有“附录”或“备考”，较难读懂的《芙蓉女儿诔》，还加了“译文”。“附编”收了对研究《红楼梦》和曹雪芹有重要参考价值的资料，其中《版本简介》一文，吸收了红学界在这方面的最新研究成果。",
                "title": "红楼梦诗词曲赋鉴赏",
                "translator": []
            },
            {
                "author": [
                    "曹雪芹"
                ],
                "binding": "简裝本",
                "category": "古典文学",
                "id": 12446,
                "image": "https://img3.doubanio.com/lpic/s1463564.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s1463564.jpg"
                },
                "isbn": "9787806654040",
                "pages": "870",
                "price": "23.00元",
                "pubdate": "2004-6",
                "publisher": "岳麓书社",
                "subtitle": "古典名著普及文库",
                "summary": "《红楼梦》是中国最具文学成就的古典文学巨著，它是中国古典文学创作的颠峰之作，是全人类的文化瑰宝。通过对“贾、史、王、薛”四大家族荣衰的描写，展示了广阔的社会生活视野，森罗万象，囊括了多姿多彩的世俗人情。人称《红楼梦》内蕴着一个时代的历史容量，是封建末世的百科全书。",
                "title": "红楼梦",
                "translator": []
            },
            {
                "author": [
                    "曹雪芹",
                    "高鹗"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12484,
                "image": "https://img3.doubanio.com/lpic/s1146630.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s1146630.jpg"
                },
                "isbn": "9787532519248",
                "pages": "1380",
                "price": "71.60元",
                "pubdate": "1995-12-1",
                "publisher": "上海古籍出版社",
                "subtitle": "",
                "summary": "《红楼梦》是中国古典小说举世公认的巅峰，是封建社会的百科全书，也是中华文化的结晶。二百多年来，深受广大读者的欢迎，历久而不衰。这次推出的豪华本《红楼梦》，心版本价值较高的程乙本为底本，并请著名红学家、作家蒋和森先生撰写了怎样读《红楼梦》的前言，著名画家刘旦宅先生创作了精美的插图。全书装帧典雅豪华，版式疏朗大方，既有很高的阅读收藏豪华，版式疏朗大方，既有很高的阅读收藏价值，又是馈赠亲友的最佳礼品。",
                "title": "红楼梦",
                "translator": []
            },
            {
                "author": [
                    "冯其庸"
                ],
                "binding": None,
                "category": "古典文学",
                "id": 12585,
                "image": "https://img3.doubanio.com/lpic/s8872404.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s8872404.jpg"
                },
                "isbn": "9787539235103",
                "pages": "2810",
                "price": "280.00元",
                "pubdate": "2000-8",
                "publisher": "江西教育",
                "subtitle": "",
                "summary": "此书是集清代评点派红学之大成，作者冯其庸先生。本书以《红楼梦》程甲本（清乾隆56年，公元1791年程伟元，高鄂整理本活字本）为底本，同时校以甲戌、己卯、庚辰、戚序、蒙府、梦稿、列藏、梦叙等脂批系统的本子,以及王雪香评双清仙馆本、张新之《妙复轩评〈石头记〉》、王希廉姚燮评《增评补图〈石头记〉》、王张姚合评上海同文书局《增评补像全图〈金玉缘〉》、乾隆壬子程伟元、高鹗萃文书屋木活字本(程乙本)诸本。\\n八大家评批文字分别是道光十二年双清仙馆刊王雪香评本、光绪七年卧云山馆刊妙复轩评《绣像〈石头记红楼梦〉》、光绪年间悼红轩原本王希廉、姚燮评《增评补像全图〈金玉缘〉》、二知道人《〈红楼梦〉说梦》、诸联《〈红楼梦〉评》、涂瀛《〈红楼梦〉论赞》、解盦居士《石头臆说》、洪秋蕃《红楼梦抉隐》。\\n此书所集评点派文字，皆力求其全。例如张新之的评点文字，不取《金玉缘》一书所录，而是取《妙复轩评绣像石头记红楼梦》光绪七年卧云山馆刊本。因《金玉缘》所录皆只一部分评点文字，未得其全，妙复轩本才得其全。但洪秋蕃《红楼梦抉隐》等原是单独印行的书籍，并非附着红楼梦原著的评点文字，而附着红楼梦原著的手批本黄小田、陈其泰诸家评点文字，本书则没有收入。\\n此书共三百五十万字，上中下三巨册。前面有冯先生作《重议评点派》长叙，提出了对评点派红学应重新认识,重新评价的问题。后边有冯先生所作《校红漫议》（校后记）长篇文字，提出了校点《红楼梦》所遇到的疑难和处理的办法。 此书采用评点派传统的排版方式，有眉评、正文下双行小字评、回前评、回后评等。\\n本书初版是由冯其庸纂校订定，陈其欣助纂的《八家评批红楼梦》1991年由文化艺术出版社出版。冯先生在大力推崇脂本石头记之外，对程本红楼梦也表示了的极大关注。",
                "title": "重校《八家评批红楼梦》",
                "translator": []
            },
            {
                "author": [
                    "王国维 著",
                    "苏缨 解说"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12591,
                "image": "https://img3.doubanio.com/lpic/s4592851.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s4592851.jpg"
                },
                "isbn": "9787538730593",
                "pages": "195",
                "price": "26.80元",
                "pubdate": "2010-7",
                "publisher": "时代文艺出版社",
                "subtitle": "",
                "summary": "《王国维点评红楼梦》既是作者王国维红学研究的开山之作，也为红学设定了一个高洁的标准，在中国文学史的宏大背景里解读《红楼梦》的卓尔不群，在西方悲剧美学的框架下理解《红楼梦》的超然境界。\\n《王国维点评红楼梦》以通俗的语言和唯美的彩绘解读王国维的《红楼梦评论》，以文学论文学，以文学论人生。",
                "title": "王国维点评红楼梦",
                "translator": []
            },
            {
                "author": [
                    "曹雪芹",
                    "吴其柔（改编）"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12705,
                "image": "https://img3.doubanio.com/lpic/s2390522.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s2390522.jpg"
                },
                "isbn": "9787532216949",
                "pages": "0",
                "price": "48.00",
                "pubdate": "1996",
                "publisher": "上海人民美术出版社",
                "subtitle": "",
                "summary": "《红楼梦》一个让人遐想的名字，一个让中国人骄傲的名字。记得小时侯，常听大人谈起毛泽东说过的一句话“我们中国有两个骄傲：一个是万里长城，一个是《红楼梦》。”在这份好奇的心境下匆匆地知道了宝玉和林妹妹爱情悲剧，当时随不懂那些风月情浓，却也流了些许的泪。\\n如今，重温旧梦，捧起《红楼梦绘画本》，黛玉葬花！宝钗扑蝶！湘云醉酒！一幅幅凄凉柔美伴着童年的回忆再一次走进那难以言表的“大观园”。",
                "title": "红楼梦（连环画）1-16",
                "translator": []
            },
            {
                "author": [
                    "曹雪芹、高鹗著",
                    "脂砚斋、王希廉点评"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12796,
                "image": "https://img3.doubanio.com/lpic/s3888784.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s3888784.jpg"
                },
                "isbn": "9787101067309",
                "pages": "805",
                "price": "76.00元",
                "pubdate": "2009-06",
                "publisher": "中华书局",
                "subtitle": "",
                "summary": "《红楼梦》是中国古典小说的巅峰之作，鲁迅在《中国小说的历史的变迁》一文中曾分析道：“其要点在敢于如实描写，并无讳饰，和从前的小说叙好人完全是好，坏人完全是坏的，大不相同，所以其中所叙的人物，都是真的人物。总之自有《红楼梦》出来以后，传统的思想和写法都打破了。”《红楼梦》以其丰富的内涵和深刻的描写吸引了一代又一代读者。\\n曹雪芹去世前修订的几次定本《红楼梦》全部定名为《脂砚斋重评石头记》，其最初流传于世的抄本也都带有脂砚斋的评语。但长期以来，更多地保留了曹雪芹的语言个性和思想锋芒的脂评本只以抄本、影印等形式在较小的范围内流传，脂砚斋评语也多以单独的评语辑本为主。为使高居象牙塔的脂评本走入普通读者的生活，为此我们从现存十一二种脂评本中，精选最能反映曹雪芹《红楼梦》原始面貌的乾隆甲戌（1754年）脂砚斋评本即甲戌本、乾隆己卯(1759年)冬月脂砚斋评本即己卯本、乾隆庚辰（1760年）秋月脂砚斋评本即庚辰本进行整理，奉献给读者一部简便、可靠、囊括脂砚斋主要评语、可供普通读者阅读的脂评本。\\n后四十回系高鹗续作，其版本主要程甲本和程乙本。考虑到清代最为流行的王希廉评本用程甲本，因此，后四十回我们选择了程甲本作为底本，王希廉评语以双清仙馆本《新评绣像红楼梦全传》为据，但仅选择了其回末评。\\n全书配以清代人物仕女画家改琦《红楼梦人物画谱》中的金陵十二钗图画，人物形象古雅、传神。正文朱墨参差，提前预思回目动静的回前总评，事后追念其文深意的回末评，不时点醒读者的眉批，乃至眼光瞄准到行文最细微之处，点破文中之“眼”和“微旨”的夹批、侧批，虽然多为寥寥数语，却将曹雪芹在思想上的深刻寓意，叙述上的安排、穿插和对人物的塑造、刻画揭示得淋漓尽致，使读者可以充分领略小说的诸多奥秘。相信这个借鉴吸收先贤时彦研究成果的脂评本会让普通读者体会到阅读经典的快乐。\\n简体横排，双色印刷",
                "title": "红楼梦",
                "translator": []
            },
            {
                "author": [
                    "[美] 余英时"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12865,
                "image": "https://img3.doubanio.com/lpic/s1066362.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s1066362.jpg"
                },
                "isbn": "9787806189580",
                "pages": "256",
                "price": "24.00元",
                "pubdate": "2002-2",
                "publisher": "上海社会科学院出版社",
                "subtitle": "",
                "summary": "《红楼梦的两个世界》汇集余英时研究《红楼梦》的八篇专论。文章考证缜密，论述生动，对把握《红楼梦》的艺术特色，探寻曹雪芹的思想轨迹有指导意义。",
                "title": "红楼梦的两个世界",
                "translator": []
            },
            {
                "author": [
                    "冯其庸"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 12882,
                "image": "https://img1.doubanio.com/lpic/s1173999.jpg",
                "images": {
                    "large": "https://img1.doubanio.com/lpic/s1173999.jpg"
                },
                "isbn": "9787205057596",
                "pages": "2042",
                "price": "268.00",
                "pubdate": "2005-1",
                "publisher": "辽宁人民出版社",
                "subtitle": "",
                "summary": "该书1981年由人民文学出版社出版。而如今这部《瓜饭楼重校评批〈红楼梦〉》则是冯老对《红楼梦》正文做了重新全面校订、将其几十年来评批《红楼梦》的全部成果皆融入一书之中的全新力作，可谓面貌焕然一新的《红楼梦》全新版本。第二，此乃相对前人的学术成就而言。《红楼梦》已然问世200余年，关于《红楼梦》的校订注释评批此前也有成果问世，故此书曰“重校评批”。\\n这部编辑、校对、排版用了五年多时间的评校本《红楼梦》之评批语词分三种形式：一是每页书眉处的眉批。眉批是针对《红楼梦》的段落文字所做的分析与评论，使读者晓明本段的意思。二是《红楼梦》正文中的小字夹批。这是针对某些有特殊含义的句子，或针对特别精彩的文字所做的分析与评论，使读者能够领会这些句子或字词的含义以及精彩之处。三是每回之后的回后批。即于每回之后，做本回之总评，分析、总结本回之要点和精义所在，使读者了解本回的要点和精义在故事发展中的作用。本书的批语以朱砂红色区分于《红楼梦》的墨色正文，眉批、夹批和回后批各有侧重，合而为一，精辟而又全面地展示了《红楼梦》所蕴藏着的深刻内涵。读者把三种评批结合起来读，更能透彻地了解《红楼梦》作者隐寓在本书中的深意。\\n本书开篇为内容非常深刻而又流畅易读的导论――《解读〈红楼梦〉》，这是冯先生聚数十年的功力于一篇文章的精要之作，发前人之所未发，启读者之解悟。\\n本书还有工笔画家谭凤缳专为此书创作的30幅精妙绝伦的插图，更增加此书的欣赏功能和收藏价值。",
                "title": "瓜饭楼重校评批《红楼梦》",
                "translator": []
            },
            {
                "author": [
                    "周汝昌"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 13038,
                "image": "https://img3.doubanio.com/lpic/s3249223.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s3249223.jpg"
                },
                "isbn": "9787542627865",
                "pages": "654",
                "price": "100.00元",
                "pubdate": "1998-5",
                "publisher": "上海三联出版社",
                "subtitle": "",
                "summary": "《红楼梦新证》是一部关于小说《红楼梦》和她的作者曹雪芹的材料考证书，是中华文化艺术史上的一部名著，也是作者的经典作及成名作。胡适对红学开端之后，《红楼梦新证》方是红学的真正“实体”，后来的曹学、脂学、版本学、探佚学等诸多分科，乃至影印的有关资料亦由她而引发。海外著名学者评之为“无可否认的红学方面一部划时代的最重要的著作”、“考证《红楼梦》的基本材料大部分是他一手挖掘出来的”，国内学者则称之为“是任何有志于红学研究的人都无法绕行”的巨著。",
                "title": "红楼梦新证",
                "translator": []
            },
            {
                "author": [
                    "萨孟武"
                ],
                "binding": "平装",
                "category": "古典文学",
                "id": 13067,
                "image": "https://img1.doubanio.com/lpic/s1418087.jpg",
                "images": {
                    "large": "https://img1.doubanio.com/lpic/s1418087.jpg"
                },
                "isbn": "9787563352890",
                "pages": "171",
                "price": "16.00元",
                "pubdate": "2005-5",
                "publisher": "广西师范大学出版社",
                "subtitle": "",
                "summary": "“满纸荒唐言，一把辛酸泪。都云作者痴，谁解其中味”。萨孟武先生以研究社会文化的角度来解读《红楼梦》，引领读者深入贾府的家庭生活，重新认识中国传统家庭，剖示传统社会的文化与伦理格局，演绎社会风气的流转，见解精微，启人心智，是一部别开生面、言近旨远的大家小书。",
                "title": "红楼梦与中国旧家庭",
                "translator": []
            },
            {
                "author": [
                    "曹雪芹"
                ],
                "binding": None,
                "category": "古典文学",
                "id": 13118,
                "image": "https://img3.doubanio.com/lpic/s4466175.jpg",
                "images": {
                    "large": "https://img3.doubanio.com/lpic/s4466175.jpg"
                },
                "isbn": "9787508823737",
                "pages": "1194",
                "price": "120.00元",
                "pubdate": "2010-7",
                "publisher": "龙门书局",
                "subtitle": "",
                "summary": "《蔡义江新评红楼梦(套装上下册)》由以下几个部分构成：第一，精心校勘的红楼梦原文，正本清源，摒弃各本常见谬误，严谨权威，在学界内此版本被誉为“蔡本”；第二，每回前均有题解，细论回目原貌，探讨回目精义；第三，每回后配有总评，从整体上赏鉴本回内容；第四，作者侧批与红楼梦正文分双栏排版，一一对应，解读精细，抽丝剥茧搬地为读者展现出红楼的艺术价值，评注中还收录了上千条脂批，以飨读者。第五，附编有多篇专题文章，系统化地阐述有关红楼的学术问题，是作者一生的心血凝集；另外《蔡义江新评红楼梦(套装上下册)》还附录了红楼的珍贵资料图片以及红楼梦人物关系图表，堪称红楼梦收藏的最佳版本。\\n封面：",
                "title": "蔡义江新评红楼梦",
                "translator": [
                    "蔡义江"
                ]
            }
        ],
        "count": 15,
        "start": 0,
        "total": 34
    }

    keywords = quote('红楼梦')

    view = __BookViewModel(data, keywords)

    ret = view.package_collection()

    pprint(ret)

    pass


def test_single():
    data = {
        "author": [
            "金庸"
        ],
        "binding": None,
        "category": "小说",
        "id": 1936,
        "image": "https://img3.doubanio.com/lpic/s2834105.jpg",
        "images": {
            "large": "https://img3.doubanio.com/lpic/s2834105.jpg"
        },
        "isbn": "9787070511209",
        "pages": None,
        "price": "683",
        "pubdate": "2006-1",
        "publisher": "广州出版社",
        "subtitle": "",
        "summary": None,
        "title": "金庸作品集",
        "translator": []
    }

    keywords = quote('9787070511209')
    # keywords = quote('97870705112091323')

    view = __BookViewModel(data, keywords)

    ret = view.package_single()

    pprint(ret)


if __name__ == '__main__':
    pass

    # q=9787070511209
    # q=红楼梦
