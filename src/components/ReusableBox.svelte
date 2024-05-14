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
    export let enableFilterBox:Boolean = false;
    export let dataSelector:Number = 0;

    let isClickedArray = [true, false, false];

    function doSomething(index:Number)
    {
        isClickedArray = isClickedArray.map((value, i) => {return (i==index)});
        dataSelector = index;
    }

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
                {#if enableFilterBox}
                    <div id="vs-filterbox">
                        <ItemDirection direction="row">
                            <button class="filter {isClickedArray[0] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(0)}>전체</button>
                            <button class="filter {isClickedArray[1] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(1)}>긍정</button>
                            <button class="filter {isClickedArray[2] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(2)}>부정</button>
                        </ItemDirection>
                    </div>
                {/if}
            </ItemDirection>
        {:else}
            <ItemDirection direction="row">
                <div class="title">{@html title}</div>
                {#if enableFilterBox}
                    <div id="vs-filterbox">
                        <ItemDirection direction="row">
                            <button class="filter {isClickedArray[0] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(0)}>전체</button>
                            <button class="filter {isClickedArray[1] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(1)}>긍정</button>
                            <button class="filter {isClickedArray[2] ? "clicked-filter" : ""}" type="button" on:click={() => doSomething(2)}>부정</button>
                        </ItemDirection>
                    </div>
                {/if}
            </ItemDirection>
            
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

    #vs-filterbox {
		height: 2.4rem;
		width: 12.75rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
		border-radius: 14px;
        margin-top: -0.5rem;
        margin-left: 5%;
        transform:translate(0, 25%);
		background-color: var(--color-bg)
	}

	.filter {
        width: 4rem;
		text-align: center;
		font-size: 1rem;
		font-weight: bold;
		color: var(--color-text-opa);
        border-radius: 14px;
        margin: 0 0.125rem 0 0.125rem;
        background-color: var(--color-bg);
	}

    .filter:hover {
        height: 2.4rem;
        color: var(--color-text);
        font-weight: bold;
        background-color: var(--color-bg-opa);
        /* https://smoothshadows.com/#djEsMiwxLDEsNSw1LDAsIzAzMDcxMiwjZmZmZmZmLCNmZmZmZmYsMw%3D%3D */
        box-shadow:
            0px 0.9px 4.5px rgba(0, 0, 0, 0.017),
            0px 2.4px 12.4px rgba(0, 0, 0, 0.025),
            0px 5.7px 29.8px rgba(0, 0, 0, 0.033),
            0px 19px 99px rgba(0, 0, 0, 0.05)
            ;
    }

    .clicked-filter {
        height: 2.4rem;
        color: var(--color-text);
        border: 2px solid black;
        font-weight: bold;
        background-color: rgb(255,255,255);
        /* https://smoothshadows.com/#djEsMiwxLDEsNSw1LDAsIzAzMDcxMiwjZmZmZmZmLCNmZmZmZmYsMw%3D%3D */
        box-shadow:
            0px 0.9px 4.5px rgba(0, 0, 0, 0.017),
            0px 2.4px 12.4px rgba(0, 0, 0, 0.025),
            0px 5.7px 29.8px rgba(0, 0, 0, 0.033),
            0px 19px 99px rgba(0, 0, 0, 0.05)
            ;
    }

    

</style>
