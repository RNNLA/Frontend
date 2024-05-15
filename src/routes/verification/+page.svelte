<script lang='ts'>

    import ItemDirection from "../../components/ItemDirection.svelte";
    import VerificationTitle from "./components/VerificationTitle.svelte";
    import VerificationNewsPart from "./components/VerificationNewsPart.svelte";
    import {verificationNewsDataModels, data_format} from "../../store";
    import {onMount} from 'svelte';

    onMount(async () => {
        await fetch("./data/" + data_format('VerificationNewsData', '2023-06-26'))
		.then(response => response.json())
		.then(data => {
			verificationNewsDataModels.update(
				models => 
				{models = data;
				return models;})
		})
		.catch(error => console.error('Error fetching JSON:', error));
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