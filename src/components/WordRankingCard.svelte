<script lang="ts">
    import ItemDirection from "../components/ItemDirection.svelte";
    export let marginBottom:Number = 16;
    export let percent:Number = 0;
    export let count:Number = 0;
</script>

<ItemDirection direction="column">
    <ItemDirection direction="row">
        <div>
            <div>순위</div>
            <div>단어</div>
            <div>긍부정</div>
            <div>건수</div>
        </div>
    </ItemDirection>
</ItemDirection>