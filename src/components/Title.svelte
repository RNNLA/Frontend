<script lang="ts">
    import {fade, fly} from "svelte/transition";

    export let isPositive:boolean;
    export let newsLargeTitles: string[];

    let currentWord = newsLargeTitles[0]??"";
    let i = 0;
    $: {
        setTimeout(() => {
            i = (i + 1) % newsLargeTitles.length;
            currentWord = newsLargeTitles[i];
        }, 3000);
    }
</script>


<div class="title">금일 <span class="{isPositive ? "good-color" : "bad-color"}">{isPositive ? "긍정" : "부정"}</span> 뉴스</div>
{#key currentWord}
    <div class="title" in:fade={{ duration: 800 }}>
        {currentWord}
    </div>
{/key}



<style>
    .title {
		font-size: 2rem;
		font-weight: bold;
	}
    /* .title span {
        color: #98C039;
    } */
</style>
