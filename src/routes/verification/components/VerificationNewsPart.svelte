<script lang="ts">
    import { fly, fade } from 'svelte/transition';
    import CheckBox from '../../../components/CheckBox.svelte';
    import ItemDirection from '../../../components/ItemDirection.svelte';
    import Spacer from '../../../components/Spacer.svelte';
    import {verificationNewsDataModels, data_format} from '../../../store';
    import verifiedImg from "$lib/images/verified-icon.png";
    let verificationViewIndex = 0;
    let verificationViewTitleFlyY = 0;
    let fadeDuration = 200;

    function updateVerification(type:string) {
        if (type === "isSemi") {
            $verificationNewsDataModels[verificationViewIndex].is_semicon_by_human = true;
            $verificationNewsDataModels[verificationViewIndex].is_checked = true;
        }
        else if (type === "isNotSemi") {
            $verificationNewsDataModels[verificationViewIndex].is_semicon_by_human = false;
            $verificationNewsDataModels[verificationViewIndex].is_checked = true;
        }
        else if (type === "isRisk") {
            if ($verificationNewsDataModels[verificationViewIndex].is_semicon_by_human)
            {
                $verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human = true;
                $verificationNewsDataModels[verificationViewIndex].is_checked = true;
            }
        }
        else if (type === "isNotRisk") {
            if ($verificationNewsDataModels[verificationViewIndex].is_semicon_by_human)
            {
                $verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human = false;
                $verificationNewsDataModels[verificationViewIndex].is_checked = true;
            }
        }
        fetchData();
    }
    async function fetchData() {
            await fetch("http://localhost:10095", {
                method: 'PUT',
                headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify(
                    {
                        "data": $verificationNewsDataModels
                    }
                )
            })
            .then(response => {
                if (!response.ok) {
                throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log('JSON 파일이 업데이트되었습니다.');
            })
            .catch(error => {
                console.error('에러 발생:', error);
            });
        }   
        

	function onKeyDown(e:any) {
        
        switch(e.keyCode) {
            case 49:
                updateVerification("isSemi");
                break;
            case 50:
                updateVerification("isNotSemi");
                break;
            case 51:
                updateVerification("isRisk");
                break;
            case 52:
                updateVerification("isNotRisk");
                break;
            case 38:
                if (verificationViewIndex > 0) verificationViewIndex -= 1;
                verificationViewTitleFlyY = -40;
                
                break;
            case 40:
                if (verificationViewIndex < $verificationNewsDataModels.length -1) verificationViewIndex += 1;
                verificationViewTitleFlyY = 40;
           
                break;
        }
        
	}
    function handleCheck(event: CustomEvent) {
        const buttonKey = event.detail.buttonKey;
        if (buttonKey === "isSemi") {
            $verificationNewsDataModels[verificationViewIndex].is_semicon_by_human = true;
            $verificationNewsDataModels[verificationViewIndex].is_checked = true;
        }
        else if (buttonKey === "isNotSemi") {
            $verificationNewsDataModels[verificationViewIndex].is_semicon_by_human = false;
            $verificationNewsDataModels[verificationViewIndex].is_checked = true;
        }
        else if (buttonKey === "isRisk") {
            if ($verificationNewsDataModels[verificationViewIndex].is_semicon_by_human)
            {
                $verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human = true;
                $verificationNewsDataModels[verificationViewIndex].is_checked = true;
            }
        }
        else if (buttonKey === "isNotRisk") {
            if ($verificationNewsDataModels[verificationViewIndex].is_semicon_by_human)
            {
                $verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human = false;
                $verificationNewsDataModels[verificationViewIndex].is_checked = true;
            }
        }
        fetchData();
    }
    function restoreVerificationPosition() {
        for (let index = 0; index < $verificationNewsDataModels.length; index++) {
            const verificationNewsData = $verificationNewsDataModels[index];
            if (verificationNewsData.is_checked == false) {
                verificationViewIndex = index;
                break;
            }
        }
    }
    restoreVerificationPosition();
</script>

{#if $verificationNewsDataModels.length > 0}
    {#if verificationViewIndex-2 >= 0}
        {#key $verificationNewsDataModels[verificationViewIndex-2].title}
            <div class="
                verification-pending-part
                {$verificationNewsDataModels[verificationViewIndex-2].is_checked ? 'verified-text-opa' : 'unverified-text-opa'}
            " in:fly={{ y: verificationViewTitleFlyY }}>
                {$verificationNewsDataModels[verificationViewIndex-2].title}
            </div>
        {/key}
    {:else}
        <div class="empty-pending-part" in:fade></div>
    {/if}
    {#if verificationViewIndex-1 >= 0}
        {#key $verificationNewsDataModels[verificationViewIndex-1].title}  
            <div class="
                verification-pending-part
                {$verificationNewsDataModels[verificationViewIndex-1].is_checked ? 'verified-text-opa' : 'unverified-text-opa'}
            " in:fly={{ y: verificationViewTitleFlyY }}>
                {$verificationNewsDataModels[verificationViewIndex-1].title}
            </div>
        {/key}
    {:else}
        <div class="empty-pending-part"></div>
    {/if}
    <div class="
        verification-part
        {$verificationNewsDataModels[verificationViewIndex].is_checked? 'verified-text':''}
    ">
            <ItemDirection direction="row">
                <div class="label-box highlight" in:fade={{duration:fadeDuration}} out:fade={{duration:fadeDuration}}>
                    예측:{$verificationNewsDataModels[verificationViewIndex].is_not_semicon ? '일반 기사' : '반도체 시황'}
                </div>
                {#if !$verificationNewsDataModels[verificationViewIndex].is_not_semicon}
                    <Spacer width={1}></Spacer>
                    <div class="
                        label-box
                        {$verificationNewsDataModels[verificationViewIndex].is_not_risk? 'positive':'negative'}
                    " in:fade={{duration:fadeDuration}} out:fade={{duration:fadeDuration}}>
                        예측:{$verificationNewsDataModels[verificationViewIndex].is_not_risk? '긍정' : '부정'}    
                    </div>
                {/if}
                <Spacer width={1}></Spacer>
                {#if $verificationNewsDataModels[verificationViewIndex].is_checked}
                    <img class="verified-img" src={verifiedImg} alt="verified img" in:fade={{duration:fadeDuration}} out:fade={{duration:fadeDuration}}>
                    <div class="label-box verified" in:fade={{duration:fadeDuration}} out:fade={{duration:fadeDuration}}>검증완료된 기사</div>
                {/if}
                <div class="progress-stage">{verificationViewIndex+1}/{$verificationNewsDataModels.length}</div>
                <Spacer width={1.5}></Spacer>
                <button class="label-box" on:click={restoreVerificationPosition}>미검증 탐색</button>
            </ItemDirection>
            <Spacer height={1.5}></Spacer>
            {#key $verificationNewsDataModels[verificationViewIndex].title}
                <div in:fly={{ y: verificationViewTitleFlyY }}>{$verificationNewsDataModels[verificationViewIndex].title}</div>
            {/key}
            <Spacer height={1.5}></Spacer>
            <ItemDirection direction="row">
                <CheckBox title="반도체 시황" buttonKey="isSemi" on:click={handleCheck} 
                    isChecked={$verificationNewsDataModels[verificationViewIndex].is_semicon_by_human}
                    >
                </CheckBox>
                <Spacer width={.8}></Spacer>
                <CheckBox title="시황 아님" buttonKey="isNotSemi" on:click={handleCheck}
                    isChecked={!$verificationNewsDataModels[verificationViewIndex].is_semicon_by_human}
                    isPositive={false}>
                </CheckBox>
                <Spacer width={2}></Spacer>
                <CheckBox title="긍정 기사" buttonKey="isRisk" on:click={handleCheck}
                    isChecked={$verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human}
                    isDisabled={!$verificationNewsDataModels[verificationViewIndex].is_semicon_by_human}>
                </CheckBox>
                <Spacer width={.8}></Spacer>
                <CheckBox title="부정 기사" buttonKey="isNotRisk" on:click={handleCheck}
                    isChecked={!$verificationNewsDataModels[verificationViewIndex].is_not_risk_by_human}
                    isDisabled={!$verificationNewsDataModels[verificationViewIndex].is_semicon_by_human}
                    isPositive={false}>
                </CheckBox>
            </ItemDirection>
    </div>
    
    {#if verificationViewIndex+1 < $verificationNewsDataModels.length}
        {#key $verificationNewsDataModels[verificationViewIndex+1].title}
            <div class="
                verification-pending-part
                {$verificationNewsDataModels[verificationViewIndex+1].is_checked ? 'verified-text-opa' : 'unverified-text-opa'}
            " in:fly={{ y: verificationViewTitleFlyY }}>
                {$verificationNewsDataModels[verificationViewIndex+1].title}
            </div>
        {/key}
    {:else}
        <div class="empty-pending-part"></div>
    {/if}
    {#if verificationViewIndex+2 < $verificationNewsDataModels.length}
        {#key $verificationNewsDataModels[verificationViewIndex+2].title}
            <div class="
                verification-pending-part
                {$verificationNewsDataModels[verificationViewIndex+2].is_checked ? 'verified-text-opa' : 'unverified-text-opa'}
            " in:fly={{ y: verificationViewTitleFlyY }}>
                {$verificationNewsDataModels[verificationViewIndex+2].title}
            </div>
        {/key}
    {:else}
        <div class="empty-pending-part"></div>
    {/if}
{/if}

<style>
    .empty-pending-part {
        height: 50.5px;
    }
    .verification-pending-part {
        align-self: center;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
    }
    .verification-part {
        font-size: 3rem;
        font-weight: 700;
        padding: 1.5rem 3rem 1.5rem 3rem;
        background-color: rgba(255,255,255,1.0);
        border-radius: 2rem;
        margin: 1rem 0rem 1rem 0rem;
    }
    .verified-text {
        color: #FF832A;
    }
    .unverified-text-opa {
        color: rgba(51, 54, 63, 0.08);
    }
    .verified-text-opa {
        color: rgba(255, 131, 42, 0.25);
    }
    .label-box {
        border: none;
        padding: .5rem 1.2rem .5rem 1.2rem;
        border-radius: 1.25rem;
        color: #FFFFFF;
        font-size: 2rem;
        font-weight: 600;
    }
    .label-box.highlight {
        background-color: var(--highlight-color);
    }
    .label-box.positive {
        border-color: var(--positive-color);
        color: var(--positive-color);
        background-color: var(--positive-color-opa);
    }
    .label-box.negative {
        border-color: var(--negative-color);
        color: var(--negative-color);
        background-color: var(--negative-color-opa);
    }
    .label-box.verified {
        margin-top: auto;
        margin-bottom: auto;
        color: var(--positive-color);
        justify-self: center;
    }
    button.label-box  {
        font-weight: 700;
        color: var(--highlight-color);
        background-color: var(--highlight-color-opa);
    }
    button.label-box:active{
        background-color: var(--highlight-color-deep-opa);
    }
    .verified-img {
        margin-top: auto;
        margin-bottom: auto;
        height: 2.5rem;
        width: 2.5rem;
    }
    .progress-stage {
        margin-left: auto;
        font-size: 2rem;
        right: 40px;
        align-self: center;
        color: var(--highlight-color);
    }
</style>

<svelte:window on:keydown|preventDefault={onKeyDown} />
