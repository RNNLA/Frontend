<script lang='ts'>

    import ItemDirection from "../../components/ItemDirection.svelte";
    import VerificationTitle from "./components/VerificationTitle.svelte";
    import VerificationNewsPart from "./components/VerificationNewsPart.svelte";
    import Spacer from "../../components/Spacer.svelte";
    import {verificationNewsDataModels} from "../../store";
    
    verificationNewsDataModels.update(models => {
        models =JSON.parse(`
        [
            {
                "title": "(1)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": true,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(2)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(3)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(4)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(6)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(7)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(8)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            },
            {
                "title": "(9)반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력",
                "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101",
                "is_checked": false,
                "is_semicon": true,
                "is_risk": false
            }
        ]
    `);
        return models;
    });
</script>

<ItemDirection direction="column">
    <div class="title-part">
        <VerificationTitle></VerificationTitle>
    </div>
    <div class="content-part">
        <VerificationNewsPart></VerificationNewsPart>
    </div>
</ItemDirection>

<style>
    .title-part {
        display: flex;
        flex-direction: column;
        padding: 4rem 6rem 3rem 6rem;
    }
</style>