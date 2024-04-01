<script lang="ts">
    import ItemDirection from "./ItemDirection.svelte";

    export let newsTitle:string = "";
    export let newsLink:string = "";
    export let marginLeft: Number = 0;
    export let marginBottom: Number = 12;

    let isMouseOver = false;
    function handleMouseOver() {
        isMouseOver = true;
    }
    function handleMouseOut() {
        isMouseOver = false;
    }
</script>

<a href={newsLink} target="_blank">
    <div 
        on:mouseover={handleMouseOver} 
        on:mouseout={handleMouseOut}
        class="container  
        {isMouseOver ? 'selected  highlight-selected-background-color' : ''}" 
        style="margin-left: {marginLeft}px; margin-bottom: {marginBottom}px"
            >
    
        {#if newsTitle != ""} 
            <ItemDirection direction="row">
                <div class="circle highlight-background-color"></div>
                <div class="title">{newsTitle}</div>
            </ItemDirection>
        {/if}
    </div>
</a>

<style>
    a {
        text-decoration: none;
    }
    .circle {
        height: 0.875rem;
        width: 0.875rem;
        align-self: center;
        margin-left: 1.25rem;
        margin-right: 1.625rem;
        border-radius: 50%;
    }
    .container {
        /* overflow: hidden; 내부 요소가 border-radius와 일치하도록 오버플로우를 숨깁니다. */
        display: flex;
        flex-direction: column;
        padding: 1em;
    }
    .selected {
        border-radius: 18px;
    }
    .title {
        font-size: 2em;
        font-weight: 500;
    }
    .title p {
        color: #5447E5;
    }
    .content {
        display: flex;
        width: 32em;
        padding: 1em;
    }
</style>
