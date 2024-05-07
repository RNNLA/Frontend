<script lang="ts">
    import ItemDirection from "./ItemDirection.svelte";

    export let titleIcon:string = "";
    export let title:String = "";
    export let padding:String = "1.8em"; // 기본 padding 값
    export let background:String = "white"; // 기본 배경색
    export let borderColor:String = "51,54,63,0.08"; // 기본 배경색
    export let cornerRadius:String = "28px"; // 기본 iOS corner 값
    export let marginTop:Number = 0;
    export let marginBottom:Number = 0;
    export let marginLeft:Number = 0;
    export let marginRight:Number = 0;
    export let enableExpand:Boolean = false;
</script>


<div
    class="container {enableExpand? 'expand':''}"
    style="
        padding: {padding};
        background-color: {background};
        border-radius: {cornerRadius};
        border: 0.12em solid rgba({borderColor});
        margin: {marginTop}px {marginRight}px {marginBottom}px {marginLeft}px
    "
>
    {#if title}
        {#if titleIcon} 
            <ItemDirection direction="row">
                <img src={titleIcon} alt="title icon">
                <div class="title">{@html title}</div>
            </ItemDirection>
        {:else}
            <div class="title">{@html title}</div>
        {/if}
    {/if}
    <div class="content"><slot /></div>
    
</div>

<style>
    .container {
        overflow: hidden; /* 내부 요소가 border-radius와 일치하도록 오버플로우를 숨깁니다. */
        display: flex;
        flex-direction: column;
    }
    .title {
        font-size: 2rem;
        font-weight: 700;
        padding-bottom: 0.5em;
    }
    .expand {
        flex-grow: 1;
    }

    img {
        width: 2.8rem;
        height: 2.8rem;
    }

</style>
