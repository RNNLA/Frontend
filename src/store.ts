import { writable } from 'svelte/store'

type VerificationNewsDataModel = {
    title: string;
    link: string;
    is_checked: boolean;
    is_semicon: boolean;
    is_not_risk: boolean;
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

function data_format(name:string, date?:string) : string {
    if (date === undefined) {
        let today = new Date();
        let dd = String(today.getDate()).padStart(2, '0');
        let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        let yyyy = today.getFullYear();

        date = yyyy + "-" + mm + "-" + dd;
    }
    return date + "_" + name + ".json";
}


export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);
export let graphDataModels = writable<GraphDataModel[]>([]);
export let wordCloudDataModels = writable<WordCloudDataModel[]>([]);
export {data_format};