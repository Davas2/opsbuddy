from opsbuddy import config as _config

_cache: dict | None = None
_lang_cache: str | None = None


def _load(lang: str) -> dict:
    if lang == "en":
        from opsbuddy.locale import en
        return en.STRINGS
    from opsbuddy.locale import pt
    return pt.STRINGS


def t(key: str, **kwargs) -> str:
    global _cache, _lang_cache
    lang = _config.get("language") or "pt"
    if lang != _lang_cache:
        _cache = _load(lang)
        _lang_cache = lang
    text = _cache.get(key, key)
    return text.format(**kwargs) if kwargs else text


def learn_registry() -> tuple[dict, list[str]]:
    lang = _config.get("language") or "pt"
    if lang == "en":
        from opsbuddy.locale import en
        return en.LEARN_REGISTRY, en.LEARN_CATEGORIES
    from opsbuddy.locale import pt
    return pt.LEARN_REGISTRY, pt.LEARN_CATEGORIES
