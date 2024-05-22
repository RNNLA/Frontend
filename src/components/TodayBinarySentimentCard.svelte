<script lang="ts">
    import ItemDirection from "../components/ItemDirection.svelte";
    export let isPositive:Boolean = true;
    export let percent:number = 0;
    export let count:number = 0;
    export let countAll:number = 0;
    import thumbsUp from "$lib/images/thumbs-up.png";
    import thumbsDown from "$lib/images/thumbs-down.png";
    import {afterUpdate} from 'svelte';

    const imgsizeMax = 14;
    const imgsizeMin = 4;
    const fontsizeMax = 2.25;
    const fontsizeMin = 1.125; 

    
    
    afterUpdate( () => {
        const rootFontSize:number = parseFloat(window.getComputedStyle(document.documentElement).fontSize);
        const imgRatio = (imgsizeMax - imgsizeMin) * (percent / 100) + imgsizeMin;
        const fontRatio = (fontsizeMax - fontsizeMin) * (percent / 100) + fontsizeMin;

        const imgsize = Math.round(rootFontSize * imgRatio * 1000) / 1000;
        const fontsize = Math.round(rootFontSize * fontRatio * 1000) / 1000;

        const img = document.querySelector(`#${isPositive ? "TodayBinarySentimentPosImg" : "TodayBinarySentimentNegImg"}`);
        img?.setAttribute("width", imgsize.toString());
        img?.setAttribute("height", imgsize.toString());
        
    });
    



</script>


<ItemDirection direction="row" enableCenter={true}>
        {#if isPositive}
            <img id="TodayBinarySentimentPosImg" src={thumbsUp} alt="thumbs up"/>
        {:else}
            <img id="TodayBinarySentimentNegImg" src={thumbsDown} alt="thumbs down"/>
        {/if}
    <ItemDirection direction="column" enableCenter={true}>
        <div class="TodayBinarySentimentTexts">
            <div class="text-area {isPositive ? 'positive-text' : 'negative-text'} {(count > (countAll - count)) ? 'bigger-text' : 'smaller-text'}">{isPositive? '긍정' : '부정'} {percent}%</div>
            <div class="text-area {isPositive ? 'positive-text' : 'negative-text'} {(count > (countAll - count)) ? 'bigger-text' : 'smaller-text'}">{count}건</div>
        </div>
    </ItemDirection>
</ItemDirection>


<style>
    .text-area {
        margin-left: 1rem;
        font-weight: 600;
    }

    .bigger-text {
        font-size: 2rem;
    }
    .smaller-text {
        font-size: 1.5rem;
    }

</style>