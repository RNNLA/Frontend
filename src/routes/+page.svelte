<script lang="ts">
	import { onMount, afterUpdate, tick } from 'svelte';
	import ReusableBox from "../components/ReusableBox.svelte";
	import NewsCard from "../components/NewsCard.svelte";
    import ItemDirection from "../components/ItemDirection.svelte";
    import TodayBinarySentimentCard from "../components/TodayBinarySentimentCard.svelte";
    import WordPreview from "../components/WordPreview.svelte";
    import WordRankingCard from "../components/WordRankingCard.svelte";
    import Title from "../components/Title.svelte";
    import Spacer from "../components/Spacer.svelte";
	import Graph from "../components/Graph.svelte";
	import NewsPin from "$lib/images/news-pin.png";
	import VirtualScroll from "svelte-virtual-scroll-list"

	import {verificationNewsDataModels, graphDataModels, wordCloudDataModels, data_format} from "../store";


	
	
	interface NewsDataModel {
		id: number;
        title: string;
		link: string;
		is_not_risk: boolean;
    }
	let newsDataModels: NewsDataModel[] = [];
	let list;
	let dataSelector: Number = 0;

	interface Calculation {
		count: number;
		is_not_risk: boolean;
	}
	let countPositive: number;
	let countAll: number;

	let newsLargeTitles: string[] = [];

	onMount(async () => {
		await fetch("./data/" + data_format('VerificationNewsData', '2023-06-26'))
		.then(response => response.json())
		.then(data => {
			verificationNewsDataModels.update(
				models => 
				{models = data;
				return models;})
			newsDataModels = data.filter((value) => 
			{
				return !value.is_not_semicon;
			});
		})
		.catch(error => console.error('Error fetching JSON:', error));

		await fetch("./data/" + data_format('WordCloudData', '2023-06-26'))
		.then(response => response.json())
		.then(data => {
			wordCloudDataModels.update(
				models => 
				{models = data;
				return models;})
		})
		.catch(error => console.error('Error fetching JSON:', error));

		await fetch("./data/" + data_format('GraphData', '2023-06-26'))
		.then(response => response.json())
		.then(data => {
			graphDataModels.update(
				models => 
				{models = data;
				return models;})
		})
		.catch(error => console.error('Error fetching JSON:', error));

		calculateTodayBinarySentiment(newsDataModels);	
		
	});
	
	function selectData(index:Number):NewsDataModel[] {
		if(index === 0)
		 return newsDataModels;
		 
		let copiedModels = JSON.parse(JSON.stringify(newsDataModels));
		
		return copiedModels.filter((value) => {
			return ((value.is_not_risk) && (index===1)) || (!(value.is_not_risk) && (index===2));
		});
	}

	function calculateTodayBinarySentiment(models:NewsDataModel[]) {
		var calculation: {[id: string]: Calculation;} = {
			"positive": {count: 0, is_not_risk: true},
			"negative": {count: 0, is_not_risk: false}
		}
		countAll = models.length;
		
		let positive_model = models.filter((value) => value.is_not_risk === true);
		let negative_model = models.filter((value) => value.is_not_risk === false);

		calculation["positive"].count = positive_model.length;
		calculation["negative"].count = negative_model.length;

		countPositive = calculation["positive"].count
	}


	

	afterUpdate( async () => {
		await tick();
		let scrollSize: number = 30;
		let newsCardItems = document.querySelectorAll("#vs-newscards > div > div.virtual-scroll-wrapper > div.virtual-scroll-item");
		const margin = window.getComputedStyle(newsCardItems[0].children[0].children[0]).getPropertyValue("margin-bottom");
		const elemLength = newsCardItems.length >= 5 ? 5 : newsCardItems.length;
		const elemHeight = newsCardItems[0].scrollHeight;
		scrollSize = elemLength * (elemHeight+parseInt(margin.replaceAll("px", "")));

		document.querySelector("#vs-newscards")?.setAttribute("style", `height: ${scrollSize.toString()}px`);

		for(let i=0; i<=$verificationNewsDataModels.length; i++){
			newsLargeTitles.push($verificationNewsDataModels[i].title);
		}
	})

	
</script>

<svelte:head>
	<title>RNNLA DASHBOARD</title>
	<meta name="description" content="RNNLA Dashboard App" />
</svelte:head>
{#if $graphDataModels.length != 0 && $wordCloudDataModels.length != 0 && $verificationNewsDataModels.length != 0}
<div class="container">
<ItemDirection>
	<Title isPositive={(countPositive > countAll - countPositive)} newsLargeTitles={newsLargeTitles}></Title>
	<ItemDirection direction="row">
			<ReusableBox 
				title='금일 <span class="highlight-color">반도체 시황</span> 기사에선 <span class="{(countPositive > countAll - countPositive) ? "good-color" : "bad-color"}">{(countPositive > countAll - countPositive) ? "긍정" : "부정"}</span> 기사가 많아요!'
				marginTop={30}
				marginRight={10}
				enableExpand={true}
				>
				<Spacer height={2}></Spacer>
				<ItemDirection direction="row" enableCenter={true}>
					<TodayBinarySentimentCard isPositive={true} percent={Math.round((countPositive / countAll) * 100)} count={countPositive} countAll={countAll}></TodayBinarySentimentCard>
					<Spacer width={4}></Spacer>
					<TodayBinarySentimentCard isPositive={false} percent={Math.round(((countAll - countPositive) / countAll) * 100)} count={countAll - countPositive} countAll={countAll}></TodayBinarySentimentCard>
				</ItemDirection>
			</ReusableBox>

		<ReusableBox title="긍·부정 단어 리스트" marginTop={30}>
			<WordRankingCard></WordRankingCard>
		</ReusableBox>
	</ItemDirection>
	<ItemDirection direction="row">
		<ReusableBox title='날짜별 긍·부정 <span class="highlight-color">비율</span>을 확인해보세요!' marginTop={20} marginRight={10} enableExpand={true}>
			<Graph></Graph>
		</ReusableBox>
		<ReusableBox title="긍부정 단어뷰" marginTop={20}>
			<WordPreview></WordPreview>
		</ReusableBox>	
	</ItemDirection>
	
	<ReusableBox title='금일 <span class="highlight-color">반도체 시황</span> 뉴스들도 확인해보세요!' marginTop={20} marginBottom={28} titleIcon={NewsPin} enableFilterBox={true} bind:dataSelector={dataSelector}>
		<div id="vs-newscards">
			{#if dataSelector == 0}
			<VirtualScroll
					bind:this={list}
					data={newsDataModels}
					key="id"
					let:data
			>
				<NewsCard newsTitle={data.title} newsLink={data.link}></NewsCard>
			</VirtualScroll>
			{:else}
			<VirtualScroll
					bind:this={list}
					data={selectData(dataSelector)}
					key="id"
					let:data
			>
				<NewsCard newsTitle={data.title} newsLink={data.link}></NewsCard>
			</VirtualScroll>
			{/if}
		</div>
	</ReusableBox>
</ItemDirection>
</div>
{:else}
<div>Loading</div>
{/if}
<style>
	.container {
		padding: 3rem 4rem 6rem 4rem;
	}
</style>
