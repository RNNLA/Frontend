import { writable } from 'svelte/store'

type VerificationNewsDataModel = {
    id: number;
    title: string;
    link: string;
    is_not_semicon: boolean;
    is_not_risk: boolean;
    timestamp: string;
    is_checked: boolean;
    is_semicon_by_human: boolean;
    is_not_risk_by_human: boolean;
}

type GraphDataModel = {
    date: string;
    positive_count: number;
    negative_count: number;
}

type WordCloudDataModel = {
    rank: number;
    word: string;
    is_not_risk: boolean;
    count: number;
}

function data_format(name:string, final_string:string=".json", time_interval?:number, date?:string) : string {
    if (date === undefined && time_interval === undefined) {
        let today = new Date();
        let dd = String(today.getDate()).padStart(2, '0');
        let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        let yyyy = today.getFullYear();

        date = yyyy + "-" + mm + "-" + dd;
    }
    else if (date === undefined && time_interval !== undefined){
        let today = new Date();
        let yesterday = new Date(today.getTime() - 24 * 60 * 60 * 1000);
        let dd = String(yesterday.getDate()).padStart(2, '0');
        let mm = String(yesterday.getMonth() + 1).padStart(2, '0'); //January is 0!
        let yyyy = yesterday.getFullYear();

        date = yyyy + "-" + mm + "-" + dd;
    }
    return date + "_" + name + final_string;
}




export let analysisNewsDataModels = writable<VerificationNewsDataModel[]>([]);
export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);
export let graphDataModels = writable<GraphDataModel[]>([]);
export let wordCloudDataModels = writable<WordCloudDataModel[]>([]);
export let newsCardHeight = writable(-1), wordRankingHeight = writable(-1);
export {data_format};