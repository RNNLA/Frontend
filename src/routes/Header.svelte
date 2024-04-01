<script>
	import { page } from "$app/stores";
	import github from "$lib/images/github.svg";

	let isMouseOver = false;

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
		<a href="/" aria-current={$page.url.pathname === '/' ? 'page' : undefined}>분석</a>
		<div class="menu_divider"></div>
		<a href="/verification" aria-current={$page.url.pathname === '/verification' ? 'page' : undefined}>검증</a>
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
		height: 1.2em;
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
	}

	.menu a{
		margin-left: 0.5em;
		margin-right: 0.5em;
		display: flex;
		text-align: center;
	}

	.menu_divider{
		border-left: 2px solid #ffffff;
		height: 130%;
		
	}


</style>
