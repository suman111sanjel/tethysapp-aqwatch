// import {TethysAppName} from "../config";

let BaseUrl = null;

if (process.env.NODE_ENV === "production") {
        // BaseUrl = "http://localhost:8000";

    BaseUrl = 'http://smog.icimod.org';
} else {
    BaseUrl = "http://localhost:8000";
}

export let Action = {
    Base: BaseUrl,
    // Base : 'http://110.44.114.244:8001/',
    SliceCatalog: "apps/regionaldrought/slicedfromcatalog",
    ForecastChartAPI: 'apps/regionaldrought/ajax/getspatialaverage/',
    CurrentChartAPI: 'apps/regionaldrought/ajax/getspatialaveragecurrent/',
    getCSRFToken: 'regionaldrought/getCSRFToken',

    //emission
    CascaderOptions:'apps/aqwatch/getCascaderData/',
    ChartDataProcess:'apps/aqwatch/getChartDataProcess/',
    LayerInfoStat:'apps/aqwatch/getLayerInfoStat/',
};