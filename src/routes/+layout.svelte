<script>
	import Header from '../components/Header.svelte';
	import './styles.css';
</script>

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
	}
	main {
		display: flex;
		align-items: start;
		align-self: center;
		/* min-height: 80vh; */
		/* height: 80vh; */
	}

</style>
