<script lang='ts'>

    import ItemDirection from "../../components/ItemDirection.svelte";
    import VerificationTitle from "./components/VerificationTitle.svelte";
    import VerificationNewsPart from "./components/VerificationNewsPart.svelte";
    import {analysisNewsDataModels, verificationNewsDataModels, data_format, graphDataModels} from "../../store";
    import {onMount} from 'svelte';

    onMount( () => {
        // await fetch("./data/" + data_format('VerificationNewsData'))
		// .then(response => response.json())
		// .then(data => {
		// 	verificationNewsDataModels.update(
		// 		models => 
		// 		{models = data;
		// 		return models;})
		// })
		// .catch(error => console.error('Error fetching JSON:', error));
        
        if($verificationNewsDataModels.length === 0)
            verificationNewsDataModels.update(
                models =>
                {
                    models = JSON.parse(JSON.stringify($analysisNewsDataModels));
                    return models;
                }
            );

        const interval = setInterval(fetchData, 10000); 
        return () => clearInterval(interval); 
        });
        
    async function fetchData() {
        await fetch("http://localhost:8080", {
            method: 'PUT',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    "data": $verificationNewsDataModels
                }
            )
        })
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('JSON 파일이 업데이트되었습니다.', data);
        })
        .catch(error => {
            console.error('에러 발생:', error);
        });
    }   
    
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