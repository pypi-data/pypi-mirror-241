from sre_compile import dis
from typing import List
import os

import re
import json
from fuzzywuzzy import fuzz

from ..config import KEYWORDS, DATA_CRAWL


def check_key_belong_to_line(key, words, thres=0.8):
    len_key = len(key.split(" "))
    len_words = len(words)
    if len_key > len_words:
        return words, False

    for i in range(len_words - len_key + 1):
        consider_words = words[i : i + len_key]
        consider_key = " ".join([x.strip() for x in consider_words]).strip()
        similarity_ratio = fuzz.ratio(key.lower(), consider_key.lower()) / 100.0
        if similarity_ratio > thres and similarity_ratio < 1:
            words_of_key = key.split(" ")
            for j in range(i, i + len_key):
                words[j] = words_of_key[j - i]
            return words, True
    return words, False


def postprocess_ocr_with_keywords(
    text_line: str, keywords: List[str] = KEYWORDS, thres: float = 0.85
):
    words = re.split(r"\s|,|-|:|;", text_line)
    for key in keywords:
        words, flag = check_key_belong_to_line(key=key, words=words, thres=thres)
    return " ".join([w.strip() for w in words]).strip()


def get_info_name_type_unsignedname(data: List):
    res = {}
    res["name"] = preprocess_text(data[1])
    res["type"] = data[2]
    res["unsign_name"] = data[3]
    return res


def get_street_for_district(street_parser, province_name: str, district_name: str):
    idx_dict = street_parser
    province_name = revert_preprocess_text(province_name)
    district_name = revert_preprocess_text(district_name)
    if idx_dict.get(province_name) == None:
        return []
    province_dict = idx_dict[province_name]
    district_list = province_dict["district"]
    for district in district_list:
        if district["name"] == district_name:
            return district["street"]
    return []


def parser_geo_json(data: dict = DATA_CRAWL, street_parser_path: str = None):
    street_parser = json.load(open(street_parser_path))
    parser_data = {}
    parser_data["provinces"] = []
    for province_info in data:
        province_dict = get_info_name_type_unsignedname(data=province_info)
        districts = province_info[4]
        province_dict["districts"] = []
        district_names = []
        for district in districts:
            district_dict = get_info_name_type_unsignedname(data=district)
            towns = district[4]
            district_dict["towns"] = []
            for town in towns:
                town_dict = get_info_name_type_unsignedname(town)
                district_dict["towns"].append(town_dict)
            district_dict["street"] = get_street_for_district(
                street_parser=street_parser,
                province_name=province_dict["name"],
                district_name=district_dict["name"],
            )
            if district_dict["name"] not in district_names:
                province_dict["districts"].append(district_dict)
                district_names.append(district_dict["name"])
            else:
                for distr in province_dict["districts"]:
                    if distr["name"] == district_dict["name"]:
                        distr["towns"].extend(district_dict["towns"])

        parser_data["provinces"].append(province_dict)
    return parser_data


def revert_preprocess_text(text):
    text = text.replace("uỷ", "ủy")
    text = text.replace("uỵ", "ụy")
    text = text.replace("uỳ", "ùy")
    text = text.replace("uý", "úy")
    text = text.replace("oá", "óa")
    text = text.replace("oà", "òa")
    return text


def preprocess_text(text):
    text = text.replace("ủy", "uỷ")
    text = text.replace("ụy", "uỵ")
    text = text.replace("ùy", "uỳ")
    text = text.replace("úy", "uý")
    text = text.replace("óa", "oá")
    text = text.replace("òa", "oà")
    return text


def check_has_digit_word(text):
    for idx, word in enumerate(text.split(" ")):
        for char in word:
            if char.isdigit():
                return idx
    return -1


def hard_postprocess(text):
    words = text.split(" ")
    words[0] = words[0].replace("Thơn", "Thôn")
    words[0] = words[0].replace("Thồn", "Thôn")
    text = " ".join(words).strip()
    text = text.replace("ủy", "uỷ")
    text = text.replace("ụy", "uỵ")
    text = text.replace("ùy", "uỳ")
    text = text.replace("úy", "uý")
    text = text.replace("óa", "oá")
    text = text.replace("òa", "oà")
    # text = text.replace("Sơn Đông Linh", "Sơn Đông")
    # text = text.replace("Thị Tránh An", "Thị Trấn Vĩnh An")
    return text


