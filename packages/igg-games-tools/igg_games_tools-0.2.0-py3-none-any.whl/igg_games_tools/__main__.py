import igg_games_tools


def main():
    print(name := input("输入游戏名："))

    print("从 steamdb 搜索相关游戏...")
    names = igg_games_tools.related_games(name=name)
    if len(names) == 0:
        print("没有找到相关游戏")
    else:
        name = names[0]
        print("搜索到最相关的游戏为", name)

    print("从 igg-games.com 中搜索游戏...")
    url = igg_games_tools.search_igg_games(name)[0]
    print("最佳搜索结果为", url)

    print("爬取 Megaup 下载链接...")
    links = igg_games_tools.list_all_download_url(url)
    url = dict(links)['MegaUp.net']
    print("Megaup 下载链接为", url)

    print("解析 bluemedia 链接...")
    url = igg_games_tools.parse_bluemedia_url(url)
    print("Bluemedia 下载链接为", url)

    print("组装 Megaup 下载链接...")
    url = igg_games_tools.pack_megaup_url(url)
    print("Megaup 下载链接为", url)


if __name__ == '__main__':
    main()
