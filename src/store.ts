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

type WordDataModel = {
    date: string;
    is_not_risk: boolean;
}

type WordCloudDataModel = {
    date: string;
    word: string;
    is_not_risk: boolean;
}


export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);
export let wordDataModels = writable<WordDataModel[]>([]);
export let wordCloudDataModels = writable<WordCloudDataModel[]>([]);