<script lang="ts">
	import { onMount } from 'svelte';
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
	
	interface NewsDataModel {
        title: string;
		link: string;
    }
	let newsDataModels: NewsDataModel[] = [];
	let list;
	onMount(async () => {
		//추후 반영
		// const res = await fetch('newsData.json');
		// newsData = await res.json();
		fetch('./data/test.json')
		.then(response => response.json())
		.then(data => {
			newsDataModels = data;
		})
		.catch(error => console.error('Error fetching JSON:', error));
	});
</script>

<svelte:head>
	<title>RNNLA DASHBOARD</title>
	<meta name="description" content="RNNLA Dashboard App" />
</svelte:head>
<div class="container">
<ItemDirection>
	<Title></Title>
	<ItemDirection direction="row">
			<ReusableBox 
				title='금일 <span class="highlight-color">반도체 시황</span> 기사에선 <span class="good-color">긍정</span> 기사가 많아요!'
				marginTop={30}
				marginRight={10}
				enableExpand={true}
				>
				<Spacer height={2}></Spacer>
				<ItemDirection direction="row" enableCenter={true}>
					<TodayBinarySentimentCard isPositive={true} percent={60} count={5000}></TodayBinarySentimentCard>
					<Spacer width={4}></Spacer>
					<TodayBinarySentimentCard isPositive={false} percent={40} count={2000}></TodayBinarySentimentCard>
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
	
	<ReusableBox title='금일 <span class="highlight-color">반도체 시황</span> 뉴스들도 확인해보세요!' marginTop={20} marginBottom={28} titleIcon={NewsPin}>
		<div class="vs">
			<VirtualScroll
					bind:this={list}
					data={newsDataModels}
					key="id"
					let:data
			>
			<NewsCard newsTitle={data.title} newsLink={data.link}></NewsCard>
			</VirtualScroll>
		</div>
	</ReusableBox>
</ItemDirection>
</div>

<style>
	.container {
		padding: 3rem 4rem 6rem 4rem;
	}
	.vs {
		height: 30rem;
	}
</style>
