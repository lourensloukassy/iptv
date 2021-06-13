import sys
from urllib.parse import urlencode, parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_URL = sys.argv[0]
# Get the plugin handle as an integer number.
_HANDLE = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'JAPAN VOD XXX': 
                     [{'name': 'EBOD-399 初拍，J罩杯111cm的巨乳少女 七草千岁',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DUT4GCW399.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171030/DUT4GCW399/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'JUFD-378 爆乳美女遭遇色狼 不断堕落的美女秘书',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DVM8JYR378.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171030/DVM8JYR378/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'SDDE-365 客房！美食！露天！！一面吸吮天上掉下来的肉棒一面在人气温泉旅馆内泡汤...甚至还一面作爱！！',
                       'thumb': 'http://img.gjtjjp.com/2017-11/EJH6CXI365.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171030/EJH6CXI365/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'SHE-095 素人比基尼辣妹对大肉棒兴奋不已!! 海岸潮吹搭讪 九十九里篇',
                       'thumb': 'http://img.gjtjjp.com/2017-11/EDT5UKM095.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171030/EDT5UKM095/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'GVG-461 最喜欢巨乳的正太的变态恶作剧 三岛奈津子',
                       'thumb': 'http://img.gjtjjp.com/2017-11/GJL9EBT461.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/GJL9EBT461/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'DVDMS-160 一般男女实验AV 单向玻璃对面是最爱的女友！能看着她被其他男人干到最后就有100万日元！巨乳女友不知道男友在看沉迷于30cm巨根！',
                       'thumb': 'http://img.gjtjjp.com/2017-11/SJEB4TKM160.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/SJEB4TKM160/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'GETS-054 让一直自以为是的不良少年喝下女体化春药，让他变成一个淫蕩女人',
                       'thumb': 'http://img.gjtjjp.com/2017-11/SJR3YLO054.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/SJR3YLO054/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'KUSR-034 公司里人见人爱 美女秘书巨乳紧缚',
                       'thumb': 'http://img.gjtjjp.com/2017-11/RTO7VKD034.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/RTO7VKD034/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'AP-469 公厕美女清洁员体内放尿中出痴汉',
                       'thumb': 'http://img.gjtjjp.com/2017-11/PKE5TH469.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/PKE5TH469/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                      {'name': 'PRED-006 后仰潮喷射 绝顶中出按摩店 樱井彩',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DJE8GHO006.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/DJE8GHO006/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'SHE-468 按摩女的玉手让下体不由自主的勃起硬起来，直接不带套内射！ 21',
                       'thumb': 'http://img.gjtjjp.com/2017-11/EJT4HYO468.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/EJT4HYO468/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'PPPD-590 巨乳女老师的诱惑 香椎梨亚',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DSN0JKQ590.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/DSN0JKQ590/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'CMD-008 诱惑◆按摩沙龙 麻里梨夏',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DA8JKE008.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/DA8JKE008/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'PRED-017 就算快乐到失禁也绝不结束的穷兇极恶胖子的强力交尾 佐佐木明希',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DJ9RHY017.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/DJ9RHY017/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'HUNTA-348 穿着小号泳衣的巨乳年轻人妻去旅行露出乳房，下乳让人挪不开目光超兴奋！',
                       'thumb': 'http://img.gjtjjp.com/2017-11/AJ2RHY348.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/AJ2RHY348/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'EBOD-591 舞蹈曆10年培养出来的惊人身材和扭腰！！九州超有名偶像组合前成员竟然AV出道！！ 松冈美绪',
                       'thumb': 'http://img.gjtjjp.com/2017-11/DFGJ9LOR591.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/DFGJ9LOR591/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'VOSS-046 家里一直都很贫穷 从小学到高中的外号一直都是穷鬼的我靠着奖学金上了大学，为了赚钱在麵包店打工 对一个巨乳太太一见锺情！',
                       'thumb': 'http://img.gjtjjp.com/2017-11/SJKL3TRY046.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/SJKL3TRY046/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'},
                       {'name': 'YST-120 我被胁迫了 古川祥子',
                       'thumb': 'http://img.gjtjjp.com/2017-11/TJKE6BGT120.jpg',
                       'video': 'http://video.feimanzb.com:8091/20171103/TJKE6BGT120/550kb/hls/index.m3u8',
                       'genre': 'JAPAN VOD XXX'}
                      ],
        'LIVE TV XXX': [{'name': 'O-La-La',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/155/mono.m3u8',
                      'genre': 'LIVE TV XXX'},
                     {'name': 'Blacked TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/17/index.m3u8',
                      'genre': 'LIVE TV XXX'},
                     {'name': 'Hustler HD',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/153/mono.m3u8',
                      'genre': 'LIVE TV XXX'},
                     {'name': 'Public Agent TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/35/index.m3u8',
                      'genre': 'LIVE TV XXX'},
                     {'name': 'Sextury HD TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/61/index.m3u8',
                      'genre': 'LIVE TV XXX'},
                      {'name': '21 Naturals TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/67/index.m3u8',
                      'genre': 'LIVE TV XXX'},
                      {'name': 'Blue Hustler TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/151/mono.m3u8',
                      'genre': 'LIVE TV XXX'},
                      {'name': 'Brazzers TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/5/index.m3u8',
                      'genre': 'LIVE TV XXX'},
                      {'name': 'Bang Bros TV',
                      'thumb': '',
                      'video': 'http://iptv.xprime.one/r/21/index.m3u8',
                      'genre': 'LIVE TV XXX'}  
                     ],
    'VIDEO VIRAL': [{'name': 'PRANK OJOL',
                      'thumb': 'https://drive.google.com/uc?export=download&id=1rrahsFLMUhd1zc1YZwfItw_BwUA9h1c7',
                      'video': 'https://drive.google.com/uc?export=download&id=1qVgwxLz75OWvvinQq3tKvdsfFGnZczR-',
                      'genre': 'VIDEO VIRAL'}
                     ]}


def get_url(**kwargs):

    return '{}?{}'.format(_URL, urlencode(kwargs))


def get_categories():

    return VIDEOS.keys()


def get_videos(category):

    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, 'LIVE TV & VOD XXX')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_HANDLE, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_HANDLE, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_HANDLE, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_HANDLE)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_HANDLE, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
