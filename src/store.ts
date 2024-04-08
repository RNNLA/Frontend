import { writable } from 'svelte/store'

type VerificationNewsDataModel = {
    title: string;
    link: string;
    is_checked: boolean;
    is_semicon: boolean;
    is_not_risk: boolean;
}
export let verificationNewsDataModels = writable<VerificationNewsDataModel[]>([]);