<script>
	import ReusableBox from "../components/ReusableBox.svelte";
	import NewsCard from "../components/NewsCard.svelte";
    import ItemDirection from "../components/ItemDirection.svelte";
    import TodayBinarySentimentCard from "../components/TodayBinarySentimentCard.svelte";
    import WordPreview from "../components/WordPreview.svelte";
</script>

<svelte:head>
	<title>RNNLA DASHBOARD</title>
	<meta name="description" content="RNNLA Dashboard App" />
</svelte:head>

<section>
	<ReusableBox title="뉴스 목록" marginBottom={28}>
		<ItemDirection direction="row">
			<ItemDirection direction="column" enableExpand={true}>
				<NewsCard isSelected={true} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
				<NewsCard isSelected={false} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
				<NewsCard isSelected={false} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
				<NewsCard isSelected={false} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
				<NewsCard isSelected={false} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
				<NewsCard isSelected={false} marginBottom={0} newsTitle="삼성 반도체 재고, 2년만에 감소"></NewsCard>
			</ItemDirection>
			<NewsCard isSelected={false} marginLeft={16} marginBottom={0} newsContent="반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소반도체 재고, 2년만에 감소"></NewsCard>
		</ItemDirection>
	</ReusableBox>
	<ItemDirection direction="row">
		<ReusableBox title="긍부정 추이" marginRight={28}></ReusableBox>
		<ReusableBox title="금일 비율">
			<ItemDirection direction="column">
				<TodayBinarySentimentCard isPositive={true} percent={60} count={5000}></TodayBinarySentimentCard>
				<TodayBinarySentimentCard isPositive={false} percent={40} count={2000}></TodayBinarySentimentCard>
			</ItemDirection>
		</ReusableBox>
	</ItemDirection>
	<ItemDirection direction="row">
		<ReusableBox title="긍부정 키워드" marginTop={28} marginRight={28}>
				<WordPreview></WordPreview>
		</ReusableBox>	
		<ReusableBox title="긍부정 단어 빈도수" marginTop={28}>
		</ReusableBox>
	</ItemDirection>
</section>

<style>

</style>
