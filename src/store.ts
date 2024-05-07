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
    is_not_risk: boolean;
    count: number;
}

type WordCloudDataModel = {
    rank: number;
    word: string;
    is_not_risk: boolean;
    count: number;
}


export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);
export let graphDataModels = writable<GraphDataModel[]>([]);
export let wordCloudDataModels = writable<WordCloudDataModel[]>([]);