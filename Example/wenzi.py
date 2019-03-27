from aip import AipOcr


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def run(path):
    """ 这里输入你创建应用获得的三个参数"""
    APP_ID = '15803909'
    API_KEY = 'd8voMcnrHZ6vadX578TvhRfd'
    SECRET_KEY = 'FjLk1qojipmN5Pcfuj3Wo2SAzX9lURKX'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    image = get_file_content(path)

    data = client.basicAccurate(image).get("words_result")
    result = "\n".join([d["words"] for d in data])
    print(result)
    return result
