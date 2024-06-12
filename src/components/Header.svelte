<script>
	import { page } from "$app/stores";
	import github from "$lib/images/github.svg";
    import { fade } from "svelte/transition";
	
	import ItemDirection from "./ItemDirection.svelte";

	let isMouseOver = false;
	let isMouseClick = false;

	function handleMouseOver() {
		isMouseOver = true;
	}
	function handleMouseOut() {
		isMouseOver = false;
	}
</script>

<header>
	<div class="left_corner">
		<a href="/">RNNLA DASHBOARD</a>
	</div>
	<div class="menu">
		<ItemDirection direction="column" enableCenter={true}>
			<a href="/" aria-current={$page.url.pathname === '/' ? 'page' : undefined} >분석</a>
			{#if $page.url.pathname === '/'}
				<div class="menu_cur" in:fade></div>
			{/if}
		</ItemDirection>
		<div class="menu_divider"></div>
		<ItemDirection direction="column" enableCenter={true}>
			<a href="/verification" aria-current={$page.url.pathname === '/verification' ? 'page' : undefined}>검증</a>
			{#if $page.url.pathname === '/verification'}
				<div class="menu_cur" in:fade></div>
			{/if}
		</ItemDirection>
		
	</div>
	<div class="right_corner">
		<a href="https://github.com/RNNLA">
			<img src={github} alt="GitHub" />
		</a>
	</div>
</header>



<style>
	header {
		display: flex;
		background-color: #33363f;
		align-items: center;
	}

	header a {
		font-size: large;
		font-weight: 700;
		height: 100%;
		align-items: center;
		color: white;
		text-decoration: none;

	} 

	header a:hover{
		background-color: rgba(208, 213, 215, 0.616);
		border-radius: 4px;
	}

	header img {
		width: 2em;
		height: 2em;
	}

	.left_corner{
		text-align: center;
		padding: 1em;
	}

	.right_corner{
		margin-left: auto;
		margin-right: 0.5em;
	}

	.right_corner a{
		display: flex;
		justify-content: center;;
	}

	.menu{
		margin-left: 2em;
		display: flex;
		flex-direction: row;
		align-items: center; 

	}

	.menu a{
		padding:0.2em;
		margin-left: 0.5em;
		margin-right: 0.5em;
		display: flex;
		flex:auto;
		text-align: center;
		flex: 1 0 auto;
	}

	.menu_divider{
		border-left: 2px solid #ffffff;
		height: 1.2em;
	}

	.menu_cur{
		height: 0.32em;
		width: 0.32em;
		margin-top : 0.1em;
		background-color: white;
		border-radius: 50%;
		display: inline-block;
	}

	.menu_not_cur{
		display: none;
	}


</style>
