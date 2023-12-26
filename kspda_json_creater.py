import json
import pprint

texts = [
         "兵 藤 一 誠",
         "ハ イ ス ク ー ル D D",
         "リ ア ス ・ グ レ モ リ ー",
         "塔 城 子 猫",
         "白 龍 帝",
         "赤 龍 帝",
         "上 級 悪 魔",
         "ジャ ガ ー ノ ー ト ド ラ イ ブ",
         "冥 界",
         "セ イ ク リ ッ ド ギ ア",
         "姫 島 朱 乃",
         "ゼ ノ ヴィ ア",
         "ロ ス ヴァ イ セ",
         "フェ ニ ッ ク ス",
         "ア ザ ゼ ル",
         "オ カ ル ト 研 究 部",
         "堕 天 使",
         "天 使",
         "エ ク ス カ リ バ ー",
         "ミ カ エ ル",
         "天 界",
         "使 い 魔",
         "神 器"
         ]
yomis = [
         "hyou dou i ssei",
         "ha i su ku - ru d d",
         "ri a su . gu re mo ri -",
         "tou jou ko neko",
         "haku ryuu tei",
         "seki ryuu tei",
         "jou kyuu aku ma",
         "ja ga - no - to do ra i bu",
         "mei kai",
         "se i ku ri d do gi a",
         "hime zima ake no",
         "ze no vi a",
         "ro su va i se",
         "fe ni k ku su",
         "a za ze ru",
         "o ka ru to kenn kyuu bu",
         "da tenn si",
         "tenn si",
         "e ku su ka ri ba -",
         "mi ka e ru",
         "tenn kai",
         "tuka i ma",
         "zinn gi"
         ]



a_json = []
for i_1, text in enumerate(texts):
    a_list = []
    for i_2, char in enumerate(text.split()):
        a_dict = {}
        a_dict["char"] = char
        a_dict["YOMI"] = yomis[i_1].split()[i_2]
        a_list.append(a_dict)
    a_json.append(a_list)


with open("static/kspda.json","w", encoding="utf-8") as f:
    json.dump(a_json, f, indent=3,  ensure_ascii=False)
    
pprint.pprint(a_json)