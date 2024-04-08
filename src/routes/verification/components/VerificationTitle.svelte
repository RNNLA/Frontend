<script lang="ts">
    import type { VerificationNewsDataModel} from '$lib/models';
    import Spacer from "../../../components/Spacer.svelte";
    import { verificationNewsDataModels } from '../../../store';
    
</script>

{#if $verificationNewsDataModels.length > 0}
    <div class="title">기사 검증이 {$verificationNewsDataModels.length}건 중 {$verificationNewsDataModels.filter(model => model.is_checked).length}건이 완료되었어요.</div>
    <div class="progress-title highlight-color">
        {($verificationNewsDataModels.filter(model => model.is_checked).length / $verificationNewsDataModels.length)*100}% 검증완료</div>
{:else}
    <div>현재 검증할 기사가 없습니다.</div>
{/if}

<style>
    .title {
        font-size: 2.5rem;
        font-weight: 600;
    }
    .progress-title {
        font-size: 3rem;
        font-weight: 700;
    }
</style>