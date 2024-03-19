<script lang="ts">
    export let newsTitle = "";
    export let newsContent = "";
    export let isSelected:Boolean = false;
    export let marginLeft: Number = 0;
    export let marginBottom: Number = 12;
</script>

<div class="container  {isSelected ? 'selected' : ''}" style="margin-left: {marginLeft}px; margin-bottom: {marginBottom}px">
   {#if newsTitle != ""}  <div class="title">{newsTitle}</div> {/if}
   {#if newsContent != ""}  <div class="content">{newsContent}</div> {/if}
</div>

<style>
    .container {
        /* overflow: hidden; 내부 요소가 border-radius와 일치하도록 오버플로우를 숨깁니다. */
        display: flex;
        flex-direction: column;
        border-radius: 28px;
        padding: 1em;
        background-color: rgba(51, 54, 63, 0.1);

    }
    .selected {
        border: 0.15em solid rgba(51, 54, 63, 1);
    }
    .title {
        font-size: 1.2em;
    }
    .content {
        display: flex;
        width: 32em;
        padding: 1em;
    }
</style>
