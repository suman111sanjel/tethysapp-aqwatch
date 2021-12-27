import {getApiWithoutToken,postApiWithoutToken} from './api';
import {Action} from '../actionType';
// import {ThreddsServer} from '../../config';

export async function getCascaderOptions(){
        const action = Action.CascaderOptions
        const response = await getApiWithoutToken(action);
        return response;
}

export async function PostChartDataProcess(param){
        const action=Action.ChartDataProcess;
        const response= await postApiWithoutToken(action,param);
        return response;
}

export async function GETLayerInfoStat(param){
        const action=Action.LayerInfoStat;
        const response= await postApiWithoutToken(action,param);
        return response;
}