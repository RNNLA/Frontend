<script lang="ts">
    export let marginBottom: Number = 16;
    export let percent: Number = 0;
    export let count: Number = 0;

    interface RankPartModel {
        rank: Number;
        word: String;
        sentiment: String;
        count: Number;
    }
    let rankPartModels: RankPartModel[] = JSON.parse(`
        [
            { "rank": 1, "word": "반도체", "sentiment":"긍정", "count": 1000 },
            { "rank": 2, "word": "미국", "sentiment":"부정", "count": 800 },
            { "rank": 3, "word": "중국", "sentiment":"부정", "count": 500 }
        ]
    `);
</script>
<div class="flex-container">
    <table>
        <thead>
            <tr class="table-header">
                <th>순위</th>
                <th>단어</th>
                <th>긍부정</th>
                <th>건수</th>
            </tr>
        </thead>
        <tbody>
            {#each rankPartModels as model}
                <tr>    
                    <td class="number">{model.rank}</td>
                    <td class="word">{model.word}</td>
                    <td class="sentiment {model.sentiment == '긍정' ? 'good-color':'bad-color'}">{model.sentiment}</td>
                    <td class="number">{model.count}</td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    table {
        border-collapse: collapse;
        width: 100%;
    }
    tr {
        text-align: center;
        font-size: 2rem;
    }
    th, td {
        font-size: 2rem;
        padding: 0.5em;
        font-weight: 500;
    }
    .table-header {
        padding-top: 0.5em; padding-bottom: 0.5em;
        border-top: rgba(51,54,63,.24) 0.063rem solid; border-bottom:rgba(51,54,63,.1) 0.063rem solid;
        color: rgba(51,54,63,.4);
    }

    .number {
        text-align: center;
    }
    .sentiment {
        text-align: center;
    }
    .word {
        text-align: start;
    }

    .flex-container {
        display: flex;
        flex-direction: row;
        width: 100%; /* flex-container의 가로길이 */
    }
</style>
