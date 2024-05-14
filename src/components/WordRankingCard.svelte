<script lang="ts">
    export let marginBottom: Number = 16;
    export let percent: Number = 0;
    export let count: Number = 0;

    import {onMount, afterUpdate} from 'svelte';

    interface RankPartModel {
        rank: Number;
        word: String;
        count: Number;
        sentiment: String;
    }
    let rankPartModels:RankPartModel[] = JSON.parse(`
        [
            {"rank":1, "word":"반도체", "count":4010, "is_not_risk":false},
            {"rank":2, "word":"중국", "count":2466, "is_not_risk":true},
            {"rank":3, "word":"삼성전자", "count":1882, "is_not_risk":false},
            {"rank":4, "word":"미국", "count":1828, "is_not_risk":true},
            {"rank":5, "word":"HBM","count":1796, "is_not_risk":false},
            {"rank":6, "word":"SK하이닉스", "count":1648, "is_not_risk":false},
            {"rank":7, "word":"분기", "count":1519, "is_not_risk":false},
            {"rank":8, "word":"AI", "count":1494, "is_not_risk":false},
            {"rank":9, "word":"시장", "count":1361, "is_not_risk":false},
            {"rank":10, "word":"제품", "count":1231, "is_not_risk":false}
        ]`).map((obj: { rank: number; word: string; count: number; is_not_risk: boolean; }) => {
            return {
                "rank" : obj.rank,
                "word" : obj.word,
                "count" : obj.count,
                "sentiment" : obj.is_not_risk ? "긍정" : "부정"
            }
        });

        afterUpdate( async () => {
            let scrollSize: number = 30;
            let tableContents = document.getElementById('word-ranking-table');
            const rowCount = 6;
            const rowHeight = tableContents.rows[1].children[0].scrollHeight;
            const padding = window.getComputedStyle(tableContents.rows[1].children[0]).getPropertyValue("padding")
            
            scrollSize = rowCount * (rowHeight - parseInt(padding.replaceAll("px", ""))/2);
            console.log(scrollSize);
            document.querySelector(".flex-container")?.setAttribute("style", `height: ${scrollSize.toString()}px`);
        });

</script>
<div class="flex-container">
    <table id="word-ranking-table">
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
                    <td class="rank">{model.rank}</td>
                    <td class="word">{model.word}</td>
                    <td class="sentiment {model.sentiment == '긍정' ? 'good-color':'bad-color'}">{model.sentiment}</td>
                    <td class="count">{model.count}</td>
                </tr>
            {/each}
        </tbody>
    </table>

</div>

<style>
    td {
        text-align: center;
    }
    table {
        border-collapse: seperate;
        border-spacing:0;
        width: 100%;
    }
    tr {
        text-align: center;
        font-size: 1.625rem;
    }
    th, td {
        font-size: 1.625rem;
        padding: 0.3em;
        font-weight: 500;
    }
    th{
        border-top: rgba(51,54,63,.24) 0.063rem solid; border-bottom:rgba(51,54,63,.1) 0.063rem solid;
    }
    thead{
        position: sticky;
        inset-block-start: 0;
    }
    .table-header {
        padding-top: 0.3em; padding-bottom: 0.3em;
        /* border-top: rgba(51,54,63,.24) 0.063rem solid; border-bottom:rgba(51,54,63,.1) 0.063rem solid; */
        color: rgba(51,54,63,.4);
        background: rgba(255,255,255,1);
    }

    td.rank {
        text-align: center;
    }
    td.sentiment {
        text-align: center;
    }
    td.word {
        text-align: center;
    }
    td.count{
        text-align: end;
    }

    .flex-container {
        display: flex;
        flex-direction: row;
        width: 100%; /* flex-container의 가로길이 */
        height: 20rem;
        overflow-y: auto;
    }
</style>
