from tethys_sdk.base import TethysAppBase, url_map_maker


class Aqwatch(TethysAppBase):
    """
    Tethys app class for Aqwatch.
    """

    name = 'Aqwatch'
    index = 'aqwatch:home'
    icon = 'aqwatch/images/icon.gif'
    package = 'aqwatch'
    root_url = 'aqwatch'
    color = '#c0392b'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='aqwatch',
                controller='aqwatch.controllers.home'
            ), UrlMap(
                name='getCascaderData',
                url='aqwatch/getCascaderData',
                controller='aqwatch.api.getCascaderData'
            ), UrlMap(
                name='getChartDataProcess',
                url='aqwatch/getChartDataProcess',
                controller='aqwatch.api.getChartDataProcess'
            ), UrlMap(
                name='getLayerInfoStat',
                url='aqwatch/getLayerInfoStat',
                controller='aqwatch.api.getLayerInfoStat'
            ),
        )

        return url_maps
