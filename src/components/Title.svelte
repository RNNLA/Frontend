<script lang="ts">
    import {fade, fly} from "svelte/transition";

    let newsLargeTitles: String[] = 
    [
        "HBM發 반도체 회복\"… 수출 경기 전망, 3년 만에 최대",
        "아몰랑",
        "망고",
        "사랑해",
        "나랑 놀자"
    ];
    let currentWord = newsLargeTitles[0];
    let i = 0;
    $: {
        setTimeout(() => {
            i = (i + 1) % newsLargeTitles.length;
            currentWord = newsLargeTitles[i];
        }, 3000);
    }
</script>


<div class="title">금일 <span>긍정</span> 뉴스</div>
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
    .title span {
        color: #98C039;
    }
</style>
