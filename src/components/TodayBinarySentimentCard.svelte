<script lang="ts">
    import ItemDirection from "../components/ItemDirection.svelte";
    export let isPositive:Boolean = true;
    export let percent:Number = 0;
    export let count:Number = 0;
    import thumbsUp from "$lib/images/thumbs-up.png";
    import thumbsDown from "$lib/images/thumbs-down.png";
</script>


<ItemDirection direction="row" enableCenter={true}>
    {#if isPositive} 
        <img src={thumbsUp} class="positive-img" alt="thumbs up"/>
    {:else}
        <img src={thumbsDown} class="negative-img" alt="thumbs down"/>
    {/if}
    <ItemDirection direction="column" enableCenter={true}>
        <div class="text-area {isPositive? 'positive-text positive-text' : 'negative-text negative-text'}">{isPositive? '긍정' : '부정'} {percent}%</div>
        <div class="text-area {isPositive? 'positive-text positive-text' : 'negative-text negative-text'}">{count}건</div>
    </ItemDirection>
</ItemDirection>


<style>
    .text-area {
        margin-left: 1.25rem;
        font-weight: 600;
    }

    .positive-text {
        font-size: 2.125rem;
    }
    .negative-text {
        font-size: 1.25rem;
    }

    .positive-img {
        width: 15rem;
        height: 15rem;
        
    }
    .negative-img {
        margin-left: 1.2rem;
        width: 8.75rem;
        height: 8.75rem;
    }
</style>