def find_pattern(words, patterns):
    max_similar = 0
    match_pattern = None
    for pattern in patterns:
        pattern_name = pattern["name"]
        len_words_of_hint = len(pattern_name.split(" "))
        if len_words_of_hint > len(words):
            continue
        consider_pattern = " ".join(words[-1 * len_words_of_hint :]).strip()
        similar_score = (
            fuzz.ratio(pattern_name.lower(), consider_pattern.lower()) / 100.0
        )

        if consider_pattern.lower() == pattern_name.lower():
            return 1.0, pattern
        if max_similar < similar_score:
            max_similar = similar_score
            match_pattern = pattern
    if match_pattern is not None:
        idx_digit = check_has_digit_word(match_pattern["name"])
        num_word = len(match_pattern["name"].split(" "))
        if idx_digit >= 0:
            is_replaced_words = words[-1 * num_word :]
            if (
                match_pattern["name"].split(" ")[idx_digit]
                != is_replaced_words[idx_digit]
            ):
                return 0, None
    return max_similar, match_pattern


def postprocess_privince(text: str, parser_data: dict):
    new_text = text
    provinces = parser_data["provinces"]
    word_texts = text.split(" ")
    max_similar, match_province = find_pattern(word_texts, provinces)
    if max_similar > 0.85:
        word_texts[-1 * len(match_province["name"].split(" ")) :] = match_province[
            "name"
        ].split(" ")[:]
        new_text = " ".join(word_texts).strip()
        new_text = postprocess_district(
            new_text,
            match_province,
            pop_element_number=len(match_province["name"].split(" ")),
        )
    return new_text


def postprocess_district(text: str, province: dict, pop_element_number: int):
    new_text = text
    words = text.split(" ")
    province_name_split = words[-1 * pop_element_number :]
    words = words[: len(words) - pop_element_number]
    if not words:
        return new_text
    if words[-1].lower() in ["tp", "t"]:
        province_name_split = [words[-1]] + province_name_split
        words = words[:-1]
    elif fuzz.ratio(" ".join(words[-2:]).strip().lower(), "thành phố") > 90:
        province_name_split = words[-2:] + province_name_split
        words = words[:-2]
    elif fuzz.ratio(words[-1].lower(), "tỉnh") > 90:
        province_name_split = [words[-1]] + province_name_split
        words = words[:-1]
    districts = province["districts"]
    max_similar, match_district = find_pattern(words, districts)
    if max_similar >= 0.8:
        words[-1 * len(match_district["name"].split(" ")) :] = match_district[
            "name"
        ].split(" ")[:]
        words = words + province_name_split
        new_text = " ".join(words).strip()
        new_text = postprocess_town(
            new_text,
            match_district,
            pop_element_number=len(match_district["name"].split(" "))
            + len(province_name_split),
        )
    return new_text


def postprocess_town(text: str, district: dict, pop_element_number: int):
    new_text = text
    words = text.split(" ")
    district_province_name_split = words[-1 * pop_element_number :]
    words = words[: len(words) - pop_element_number]
    if not words:
        return new_text
    if fuzz.ratio(" ".join(words[-2:]).strip().lower(), "thành phố") > 90:
        district_province_name_split = words[-2:] + district_province_name_split
        words = words[:-2]
    elif fuzz.ratio(" ".join(words[-2:]).strip().lower(), "thị xã") > 90:
        district_province_name_split = words[-2:] + district_province_name_split
        words = words[:-2]
    elif (
        fuzz.ratio(words[-1].lower(), "huyện") > 90
        or fuzz.ratio(words[-1].lower(), "quận") > 90
    ):
        district_province_name_split = [words[-1]] + district_province_name_split
        words = words[:-1]
    elif words[-1].lower() in ["tp", "q", "h"]:
        district_province_name_split = [words[-1]] + district_province_name_split
        words = words[:-1]
    towns = district["towns"]
    max_similar, match_town = find_pattern(words, towns)
    if (max_similar > 0.8) or (
        max_similar > 0.7 and len(match_town["name"].split(" ")) >= 2
    ):
        words[-1 * len(match_town["name"].split(" ")) :] = match_town["name"].split(
            " "
        )[:]
        words = words + district_province_name_split
        consider_text = " ".join(
            words[
                : -1
                * (
                    len(match_town["name"].split(" "))
                    + len(district_province_name_split)
                )
            ]
        ).strip()
        street_names = [
            preprocess_text(x)
            for x in district["street"]
            if len(x.split(" ")) >= 2 and check_has_digit_word(x) < 0
        ]
        street_name = postprocess_ocr_with_keywords(
            consider_text, keywords=street_names
        )
        new_text = (
            street_name
            + " "
            + match_town["name"]
            + " "
            + " ".join(district_province_name_split).strip()
        )
    else:
        street_names = [
            preprocess_text(x)
            for x in district["street"]
            if len(x.split(" ")) >= 3 and check_has_digit_word(x) < 0
        ]
        consider_text = " ".join(words).strip()
        street_name = postprocess_ocr_with_keywords(
            consider_text, keywords=street_names, thres=0.8
        )

        new_text = street_name + " " + " ".join(district_province_name_split).strip()
    return new_text.strip()
