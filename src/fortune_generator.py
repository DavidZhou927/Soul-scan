import datetime
import hashlib
import random
from typing import Dict, Any

# 原创签文模板（避免抄袭，短小多样）
_TEMPLATES = [
    {"title": "Plum Blossoms Renewed", "poem": "A plum stands proud in winter; patient roots await spring's return."},
    {"title": "Crane in the Clouds", "poem": "A crane sails the high clouds; keep steady steps and peace will follow."},
    {"title": "Flowing Water", "poem": "Water finds its way; leave gentle traces and move with the current."},
    {"title": "Bamboo and Breeze", "poem": "Bamboo bends but does not break; quiet strength endures the wind."},
    {"title": "River of Stars", "poem": "The starry river guides the night; lift your gaze and follow the light."},
    {"title": "Late Warmth", "poem": "Cold gives way to warmth; patient hearts will see opportunity."},
    {"title": "Snow on the Bridge", "poem": "Snow rests on the old bridge; past paths teach steady steps ahead."},
    {"title": "Wind Through the Woods", "poem": "Wind stirs the leaves; trials feed the roots that hold firm."},
    {"title": "Silkworm's Devotion", "poem": "Toil with quiet purpose; faithful effort yields its reward."},
    {"title": "Waiting at the Ferry", "poem": "Watch the tides without haste; a faithful hope will bring a boat."},
    {"title": "After the Rain", "poem": "Gentle rains nourish small growth; clear skies will bring brighter days."},
    {"title": "Lamp in the Night", "poem": "A single lamp lights a path; hold your inner flame through the dark."},
    {"title": "Beneath the Pine", "poem": "Beneath the pine a quiet wind: ask, listen, and walk with care."},
    {"title": "Smiling Distant Hills", "poem": "Distant hills smile softly; with calm hearts the road is open."},
    {"title": "Leaves of Autumn", "poem": "Falling leaves know the season; let go lightly and step forward."},
    {"title": "Night Rain", "poem": "Night rain carries thoughts away; when it clears, the sky reveals new paths."},
    {"title": "Returning Geese", "poem": "A returning call from afar; small joys warm the traveler’s heart."},
    {"title": "Stone Bridge", "poem": "Old stone bridges bear many feet; each step leaves its honest glow."},
    {"title": "Poem by Lamplight", "poem": "Words shaped under lamplight; care and craft grow into meaning."},
    {"title": "Birdsong in the Valley", "poem": "Morning birds announce the day; listen and take gentle action."}
]

_COLORS = ["Red", "Blue", "Black", "Green", "Gold", "Silver", "Violet", "Indigo"]
_DIRECTIONS = ["East", "South", "West", "North", "Northeast", "Southwest", "Northwest", "Southeast"]


def _seed_from_date(dt: datetime.date) -> int:
    s = dt.isoformat().encode('utf-8')
    h = hashlib.sha256(s).hexdigest()
    # 取一个足够大的整数作为种子
    return int(h[:16], 16)


def generate_fortune(birth_date: datetime.date) -> Dict[str, Any]:
    """基于出生日期生成一个 deterministic 的签文。

    返回字段：category(吉/中/凶), title, poem, score(0-99), advice, lucky_numbers, lucky_color, lucky_direction
    """
    seed = _seed_from_date(birth_date)
    rng = random.Random(seed)

    template = rng.choice(_TEMPLATES)
    score = seed % 100

    if score >= 75:
        category = "Great Luck"
        advice_tone = "Move forward with energy but keep balance; avoid excess."
    elif score >= 40:
        category = "Moderate Luck"
        advice_tone = "Stay steady and act with care; favor cautious choices."
    else:
        category = "Misfortune"
        advice_tone = "Observe and be cautious; avoid rash or impulsive moves."

    # 生成5个幸运数字（1-49）
    lucky_numbers = sorted(rng.sample(range(1, 50), 5))
    lucky_color = rng.choice(_COLORS)
    lucky_direction = rng.choice(_DIRECTIONS)

    # 额外建议，结合分数给出短句
    if score >= 90:
        extra = "Fortune favors bold beginnings; consider new ventures."
    elif score >= 75:
        extra = "Opportunities and risks travel together; proceed mindfully."
    elif score >= 55:
        extra = "Work steadily; steady efforts will bring stable gains."
    elif score >= 40:
        extra = "Hold your ground and avoid reckless moves."
    elif score >= 20:
        extra = "Watch closely and be careful with relationships and finances."
    else:
        extra = "Better to conserve energy now; seek help and ease tensions."

    advice = f"{advice_tone} Recommendation: {extra}"

    return {
        "category": category,
        "title": template["title"],
        "poem": template["poem"],
        "score": score,
        "advice": advice,
        "lucky_numbers": lucky_numbers,
        "lucky_color": lucky_color,
        "lucky_direction": lucky_direction,
        "seed": seed,
        "date": birth_date.isoformat()
    }


if __name__ == "__main__":
    # 小自测
    today = datetime.date.today()
    f = generate_fortune(today)
    print(f)
