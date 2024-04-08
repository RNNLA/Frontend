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
export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);