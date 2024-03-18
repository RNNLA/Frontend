<script lang="ts">
    import ItemDirection from "../components/ItemDirection.svelte";
    export let isPositive:Boolean = true;
    export let marginBottom:Number = 16;
    export let percent:Number = 0;
    export let count:Number = 0;
    import thumbsUp from "$lib/images/thumbs-up.svg";
    import thumbsDown from "$lib/images/thumbs-down.svg";
</script>


<ItemDirection direction="row">
    {#if isPositive} 
    <div class="positive-background" style="margin-bottom:{marginBottom}px;">
        <img src={thumbsUp} alt="thumbs up"/>
    </div>
    {:else}
    <div class="negative-background">
        <img src={thumbsDown} alt="thumbs down"/>
    </div>
    {/if}
    <ItemDirection direction="column" enableCenter={true}>
        <div class="text-area {isPositive? 'positive-text' : 'negative-text'}">{isPositive? '긍정' : '부정'} {percent}%</div>
        <div class="text-area {isPositive? 'positive-text' : 'negative-text'}">{count}건</div>
    </ItemDirection>
</ItemDirection>


<style>
    .text-area {
        margin-left: 1.25em;
        font-size: 1.25em;
        font-weight: 500;
    }
    .positive-text {
        color : #4F641A;
    }
    .negative-text {
        color : #D43C36;
    }
    .positive-background {
        padding: 2em;
        background-color: rgba(152,192,57, 0.3);
        border-radius: 50%;
    }
    .negative-background {
        padding: 2em;
        background-color: rgba(212,60,54, 0.3);
        border-radius: 50%;
    }
    img {
        width: 2em;
    }
</style>