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
	
	interface NewsDataModel {
        title: string;
		link: string;
    }
	let newsDataModels: NewsDataModel[] = JSON.parse(`
        [
            { "title": "반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력", "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101" },
            { "title": "반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력", "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101" },
            { "title": "반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력", "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101" },
            { "title": "반도체 겨울 지났다…삼성전자 1분기 매출 '70조 복귀' 유력", "link": "https://n.news.naver.com/mnews/article/015/0004967080?sid=101" }
        ]
    `);

	onMount(async () => {
		//추후 반영
		// const res = await fetch('newsData.json');
		// newsData = await res.json();
	});
</script>

<svelte:head>
	<title>RNNLA DASHBOARD</title>
	<meta name="description" content="RNNLA Dashboard App" />
</svelte:head>

<section>
	<Title></Title>
	<ItemDirection direction="row">
			<ReusableBox 
				title='금일 <span class="highlight-color">반도체 시황</span> 기사에선 <span class="good-color">긍정</span> 기사가 많아요!'
				marginTop={48}
				enableExpand={true}
				>
				<Spacer height={2}></Spacer>
				<ItemDirection direction="row" enableCenter={true}>
					<TodayBinarySentimentCard isPositive={true} percent={60} count={5000}></TodayBinarySentimentCard>
					<Spacer width={4}></Spacer>
					<TodayBinarySentimentCard isPositive={false} percent={40} count={2000}></TodayBinarySentimentCard>
				</ItemDirection>
			</ReusableBox>

		<ReusableBox title="긍·부정 단어 리스트" marginTop={48} marginLeft={28}>
			<WordRankingCard></WordRankingCard>
		</ReusableBox>
	</ItemDirection>
	<ItemDirection direction="row">
		<ReusableBox title='날짜별 긍·부정 <span class="highlight-color">비율</span>을 확인해보세요!' marginTop={28} enableExpand={true}>
			<Graph svg_width=600 svg_height=400></Graph>
		</ReusableBox>
		<ReusableBox title="긍부정 단어뷰	" marginTop={28} marginLeft={28}>
			<WordPreview></WordPreview>
		</ReusableBox>	
	</ItemDirection>
	<ReusableBox title='금일 <span class="highlight-color">반도체 시황</span> 뉴스들도 확인해보세요!' marginTop={48} marginBottom={28} titleIcon={NewsPin}>
		<ItemDirection direction="row">
			<ItemDirection direction="column" enableExpand={true}>
				{#each newsDataModels as news}
					<NewsCard newsTitle={news.title} newsLink={news.link}></NewsCard>
				{/each}
			</ItemDirection>
			<NewsCard marginLeft={16} marginBottom={0}></NewsCard>
		</ItemDirection>
	</ReusableBox>
	
	
</section>

<style>
	
</style>
